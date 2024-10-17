from flask import Blueprint, render_template, request, redirect, url_for, flash
from concurrent.futures import ThreadPoolExecutor

from ..apis.dca.anexos.dca_anexo_i_hi import(
    get_dca_i_hi, 
    d2_1_vpa_fundeb_principal, 
    d2_2_vpd_fundeb_principal
) 
from ..apis.dca.anexos.dca_anexo_i_c import(
    get_dca_i_c, 
    d2_3_deducoes_fundeb, 
    d2_4_receitas_fundeb,
    d2_10_receitas_outros_entes
)
from ..apis.dca.anexos.dca_anexo_i_d import (
    get_dca_i_d, 
    d2_5_desp_patronal_empenhada, 
    d2_6_desp_pessoal_empenhada, 
    d2_7_desp_custeio_empenhada
)
from ..apis.dca.anexos.dca_anexo_i_e import (
    get_dca_i_e, 
    d2_8_desp_por_funcao
)

dimensionii_bp = Blueprint('dimensionii_bp', __name__)
@dimensionii_bp.route('/dimensionii', methods=['GET'])
def dimensionii():
    id_ente = request.args.get('id_ente')
    an_referencia = request.args.get('an_referencia')

    if not id_ente or not an_referencia:
        flash("Parâmetros 'id_ente' e 'an_referencia' são necessários.", "warning")
        return redirect(url_for('home_bp.home'))

    # Executa as chamadas de API em paralelo
    with ThreadPoolExecutor() as executor:
        future_api_hi = executor.submit(get_dca_i_hi, id_ente, an_referencia)
        future_api_ic = executor.submit(get_dca_i_c, id_ente, an_referencia)
        future_api_id = executor.submit(get_dca_i_d, id_ente, an_referencia)
        future_api_ie = executor.submit(get_dca_i_e, id_ente, an_referencia)

        ane_i_hi = future_api_hi.result()
        ane_ic = future_api_ic.result()
        ane_id = future_api_id.result()
        ane_ie = future_api_ie.result()

    # Processa os resultados de cada DataFrame separadamente
    results = {
        'd2_01': d2_1_vpa_fundeb_principal(ane_i_hi),
        'd2_02': d2_2_vpd_fundeb_principal(ane_i_hi),
        'd2_03': d2_3_deducoes_fundeb(ane_ic),
        'd2_04': d2_4_receitas_fundeb(ane_ic),
        'd2_05': d2_5_desp_patronal_empenhada(ane_id),
        'd2_06': d2_6_desp_pessoal_empenhada(ane_id),
        'd2_07':d2_7_desp_custeio_empenhada(ane_id),
        'd2_08': d2_8_desp_por_funcao(ane_ie),
        'd2_10': d2_10_receitas_outros_entes(ane_ic)
    }

    # Renderiza o template com os resultados
    return render_template('dimension_ii.html', **results)

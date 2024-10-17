from flask import Blueprint, render_template, request, redirect, url_for, flash
from concurrent.futures import ThreadPoolExecutor

from ..dimensao_II.dca.anexos.dca_anexo_i_hi import(
    get_dca_i_hi, 
    d2_1_vpa_fundeb_principal, 
    d2_2_vpd_fundeb_principal
) 
from ..dimensao_II.dca.anexos.dca_anexo_i_c import(
    get_dca_i_c, 
    d2_3_deducoes_fundeb, 
    d2_4_receitas_fundeb,
    d2_10_receitas_outros_entes
)
from ..dimensao_II.dca.anexos.dca_anexo_i_d import (
    get_dca_i_d, 
    d2_5_desp_patronal_empenhada, 
    d2_6_desp_pessoal_empenhada, 
    d2_7_desp_custeio_empenhada
)
from ..dimensao_II.dca.anexos.dca_anexo_i_e import (
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
        get_api_hi = executor.submit(get_dca_i_hi, id_ente, an_referencia)
        get_api_ic = executor.submit(get_dca_i_c, id_ente, an_referencia)
        get_api_id = executor.submit(get_dca_i_d, id_ente, an_referencia)
        get_api_ie = executor.submit(get_dca_i_e, id_ente, an_referencia)

        anexo_i_hi = get_api_hi.result()
        anexo_ic = get_api_ic.result()
        anexo_id = get_api_id.result()
        anexo_ie = get_api_ie.result()

    # Processa os resultados das validações conforme cada anexo
    results_d2 = {
        'd2_01': d2_1_vpa_fundeb_principal(anexo_i_hi),
        'd2_02': d2_2_vpd_fundeb_principal(anexo_i_hi),
        'd2_03': d2_3_deducoes_fundeb(anexo_ic),
        'd2_04': d2_4_receitas_fundeb(anexo_ic),
        'd2_05': d2_5_desp_patronal_empenhada(anexo_id),
        'd2_06': d2_6_desp_pessoal_empenhada(anexo_id),
        'd2_07': d2_7_desp_custeio_empenhada(anexo_id),
        'd2_08': d2_8_desp_por_funcao(anexo_ie),
        'd2_10': d2_10_receitas_outros_entes(anexo_ic),
    }

    # Renderiza o template com os resultados
    return render_template('dimension_ii.html', **results_d2)

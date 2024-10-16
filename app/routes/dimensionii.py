from flask import Blueprint, render_template, request, redirect, url_for, flash
from concurrent.futures import ThreadPoolExecutor
from ..apis.dca.d2_00004 import receitas_fundeb
from ..apis.dca.d2_00005 import desp_patronal_empenhada
from ..apis.dca.d2_00006 import desp_pessoal_empenhada
from ..apis.dca.d2_00007 import desp_custeio_empenhada
from ..apis.dca.d2_00008 import desp_por_funcao
from ..apis.dca.d2_00010 import receitas_outros_entes
from ..apis.dca.dca_anexo_i_hi import get_dca_i_hi, d2_1_vpa_fundeb_principal, d2_2_vpd_fundeb_principal
from ..apis.dca.dca_anexo_i_c import get_dca_i_c, d2_3_deducoes_fundeb

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
        future_hi = executor.submit(get_dca_i_hi, id_ente, an_referencia)
        future_c = executor.submit(get_dca_i_c, id_ente, an_referencia)

        ane_i_hi = future_hi.result()
        ane_i_c = future_c.result()

    # Processa os resultados de cada DataFrame separadamente
    results = {
        'd2_01': d2_1_vpa_fundeb_principal(ane_i_hi),
        'd2_02': d2_2_vpd_fundeb_principal(ane_i_hi),
        'd2_03': d2_3_deducoes_fundeb(ane_i_c),
        'd2_04': receitas_fundeb(id_ente, an_referencia),
        'd2_05': desp_patronal_empenhada(id_ente, an_referencia),
        'd2_06': desp_pessoal_empenhada(id_ente, an_referencia),
        'd2_07': desp_custeio_empenhada(id_ente, an_referencia),
        'd2_08': desp_por_funcao(id_ente, an_referencia),
        'd2_10': receitas_outros_entes(id_ente, an_referencia)
    }

    # Renderiza o template com os resultados
    return render_template('dimension_ii.html', **results)

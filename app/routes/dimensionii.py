from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..apis.dca.d2_00003 import deducoes_fundeb
from ..apis.dca.d2_00004 import receitas_fundeb
from ..apis.dca.d2_00005 import desp_patronal_empenhada
from ..apis.dca.d2_00006 import desp_pessoal_empenhada
from ..apis.dca.d2_00007 import desp_custeio_empenhada
from ..apis.dca.d2_00008 import desp_por_funcao
from ..apis.dca.d2_00010 import receitas_outros_entes
from ..apis.dca.dca_anexo_i_hi import get_dca_i_hi
from ..apis.dca.dca_anexo_i_hi import d2_1_vpa_fundeb_principal
from ..apis.dca.dca_anexo_i_hi import d2_2_vpd_fundeb_principal
from ..apis.dca.dca_anexo_i_hi import d2_3_deducoes_fundeb

dimensionii_bp = Blueprint('dimensionii_bp', __name__)

@dimensionii_bp.route('/dimensionii', methods=['GET'])
def dimensionii():
    id_ente = request.args.get('id_ente')
    an_referencia = request.args.get('an_referencia')

    if not id_ente or not an_referencia:
        flash("Parâmetros 'id_ente' e 'an_referencia' são necessários.", "warning")
        return redirect(url_for('home_bp.home'))

    # Chamada única à API para compartilhar os dados
    df = get_dca_i_hi(id_ente, an_referencia)

    if df.empty:
        flash("Informe: Exercício, UF e Cidade.", "warning")
        return redirect(url_for('home_bp.home'))

    # Chama as funções com o DataFrame compartilhado
    result_d2_01 = d2_1_vpa_fundeb_principal(df)  # Processa o DataFrame para VPA
    result_d2_02 = d2_2_vpd_fundeb_principal(df)  # Processa o DataFrame para VPD
    result_d2_03 = d2_3_deducoes_fundeb(df)
    result_d2_04 = receitas_fundeb(id_ente, an_referencia)
    result_d2_05 = desp_patronal_empenhada(id_ente, an_referencia)
    result_d2_06 = desp_pessoal_empenhada(id_ente, an_referencia)
    result_d2_07 = desp_custeio_empenhada(id_ente, an_referencia)
    result_d2_08 = desp_por_funcao(id_ente, an_referencia)
    result_d2_10 = receitas_outros_entes(id_ente, an_referencia)

    # Renderiza o template com os resultados
    return render_template('dimension_ii.html', d2_01=result_d2_01,
                                              d2_02=result_d2_02,
                                              d2_03=result_d2_03,
                                              d2_04=result_d2_04,
                                              d2_05=result_d2_05,
                                              d2_06=result_d2_06,
                                              d2_07=result_d2_07,
                                              d2_08=result_d2_08,
                                              d2_10=result_d2_10)

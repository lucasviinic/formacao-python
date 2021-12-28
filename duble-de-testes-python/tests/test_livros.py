from unittest.mock import patch
from colecao.livros import consultar_livros


def test_consultar_livros_retorna_resultado_formato_string():

    resultado = consultar_livros("Agatha Christie")
    assert type(resultado) == str

def test_consultar_livros_chama_preparar_dados_para_requisicao_uma_vez_e_com_os_mesmos_parametros_de_consultar_livros():
    with patch("colecao.livros.preparar_dados_para_requisicao") as duble:
        consultar_livros("Agatha Christie")
        duble.assert_called_once_with("Agatha Christie")

def test_consultar_livros_chama_a_funcao_obter_url_usando_como_parametro_o_retorno_de_preparar_dados_para_requisicao():
    with patch("colecao.livros.preparar_dados_para_requisicao") as duble_preparar:
        dados = {"autor": "Agatha Christie"}
        duble_preparar.return_value = dados
        with patch("colecao.livros.obter_url") as duble_obter_url:
            consultar_livros("Agatha Christie")
            duble_obter_url.assert_called_once_with("https://buscador", dados)



























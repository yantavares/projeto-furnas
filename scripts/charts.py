import plotly.graph_objects as go
import os
from IPython.display import display
from ipywidgets import Button


def grafico_interativo_linha(x, y, nome_eixo_x, nome_eixo_y, titulo="", nome_legenda=""):
    """
    Cria um gráfico de linha interativo utilizando Plotly.

    :param x: Vetor com os valores do eixo x.
    :param y: Vetor com os valores do eixo y.
    :param nome_eixo_x: Nome para ser exibido no eixo x do gráfico.
    :param nome_eixo_y: Nome para ser exibido no eixo y do gráfico.
    :param titulo: Título opcional do gráfico.
    :param nome_legenda: Nome opcional para a legenda da linha.
    :return: Objeto de figura Plotly contendo o gráfico de linha.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=nome_legenda))

    fig.update_layout(
        title=titulo,
        xaxis_title=nome_eixo_x,
        yaxis_title=nome_eixo_y,
        legend_title="Legenda"
    )

    fig.show(config={'displaylogo': False})

    return fig


def grafico_interativo_multiplas_linhas(x, y, nome_eixo_x, nome_eixo_y, titulo="", nome_legenda=[]):
    """
    Cria um gráfico interativo com múltiplas linhas utilizando Plotly.

    :param x: Vetor com os valores do eixo x, comum a todas as linhas.
    :param y: Matriz com os valores do eixo y para cada linha.
    :param nome_eixo_x: Nome para ser exibido no eixo x do gráfico.
    :param nome_eixo_y: Nome para ser exibido no eixo y do gráfico.
    :param titulo: Título opcional do gráfico.
    :param nome_legenda: Lista com os nomes das legendas para cada linha.
    :return: Objeto de figura Plotly contendo o gráfico com múltiplas linhas.
    """
    fig = go.Figure()
    for i in range(len(y)):
        legenda = nome_legenda[i] if i < len(nome_legenda) else ""
        fig.add_trace(go.Scatter(x=x, y=y[i], mode='lines', name=legenda))

    fig.update_layout(
        title=titulo,
        xaxis_title=nome_eixo_x,
        yaxis_title=nome_eixo_y,
        legend_title=""
    )

    fig.show(config={'displaylogo': False})

    return fig


def exportar_para_pdf(fig, nome_arquivo="grafico.pdf"):
    """
    Exporta um gráfico para um arquivo PDF.

    :param fig: Objeto de figura Plotly que será exportado.
    :param nome_arquivo: Nome do arquivo PDF para salvar o gráfico.
    """
    if not os.path.exists("imagens"):
        os.mkdir("imagens")
    fig.write_image(f"imagens/{nome_arquivo}")


def _criar_handler_botao(fig, nome_arquivo):
    """
    Cria um handler para um evento de clique de botão que exporta um gráfico para PDF.

    :param fig: Objeto de figura Plotly que será exportado.
    :param nome_arquivo: Nome do arquivo PDF para salvar o gráfico.
    :return: Função que será chamada quando o botão for clicado.
    """
    def ao_clicar_no_botao(_):
        exportar_para_pdf(fig, nome_arquivo)
        try:
            pass
            # files.download(f'imagens/{nome_arquivo}')
        except Exception as e:
            print(f"Não foi possível baixar o arquivo: {e}")
    return ao_clicar_no_botao


def botao_exportar_pdf(fig, nome_arquivo="grafico.pdf"):
    """
    Cria e exibe um botão no Google Colab para exportar um gráfico como PDF.

    :param fig: Objeto de figura Plotly que será exportado.
    :param nome_arquivo: Nome do arquivo PDF para salvar o gráfico.
    """
    botao = Button(description="Exportar como PDF")
    handler_botao = _criar_handler_botao(fig, nome_arquivo)
    botao.on_click(handler_botao)
    display(botao)

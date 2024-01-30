import os
from IPython.display import display
from ipywidgets import Button
import plotly.graph_objects as go


class GeradorGraficoFurnas:
    def __init__(self, nome_arquivo="grafico"):
        self.nome_arquivo = nome_arquivo

    def grafico_interativo_linha(self, x, y, nome_eixo_x, nome_eixo_y, titulo="", nome_legenda=""):
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
        self.fig = fig

    def grafico_interativo_multiplas_linhas(self, x, y, nome_eixo_x, nome_eixo_y, titulo="", nome_legenda=[]):
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
        self.fig = fig

    def exportar_para_pdf(self):
        """
        Exporta um gráfico para um arquivo PDF.

        :param fig: Objeto de figura Plotly que será exportado.
        :param nome_arquivo: Nome do arquivo PDF para salvar o gráfico.
        """
        if not os.path.exists("imagens"):
            os.mkdir("imagens")
        self.fig.write_image(f"imagens/{self.nome_arquivo}")

    def botao_exportar_pdf(self):
        """
        Cria e exibe um botão no Jupyter para exportar um gráfico como PDF.

        :param fig: Objeto de figura Plotly que será exportado.
        :param nome_arquivo: Nome do arquivo PDF para salvar o gráfico.
        """

        botao = Button(description="Exportar para PDF")
        botao.on_click(self._criar_handler_botao(self.fig, self.nome_arquivo))
        display(botao)

    def _criar_handler_botao(self, fig, nome_arquivo):
        """
        Cria um handler para um evento de clique de botão que exporta um gráfico para PDF.

        :param fig: Objeto de figura Plotly que será exportado.
        :param nome_arquivo: Nome do arquivo PDF para salvar o gráfico.
        :return: Função que será chamada quando o botão for clicado.
        """
        def ao_clicar_no_botao(_):
            # Verifica se o diretório 'imagens/' existe, se não, cria
            if not os.path.exists('imagens'):
                os.makedirs('imagens')

            try:
                # Caminho completo do arquivo
                arquivo_completo = f'imagens/{nome_arquivo}.pdf'

                # Exporta a figura como PDF
                fig.write_image(arquivo_completo)

                # Inicia o download do arquivo
                self.download_file(arquivo_completo)
            except Exception as e:
                print(f"Não foi possível baixar o arquivo: {e}")

        return ao_clicar_no_botao

    def download_file(self, file_path):
        """
        Inicia o download de um arquivo no Jupyter Notebook.

        :param file_path: Caminho do arquivo a ser baixado.
        """
        from IPython.display import FileLink
        display(FileLink(file_path))


if __name__ == "__main__":
    # Exemplo de uso da classe
    gerador = GeradorGraficoFurnas("meu_grafico")
    x = [1, 2, 3, 4]
    y = [10, 11, 12, 13]
    gerador.grafico_interativo_linha(
        x, y, "Eixo X", "Eixo Y", "Título do Gráfico", "Legenda da Linha")
    gerador.botao_exportar_pdf()

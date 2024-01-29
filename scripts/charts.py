import os
from IPython.display import display
from ipywidgets import Button
import plotly.graph_objects as go


class GeradorGrafico:
    def __init__(self, nome_arquivo="grafico.pdf"):
        self.nome_arquivo = nome_arquivo

    def grafico_interativo_linha(self, x, y, nome_eixo_x, nome_eixo_y, titulo="", nome_legenda=""):
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
        if not os.path.exists("imagens"):
            os.mkdir("imagens")
        self.fig.write_image(f"imagens/{self.nome_arquivo}")

    def botao_exportar_pdf(self):
        botao = Button(description="Exportar como PDF")
        botao.on_click(self._ao_clicar_no_botao)
        display(botao)

    def _ao_clicar_no_botao(self, _):
        try:
            self.exportar_para_pdf()
            # files.download(f'imagens/{self.nome_arquivo}')
        except Exception as e:
            print(f"Não foi possível baixar o arquivo: {e}")


if __name__ == "__main__":
    # Exemplo de uso da classe
    gerador = GeradorGrafico("meu_grafico.pdf")
    x = [1, 2, 3, 4]
    y = [10, 11, 12, 13]
    gerador.grafico_interativo_linha(
        x, y, "Eixo X", "Eixo Y", "Título do Gráfico", "Legenda da Linha")
    gerador.botao_exportar_pdf()

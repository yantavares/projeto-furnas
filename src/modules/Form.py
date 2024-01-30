from IPython.display import display, clear_output
from ipywidgets import Button, Dropdown, FloatText, VBox, HBox, Layout


class FormularioFurnas:
    def __init__(self):
        # Inicializando os atributos
        self.dropdown = Dropdown(
            options=['Usar Dados Padrão', 'Usar Dados Personalizados'],
            description='Escolha:',
            disabled=False,
        )
        self.dropdown.observe(self.manipulador_evento_dropdown, names='value')

        self.potencia_termo = 100
        self.custo_capital_termo = 100
        self.custo_oem = 100
        self.taxa_de_juros = 100
        self.tempo_pagar_divida = 100
        self.eficiencia_aeroGT = 100
        self.eficiencia_steam = 100
        self.eficiencia_NG = 100
        self.energia_combustivel = 100
        self.preco_combustivel = 100
        self.custo_ciclo_aeroGT_cold = 100
        self.custo_ciclo_steam_cold = 100
        self.custo_ciclo_NG_cold = 100
        self.custo_ciclo_aeroGT_warm = 100
        self.custo_ciclo_steam_warm = 100
        self.custo_ciclo_NG_warm = 100
        self.custo_ciclo_aeroGT_hot = 100
        self.custo_ciclo_steam_hot = 100
        self.custo_ciclo_NG_hot = 100
        self.limite_ciclo_aeroGT_cold = 100
        self.limite_ciclo_steam_cold = 100
        self.limite_ciclo_NG_cold = 100
        self.limite_ciclo_aeroGT_warm = 100
        self.limite_ciclo_steam_warm = 100
        self.limite_ciclo_NG_warm = 100
        self.limite_ciclo_aeroGT_hot = 100
        self.limite_ciclo_steam_hot = 100
        self.limite_ciclo_NG_hot = 100

    def exibir_formulario(self):
        # Exibir dropdown inicial
        display(self.dropdown)

    def manipulador_evento_dropdown(self, change):
        clear_output(wait=True)
        display(self.dropdown)
        if change.new == 'Usar Dados Personalizados':
            self.exibir_formulario_dados_personalizados()

    def display_form(self, widgets):
        rows = []
        dict_iterator = iter(widgets.items())

        while True:
            try:
                element1 = next(dict_iterator)[1]
                element2 = next(dict_iterator)[1]
                rows.append([element1, element2])
            except StopIteration:
                try:
                    element1 = next(dict_iterator)[1]
                    rows.append([element1])
                except StopIteration:
                    break

        rows.append([self.botao_enviar])
        form = VBox([HBox([element for element in row]) for row in rows])
        display(form)

    def exibir_formulario_dados_personalizados(self):
        # Definição de estilo para os widgets
        self.widget_style = {'description_width': '230px'}
        self.widget_layout = Layout(width='auto', margin='5px auto')

        def criar_widget(description, value, disabled=False, style=self.widget_style, layout=self.widget_layout):
            return FloatText(description=description,
                             value=value,
                             disabled=disabled,
                             style=style,
                             layout=layout)

        self.elementos_para_exibir = {
            "potencia_termo_input": criar_widget('Potência Termelétrica (W): ', 100),
            "custo_capital_termo_input": criar_widget('Custo de Capital Termelétrico ($/W): ', 100),
            "custo_oem_input": criar_widget('Custo de O&M ($/W): ', 100),
            "taxa_de_juros_input": criar_widget('Taxa de Juros (%): ', 100),
            "tempo_pagar_divida_input": criar_widget('Tempo para Pagar a Dívida (anos): ', 100),
            "eficiencia_aeroGT_input": criar_widget('Eficiência AeroGT (%): ', 100),
            "eficiencia_steam_input": criar_widget('Eficiência Steam (%): ', 100),
            "eficiencia_NG_input": criar_widget('Eficiência NG (%): ', 100),
            "energia_combustivel_input": criar_widget('Energia do Combustível (MJ/kg): ', 100),
            "preco_combustivel_input": criar_widget('Preço do Combustível ($/kg): ', 100),
            "custo_ciclo_aeroGT_cold_input": criar_widget('Custo do Ciclo AeroGT ($/W): ', 100),
            "custo_ciclo_steam_cold_input": criar_widget('Custo do Ciclo Steam ($/W): ', 100),
            "custo_ciclo_NG_cold_input": criar_widget('Custo do Ciclo NG ($/W): ', 100),
            "custo_ciclo_aeroGT_warm_input": criar_widget('Custo do Ciclo AeroGT ($/W): ', 100),
            "custo_ciclo_steam_warm_input": criar_widget('Custo do Ciclo Steam ($/W): ', 100),
            "custo_ciclo_NG_warm_input": criar_widget('Custo do Ciclo NG ($/W): ', 100),
            "custo_ciclo_aeroGT_hot_input": criar_widget('Custo do Ciclo AeroGT ($/W): ', 100),
            "custo_ciclo_steam_hot_input": criar_widget('Custo do Ciclo Steam ($/W): ', 100),
            "custo_ciclo_NG_hot_input": criar_widget('Custo do Ciclo NG ($/W): ', 100),
            "limite_ciclo_aeroGT_cold_input": criar_widget('Limite do Ciclo AeroGT (s): ', 100),
            "limite_ciclo_steam_cold_input": criar_widget('Limite do Ciclo Steam (s): ', 100),
            "limite_ciclo_NG_cold_input": criar_widget('Limite do Ciclo NG (s): ', 100),
            "limite_ciclo_aeroGT_warm_input": criar_widget('Limite do Ciclo AeroGT (s): ', 100),
            "limite_ciclo_steam_warm_input": criar_widget('Limite do Ciclo Steam (s): ', 100),
            "limite_ciclo_NG_warm_input": criar_widget('Limite do Ciclo NG (s): ', 100),
            "limite_ciclo_aeroGT_hot_input": criar_widget('Limite do Ciclo AeroGT (s): ', 100),
            "limite_ciclo_steam_hot_input": criar_widget('Limite do Ciclo Steam (s): ', 100),
            "limite_ciclo_NG_hot_input": criar_widget('Limite do Ciclo NG (s): ', 100),
        }

        # Botão para enviar os dados
        self.botao_enviar = Button(description='Enviar', layout=Layout(
            width='auto', margin='0 auto'))
        self.botao_enviar.on_click(self.manipulador_evento_botao_enviar)

        # Exibir o formulário
        self.display_form(self.elementos_para_exibir)

    def manipulador_evento_botao_enviar(self, _):
        try:
            self.potencia_termo = self.elementos_para_exibir["potencia_termo_input"].value
            self.custo_capital_termo = self.elementos_para_exibir["custo_capital_termo_input"].value
            self.custo_oem = self.elementos_para_exibir["custo_oem_input"].value
            self.taxa_de_juros = self.elementos_para_exibir["taxa_de_juros_input"].value
            self.tempo_pagar_divida = self.elementos_para_exibir["tempo_pagar_divida_input"].value
            self.eficiencia_aeroGT = self.elementos_para_exibir["eficiencia_aeroGT_input"].value
            self.eficiencia_steam = self.elementos_para_exibir["eficiencia_steam_input"].value
            self.eficiencia_NG = self.elementos_para_exibir["eficiencia_NG_input"].value
            self.energia_combustivel = self.elementos_para_exibir["energia_combustivel_input"].value
            self.preco_combustivel = self.elementos_para_exibir["preco_combustivel_input"].value
            self.custo_ciclo_aeroGT_cold = self.elementos_para_exibir[
                "custo_ciclo_aeroGT_cold_input"].value
            self.custo_ciclo_steam_cold = self.elementos_para_exibir[
                "custo_ciclo_steam_cold_input"].value
            self.custo_ciclo_NG_cold = self.elementos_para_exibir["custo_ciclo_NG_cold_input"].value
            self.custo_ciclo_aeroGT_warm = self.elementos_para_exibir[
                "custo_ciclo_aeroGT_warm_input"].value
            self.custo_ciclo_steam_warm = self.elementos_para_exibir[
                "custo_ciclo_steam_warm_input"].value
            self.custo_ciclo_NG_warm = self.elementos_para_exibir["custo_ciclo_NG_warm_input"].value
            self.custo_ciclo_aeroGT_hot = self.elementos_para_exibir[
                "custo_ciclo_aeroGT_hot_input"].value
            self.custo_ciclo_steam_hot = self.elementos_para_exibir[
                "custo_ciclo_steam_hot_input"].value
            self.custo_ciclo_NG_hot = self.elementos_para_exibir["custo_ciclo_NG_hot_input"].value
            self.limite_ciclo_aeroGT_cold = self.elementos_para_exibir[
                "limite_ciclo_aeroGT_cold_input"].value
            self.limite_ciclo_steam_cold = self.elementos_para_exibir[
                "limite_ciclo_steam_cold_input"].value
            self.limite_ciclo_NG_cold = self.elementos_para_exibir["limite_ciclo_NG_cold_input"].value
            self.limite_ciclo_aeroGT_warm = self.elementos_para_exibir[
                "limite_ciclo_aeroGT_warm_input"].value
            self.limite_ciclo_steam_warm = self.elementos_para_exibir[
                "limite_ciclo_steam_warm_input"].value
            self.limite_ciclo_NG_warm = self.elementos_para_exibir["limite_ciclo_NG_warm_input"].value
            self.limite_ciclo_aeroGT_hot = self.elementos_para_exibir[
                "limite_ciclo_aeroGT_hot_input"].value
            self.limite_ciclo_steam_hot = self.elementos_para_exibir[
                "limite_ciclo_steam_hot_input"].value
            self.limite_ciclo_NG_hot = self.elementos_para_exibir["limite_ciclo_NG_hot_input"].value

            print("Dados enviados com sucesso!")

        except Exception as e:
            print("Não foi possível ler os dados inseridos")
            print(e)

    def recuperar_valores(self):
        return self.potencia_termo, self.custo_oem, self.taxa_de_juros, \
            self.tempo_pagar_divida, self.eficiencia_aeroGT, self.eficiencia_steam, self.eficiencia_NG, \
            self.energia_combustivel, self.preco_combustivel, self.custo_ciclo_aeroGT_cold, \
            self.custo_ciclo_steam_cold, self.custo_ciclo_NG_cold, self.custo_ciclo_aeroGT_warm, \
            self.custo_ciclo_steam_warm, self.custo_ciclo_NG_warm, self.custo_ciclo_aeroGT_hot, \
            self.custo_ciclo_steam_hot, self.custo_ciclo_NG_hot, self.limite_ciclo_aeroGT_cold, \
            self.limite_ciclo_steam_cold, self.limite_ciclo_NG_cold, self.limite_ciclo_aeroGT_warm, \
            self.limite_ciclo_steam_warm, self.limite_ciclo_NG_warm, self.limite_ciclo_aeroGT_hot, \
            self.limite_ciclo_steam_hot, self.limite_ciclo_NG_hot


if __name__ == "__main__":
    # Para usar a classe
    form = FormularioFurnas()
    form.exibir_formulario()

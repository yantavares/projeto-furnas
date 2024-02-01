from IPython.display import display, clear_output
from ipywidgets import Button, Dropdown, FloatText, VBox, HBox, Layout
from types import SimpleNamespace


class FormularioFurnas:
    def __init__(self):
        # Inicializando os atributos
        self.dropdown = Dropdown(
            options=['Usar Dados Padrão', 'Usar Dados Personalizados'],
            description='Escolha:',
            disabled=False,
        )
        self.dropdown.observe(self.manipulador_evento_dropdown, names='value')

        # Multiplicador de inflação corrigido
        self.multiplicador_inflacao = 1.33

        # Conversão de BTU/ft^3 para MJ/m^3
        self.pe_cubico_para_m = 28.3

        # Preço do pé cúbico de gás natural em USD
        self.preco_NG = 7.66

        # Taxa de juros anual
        self.taxa_de_juros = 0.05

        # Tempo para pagar o valor da turbina em meses (20 anos x 12 meses)
        self.tempo_pagar_turbina = 20 * 12

        # CCGT - Ciclo Combinado de Gás e Turbina a Vapor
        self.potencia_CCGT = 430  # em MW
        self.custo_capital_CCGT = 1084  # $/kW
        self.custo_OM_CCGT = 14.1 * 1000  # US$/MW por ano
        self.eficiencia_CCGT = 0.623
        self.tempo_inicio_quente_CCGT = 105  # Minutos (80 + 25)
        self.tempo_inicio_morno_CCGT = 105  # Minutos (80 + 25)
        self.tempo_inicio_frio_CCGT = 105  # Minutos (80 + 25)
        self.custo_inicio_quente_CCGT = 35  # $/MW
        self.custo_inicio_morno_CCGT = 55  # $/MW
        self.custo_inicio_frio_CCGT = 79  # $/MW

        # Aero GT - Turbina a Gás Aeroderivativa
        self.potencia_Aero = 106  # MW (53*2)
        self.custo_total_Aero = 1175  # $/kW
        self.custo_OM_Aero = 16.3 * 1000  # US$/MW por ano
        self.eficiencia_Aero = 0.408
        self.tempo_inicio_quente_Aero = 2  # Minutos
        self.tempo_inicio_morno_Aero = 4  # Minutos
        self.tempo_inicio_frio_Aero = 5  # Minutos
        self.custo_inicio_quente_Aero = 19  # $/MW
        self.custo_inicio_morno_Aero = 24  # $/MW
        self.custo_inicio_frio_Aero = 32  # $/MW

        # Turbina a Gás de Grande Porte GE 7F.05
        self.potencia_Heavy_Duty_GE_7F_05 = 239  # MW
        self.custo_total_Heavy_Duty_GE_7F_05 = 713  # $/kW
        self.custo_OM_Heavy_Duty_GE_7F_05_espera = 7 * 1000  # US$/MW por ano
        self.eficiencia_Heavy_Duty = 0.385
        self.tempo_inicio_quente_Heavy_Duty = 20  # Minutos
        self.tempo_inicio_morno_Heavy_Duty = 25  # Minutos
        self.tempo_inicio_frio_Heavy_Duty = 25  # Minutos
        self.custo_inicio_quente_Heavy_Duty = 36  # $/MW
        self.custo_inicio_morno_Heavy_Duty = 58  # $/MW
        self.custo_inicio_frio_Heavy_Duty = 75  # $/MW

        # Calcula o custo de combustível para uma turbina CCGT
        self.custo_combustivel_CCGT = self.encontrar_volume_combustivel_turbina(
            self.potencia_CCGT, self.eficiencia_CCGT, self.pe_cubico_para_m) * self.preco_NG * self.pe_cubico_para_m

    def encontrar_volume_combustivel_turbina(self, potencia_Turbina, eficiencia, energia_por_volume):
        Volume = potencia_Turbina / (eficiencia * energia_por_volume)
        return Volume
        # Valor_calorifico_todo_combustivel = Potencia_Turbina / (eficiencia * taxa_consumo_combustivel)
        # Quantidade_combustivel = Valor_calorifico_todo_combustivel / (valor_calorifico_combustivel_especifico)

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
        self.widget_style = {'description_width': '300px'}
        self.widget_layout = Layout(width='auto', margin='5px auto')

        def criar_widget(description, value, disabled=False, style=self.widget_style, layout=self.widget_layout):
            return FloatText(description=description,
                             title=description,
                             label=description,
                             value=value,
                             disabled=disabled,
                             style=style,
                             layout=layout)

        self.elementos_para_exibir = {
            "multiplicador_inflacao": criar_widget('Multiplicador de Inflação: ', 1.33),
            "pe_cubico_para_m": criar_widget('Conversão de BTU/ft^3 para MJ/m^3: ', 28.3),
            "preco_NG": criar_widget('Preço do Pé Cúbico de Gás Natural (USD): ', 7.66),
            "taxa_de_juros": criar_widget('Taxa de Juros Anual: ', 0.05),
            "tempo_pagar_turbina": criar_widget('Tempo para Pagar a Turbina (meses): ', 20 * 12),
            "potencia_CCGT": criar_widget('Potência CCGT (MW): ', 430),
            "custo_capital_CCGT": criar_widget('Custo Capital CCGT ($/kW): ', 1084),
            "custo_OM_CCGT": criar_widget('Custo O&M CCGT (US$/MW por ano): ', 14.1 * 1000),
            "eficiencia_CCGT": criar_widget('Eficiência CCGT: ', 0.623),
            "tempo_inicio_quente_CCGT": criar_widget('Tempo de Início Quente CCGT (Minutos): ', 105),
            "tempo_inicio_morno_CCGT": criar_widget('Tempo de Início Morno CCGT (Minutos): ', 105),
            "tempo_inicio_frio_CCGT": criar_widget('Tempo de Início Frio CCGT (Minutos): ', 105),
            "custo_inicio_quente_CCGT": criar_widget('Custo de Início Quente CCGT ($/MW): ', 35),
            "custo_inicio_morno_CCGT": criar_widget('Custo de Início Morno CCGT ($/MW): ', 55),
            "custo_inicio_frio_CCGT": criar_widget('Custo de Início Frio CCGT ($/MW): ', 79),
            "potencia_Aero": criar_widget('Potência Aero GT (MW): ', 106),
            "custo_total_Aero": criar_widget('Custo Total Aero GT ($/kW): ', 1175),
            "custo_OM_Aero": criar_widget('Custo O&M Aero GT (US$/MW por ano): ', 16.3 * 1000),
            "eficiencia_Aero": criar_widget('Eficiência Aero GT: ', 0.408),
            "tempo_inicio_quente_Aero": criar_widget('Tempo de Início Quente Aero GT (Minutos): ', 2),
            "tempo_inicio_morno_Aero": criar_widget('Tempo de Início Morno Aero GT (Minutos): ', 4),
            "tempo_inicio_frio_Aero": criar_widget('Tempo de Início Frio Aero GT (Minutos): ', 5),
            "custo_inicio_quente_Aero": criar_widget('Custo de Início Quente Aero GT ($/MW): ', 19),
            "custo_inicio_morno_Aero": criar_widget('Custo de Início Morno Aero GT ($/MW): ', 24),
            "custo_inicio_frio_Aero": criar_widget('Custo de Início Frio Aero GT ($/MW): ', 32),
            "potencia_Heavy_Duty_GE_7F_05": criar_widget('Potência Heavy Duty GE 7F.05 (MW): ', 239),
            "custo_total_Heavy_Duty_GE_7F_05": criar_widget('Custo Total Heavy Duty GE 7F.05 ($/kW): ', 713),
            "custo_OM_Heavy_Duty_GE_7F_05_espera": criar_widget('Custo O&M Heavy Duty GE 7F.05 Espera (US$/MW por ano): ', 7 * 1000),
            "eficiencia_Heavy_Duty": criar_widget('Eficiência Heavy Duty GE 7F.05: ', 0.385),
            "tempo_inicio_quente_Heavy_Duty": criar_widget('Tempo de Início Quente Heavy Duty GE 7F.05 (Minutos): ', 20),
            "tempo_inicio_morno_Heavy_Duty": criar_widget('Tempo de Início Morno Heavy Duty GE 7F.05 (Minutos): ', 25),
            "tempo_inicio_frio_Heavy_Duty": criar_widget('Tempo de Início Frio Heavy Duty GE 7F.05 (Minutos): ', 25),
            "custo_inicio_quente_Heavy_Duty": criar_widget('Custo de Início Quente Heavy Duty GE 7F.05 ($/MW): ', 36),
            "custo_inicio_morno_Heavy_Duty": criar_widget('Custo de Início Morno Heavy Duty GE 7F.05 ($/MW): ', 58),
            "custo_inicio_frio_Heavy_Duty": criar_widget('Custo de Início Frio Heavy Duty GE 7F.05 ($/MW): ', 75),

        }

        # Botão para enviar os dados
        self.botao_enviar = Button(description='Enviar', layout=Layout(
            width='auto', margin='0 auto'))
        self.botao_enviar.on_click(self.manipulador_evento_botao_enviar)

        # Exibir o formulário
        self.display_form(self.elementos_para_exibir)

    def manipulador_evento_botao_enviar(self, _):
        try:
            self.multiplicador_inflacao = self.elementos_para_exibir["multiplicador_inflacao"].value
            self.pe_cubico_para_m = self.elementos_para_exibir["pe_cubico_para_m"].value
            self.preco_NG = self.elementos_para_exibir["preco_NG"].value
            self.taxa_de_juros = self.elementos_para_exibir["taxa_de_juros"].value
            self.tempo_pagar_turbina = self.elementos_para_exibir["tempo_pagar_turbina"].value
            self.potencia_CCGT = self.elementos_para_exibir["potencia_CCGT"].value
            self.custo_capital_CCGT = self.elementos_para_exibir["custo_capital_CCGT"].value
            self.custo_OM_CCGT = self.elementos_para_exibir["custo_OM_CCGT"].value
            self.eficiencia_CCGT = self.elementos_para_exibir["eficiencia_CCGT"].value
            self.tempo_inicio_quente_CCGT = self.elementos_para_exibir[
                "tempo_inicio_quente_CCGT"].value
            self.tempo_inicio_morno_CCGT = self.elementos_para_exibir[
                "tempo_inicio_morno_CCGT"].value
            self.tempo_inicio_frio_CCGT = self.elementos_para_exibir["tempo_inicio_frio_CCGT"].value
            self.custo_inicio_quente_CCGT = self.elementos_para_exibir[
                "custo_inicio_quente_CCGT"].value
            self.custo_inicio_morno_CCGT = self.elementos_para_exibir[
                "custo_inicio_morno_CCGT"].value
            self.custo_inicio_frio_CCGT = self.elementos_para_exibir["custo_inicio_frio_CCGT"].value
            self.potencia_Aero = self.elementos_para_exibir["potencia_Aero"].value
            self.custo_total_Aero = self.elementos_para_exibir["custo_total_Aero"].value
            self.custo_OM_Aero = self.elementos_para_exibir["custo_OM_Aero"].value
            self.eficiencia_Aero = self.elementos_para_exibir["eficiencia_Aero"].value
            self.tempo_inicio_quente_Aero = self.elementos_para_exibir[
                "tempo_inicio_quente_Aero"].value
            self.tempo_inicio_morno_Aero = self.elementos_para_exibir[
                "tempo_inicio_morno_Aero"].value
            self.tempo_inicio_frio_Aero = self.elementos_para_exibir["tempo_inicio_frio_Aero"].value
            self.custo_inicio_quente_Aero = self.elementos_para_exibir[
                "custo_inicio_quente_Aero"].value
            self.custo_inicio_morno_Aero = self.elementos_para_exibir[
                "custo_inicio_morno_Aero"].value
            self.custo_inicio_frio_Aero = self.elementos_para_exibir["custo_inicio_frio_Aero"].value
            self.potencia_Heavy_Duty_GE_7F_05 = self.elementos_para_exibir[
                "potencia_Heavy_Duty_GE_7F_05"].value
            self.custo_total_Heavy_Duty_GE_7F_05 = self.elementos_para_exibir[
                "custo_total_Heavy_Duty_GE_7F_05"].value
            self.custo_OM_Heavy_Duty_GE_7F_05_espera = self.elementos_para_exibir[
                "custo_OM_Heavy_Duty_GE_7F_05_espera"].value
            self.eficiencia_Heavy_Duty = self.elementos_para_exibir["eficiencia_Heavy_Duty"].value
            self.tempo_inicio_quente_Heavy_Duty = self.elementos_para_exibir[
                "tempo_inicio_quente_Heavy_Duty"].value
            self.tempo_inicio_morno_Heavy_Duty = self.elementos_para_exibir[
                "tempo_inicio_morno_Heavy_Duty"].value
            self.tempo_inicio_frio_Heavy_Duty = self.elementos_para_exibir[
                "tempo_inicio_frio_Heavy_Duty"].value
            self.custo_inicio_quente_Heavy_Duty = self.elementos_para_exibir[
                "custo_inicio_quente_Heavy_Duty"].value
            self.custo_inicio_morno_Heavy_Duty = self.elementos_para_exibir[
                "custo_inicio_morno_Heavy_Duty"].value
            self.custo_inicio_frio_Heavy_Duty = self.elementos_para_exibir[
                "custo_inicio_frio_Heavy_Duty"].value

            self.custo_combustivel_CCGT = self.encontrar_volume_combustivel_turbina(
                self.potencia_CCGT, self.eficiencia_CCGT, self.pe_cubico_para_m) * self.preco_NG * self.pe_cubico_para_m

            print("Dados enviados com sucesso!")

        except Exception as e:
            print("Não foi possível ler os dados inseridos")
            print(e)

    def recuperar_valores(self):
        return SimpleNamespace(
            multiplicador_inflacao=self.multiplicador_inflacao,
            pe_cubico_para_m=self.pe_cubico_para_m,
            preco_NG=self.preco_NG,
            taxa_de_juros=self.taxa_de_juros,
            tempo_pagar_turbina=self.tempo_pagar_turbina,
            potencia_CCGT=self.potencia_CCGT,
            custo_capital_CCGT=self.custo_capital_CCGT,
            custo_OM_CCGT=self.custo_OM_CCGT,
            eficiencia_CCGT=self.eficiencia_CCGT,
            tempo_inicio_quente_CCGT=self.tempo_inicio_quente_CCGT,
            tempo_inicio_morno_CCGT=self.tempo_inicio_morno_CCGT,
            tempo_inicio_frio_CCGT=self.tempo_inicio_frio_CCGT,
            custo_inicio_quente_CCGT=self.custo_inicio_quente_CCGT,
            custo_inicio_morno_CCGT=self.custo_inicio_morno_CCGT,
            custo_inicio_frio_CCGT=self.custo_inicio_frio_CCGT,
            potencia_Aero=self.potencia_Aero,
            custo_total_Aero=self.custo_total_Aero,
            custo_OM_Aero=self.custo_OM_Aero,
            eficiencia_Aero=self.eficiencia_Aero,
            tempo_inicio_quente_Aero=self.tempo_inicio_quente_Aero,
            tempo_inicio_morno_Aero=self.tempo_inicio_morno_Aero,
            tempo_inicio_frio_Aero=self.tempo_inicio_frio_Aero,
            custo_inicio_quente_Aero=self.custo_inicio_quente_Aero,
            custo_inicio_morno_Aero=self.custo_inicio_morno_Aero,
            custo_inicio_frio_Aero=self.custo_inicio_frio_Aero,
            potencia_Heavy_Duty_GE_7F_05=self.potencia_Heavy_Duty_GE_7F_05,
            custo_total_Heavy_Duty_GE_7F_05=self.custo_total_Heavy_Duty_GE_7F_05,
            custo_OM_Heavy_Duty_GE_7F_05_espera=self.custo_OM_Heavy_Duty_GE_7F_05_espera,
            eficiencia_Heavy_Duty=self.eficiencia_Heavy_Duty,
            tempo_inicio_quente_Heavy_Duty=self.tempo_inicio_quente_Heavy_Duty,
            tempo_inicio_morno_Heavy_Duty=self.tempo_inicio_morno_Heavy_Duty,
            tempo_inicio_frio_Heavy_Duty=self.tempo_inicio_frio_Heavy_Duty,
            custo_inicio_quente_Heavy_Duty=self.custo_inicio_quente_Heavy_Duty,
            custo_inicio_morno_Heavy_Duty=self.custo_inicio_morno_Heavy_Duty,
            custo_inicio_frio_Heavy_Duty=self.custo_inicio_frio_Heavy_Duty,
            custo_combustivel_CCGT=self.custo_combustivel_CCGT
        )


if __name__ == "__main__":
    # Para usar a classe
    form = FormularioFurnas()
    form.exibir_formulario()

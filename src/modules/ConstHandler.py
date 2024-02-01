from types import SimpleNamespace
from ipywidgets import FloatText, Layout


def criar_widget(description, value, disabled=False, widget_style={'description_width': '300px'}, widget_layout=Layout(width='auto', margin='5px auto')):
    return FloatText(description=description,
                     title=description,
                     label=description,
                     value=value,
                     disabled=disabled,
                     style=widget_style,
                     layout=widget_layout)


class Constants:
    def __init__(self):

        self.values = SimpleNamespace()
        self.widget_constants = SimpleNamespace(
            multiplicador_inflacao=criar_widget(
                'Multiplicador de Inflação', 1.33),
            pe_cubico_para_m=criar_widget(
                'Conversão de BTU/ft^3 para MJ/m^3', 28.3),
            preco_NG=criar_widget(
                'Preço do Pé Cúbico de Gás Natural (USD)', 7.66),
            taxa_de_juros=criar_widget('Taxa de Juros Anual', 0.05),
            tempo_pagar_turbina=criar_widget(
                'Tempo para Pagar a Turbina (meses)', 20 * 12),
            potencia_CCGT=criar_widget('Potência CCGT (MW)', 430),
            custo_capital_CCGT=criar_widget(
                'Custo Capital CCGT ($/kW)', 1084),
            custo_OM_CCGT=criar_widget(
                'Custo O&M CCGT (US$/MW por ano)', 14.1 * 1000),
            eficiencia_CCGT=criar_widget('Eficiência CCGT', 0.623),
            tempo_inicio_quente_CCGT=criar_widget(
                'Tempo de Início Quente CCGT (Minutos)', 105),
            tempo_inicio_morno_CCGT=criar_widget(
                'Tempo de Início Morno CCGT (Minutos)', 105),
            tempo_inicio_frio_CCGT=criar_widget(
                'Tempo de Início Frio CCGT (Minutos)', 105),
            custo_inicio_quente_CCGT=criar_widget(
                'Custo de Início Quente CCGT ($/MW)', 35),
            custo_inicio_morno_CCGT=criar_widget(
                'Custo de Início Morno CCGT ($/MW)', 55),
            custo_inicio_frio_CCGT=criar_widget(
                'Custo de Início Frio CCGT ($/MW)', 79),
            potencia_Aero=criar_widget('Potência Aero GT (MW)', 106),
            custo_total_Aero=criar_widget(
                'Custo Total Aero GT ($/kW)', 1175),
            custo_OM_Aero=criar_widget(
                'Custo O&M Aero GT (US$/MW por ano)', 16.3 * 1000),
            eficiencia_Aero=criar_widget('Eficiência Aero GT', 0.408),
            tempo_inicio_quente_Aero=criar_widget(
                'Tempo de Início Quente Aero GT (Minutos)', 2),
            tempo_inicio_morno_Aero=criar_widget(
                'Tempo de Início Morno Aero GT (Minutos)', 4),
            tempo_inicio_frio_Aero=criar_widget(
                'Tempo de Início Frio Aero GT (Minutos)', 5),
            custo_inicio_quente_Aero=criar_widget(
                'Custo de Início Quente Aero GT ($/MW)', 19),
            custo_inicio_morno_Aero=criar_widget(
                'Custo de Início Morno Aero GT ($/MW)', 24),
            custo_inicio_frio_Aero=criar_widget(
                'Custo de Início Frio Aero GT ($/MW)', 32),
            potencia_Heavy_Duty_GE_7F_05=criar_widget(
                'Potência Heavy Duty GE 7F.05 (MW)', 239),
            custo_total_Heavy_Duty_GE_7F_05=criar_widget(
                'Custo Total Heavy Duty GE 7F.05 ($/kW)', 713),
            custo_OM_Heavy_Duty_GE_7F_05_espera=criar_widget(
                'Custo O&M Heavy Duty GE 7F.05 Espera (US$/MW por ano)', 7 * 1000),
            eficiencia_Heavy_Duty=criar_widget(
                'Eficiência Heavy Duty GE 7F.05', 0.385),
            tempo_inicio_quente_Heavy_Duty=criar_widget(
                'Tempo de Início Quente Heavy Duty GE 7F.05 (Minutos)', 20),
            tempo_inicio_morno_Heavy_Duty=criar_widget(
                'Tempo de Início Morno Heavy Duty GE 7F.05 (Minutos)', 25),
            tempo_inicio_frio_Heavy_Duty=criar_widget(
                'Tempo de Início Frio Heavy Duty GE 7F.05 (Minutos)', 25),
            custo_inicio_quente_Heavy_Duty=criar_widget(
                'Custo de Início Quente Heavy Duty GE 7F.05 ($/MW)', 36),
            custo_inicio_morno_Heavy_Duty=criar_widget(
                'Custo de Início Morno Heavy Duty GE 7F.05 ($/MW)', 58),
            custo_inicio_frio_Heavy_Duty=criar_widget(
                'Custo de Início Frio Heavy Duty GE 7F.05 ($/MW)', 75),
        )

    def get_widgets(self):
        return self.widget_constants

    def set_values(self):
        # Usar a compreensão de dicionário para construir um novo dicionário,
        # onde cada valor é alterado para (valor_anterior).value
        novo_dicionario = {chave: getattr(
            valor, 'value', valor) for chave, valor in vars(self.widget_constants).items()}

        # Criar um novo SimpleNamespace com o dicionário transformado
        novo_namespace = SimpleNamespace(**novo_dicionario)

        self.values = novo_namespace

    def get_values(self):
        return self.values

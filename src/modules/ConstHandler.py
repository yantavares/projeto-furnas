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


def calcular_combustivel(Turbine_Power, efficiency):
    Volume = Turbine_Power/efficiency
    return (Volume)


class Constants:
    """
    Fontes:
    - https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2020.pdf
    - https://www.ge.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/products/gas-turbines/7ha-fact-sheet-product-specifications.pdf
    - https://etn.global/wp-content/uploads/2018/09/Startup_time_reduction_for_Combined_Cycle_Power_Plants.pdf
    - https://www.nrel.gov/docs/fy12osti/55433.pdf
    """

    def __init__(self):

        self.values = SimpleNamespace()
        self.widget_constants = SimpleNamespace(
            # taxa de inflação em dólares corrigida em dólares https://www.bls.gov/data/inflation_calculator.htm
            inflation_multiplier_2012=criar_widget(
                'Multiplicador de Inflação', 1.35),
            inflation_multiplier_2019=criar_widget(
                'Multiplicador de Inflação', 1.19),
            # Transformação de BTU/ft^3 (BTU sobre pé cubico) para MJ/m^3 (Megajoule sobre metro cúbico)
            # Encontrado em: https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion-calculators.php
            cubic_ft_to_m=criar_widget(
                'Conversão de BTU/ft^3 para MJ/m^3', 28.3),
            # Considerando que o preço do pé cúbico do gás natural é 0,27051 USD
            # De acordo com: https://www.eia.gov/dnav/ng/hist/n3035us3A.htm
            NG_price=criar_widget(
                'Preço do Pé Cúbico de Gás Natural (USD)', 7.66),
            # Taxa de juros de 5% ao ano
            interest_rate=criar_widget('Taxa de Juros Anual', 0.05),
            # Tempo para pagar o valor da turbina em 20 anos de 12 meses
            time_to_pay_turbine=criar_widget(
                'Tempo para Pagar a Turbina (meses)', 20 * 12),

            # Para a CCGT
            CCGT_power=criar_widget('Potência CCGT (MW)', 430),
            CCGT_capital_cost=criar_widget('Custo Capital CCGT ($/kW)', 1084),
            CCGT_OM_cost=criar_widget(
                'Custo O&M CCGT (US$/MW por ano)', 14.1 * 1000),
            CCGT_efficiency=criar_widget('Eficiência CCGT', 0.623),
            CCGT_hot_start_time=criar_widget(
                'Tempo de Início Quente CCGT (Minutos)', 105),
            CCGT_warm_start_time=criar_widget(
                'Tempo de Início Morno CCGT (Minutos)', 105),
            CCGT_cold_start_time=criar_widget(
                'Tempo de Início Frio CCGT (Minutos)', 105),
            CCGT_hot_start_cost=criar_widget(
                'Custo de Início Quente CCGT ($/MW)', 35),
            CCGT_warm_start_cost=criar_widget(
                'Custo de Início Morno CCGT ($/MW)', 55),
            CCGT_cold_start_cost=criar_widget(
                'Custo de Início Frio CCGT ($/MW)', 79),

            # Para a Aero GT - modelo GE LM600: https://www.ge.com/gas-power/products/gas-turbines/lm6000
            Aero_power=criar_widget('Potência Aero GT (MW)', 106),
            Aero_total_cost=criar_widget('Custo Total Aero GT ($/kW)', 1175),
            Aero_OM_cost=criar_widget(
                'Custo O&M Aero GT (US$/MW por ano)', 16.3 * 1000),
            Aero_efficiency=criar_widget('Eficiência Aero GT', 0.408),
            Aero_hot_start_time=criar_widget(
                'Tempo de Início Quente Aero GT (Minutos)', 2),
            Aero_warm_start_time=criar_widget(
                'Tempo de Início Morno Aero GT (Minutos)', 4),
            Aero_cold_start_time=criar_widget(
                'Tempo de Início Frio Aero GT (Minutos)', 5),
            Aero_hot_start_cost=criar_widget(
                'Custo de Início Quente Aero GT ($/MW)', 19),
            Aero_warm_start_cost=criar_widget(
                'Custo de Início Morno Aero GT ($/MW)', 24),
            Aero_cold_start_cost=criar_widget(
                'Custo de Início Frio Aero GT ($/MW)', 32),

            # Para a Heavy Duty - modelo GE 7F.05: https://www.ge.com/gas-power/products/gas-turbines/7f
            Heavy_Duty_power=criar_widget(
                'Potência Heavy Duty GE 7F.05 (MW)', 239),
            Heavy_Duty_total_cost=criar_widget(
                'Custo Total Heavy Duty GE 7F.05 ($/kW)', 713),
            Heavy_Duty_OM_cost=criar_widget(
                'Custo O&M Heavy Duty GE 7F.05 Espera (US$/MW por ano)', 7 * 1000),
            Heavy_Duty_efficiency=criar_widget(
                'Eficiência Heavy Duty GE 7F.05', 0.385),
            Heavy_Duty_hot_start_time=criar_widget(
                'Tempo de Início Quente Heavy Duty GE 7F.05 (Minutos)', 20),
            Heavy_Duty_warm_start_time=criar_widget(
                'Tempo de Início Morno Heavy Duty GE 7F.05 (Minutos)', 25),
            Heavy_Duty_cold_start_time=criar_widget(
                'Tempo de Início Frio Heavy Duty GE 7F.05 (Minutos)', 25),
            Heavy_Duty_hot_start_cost=criar_widget(
                'Custo de Início Quente Heavy Duty GE 7F.05 ($/MW)', 36),
            Heavy_Duty_warm_start_cost=criar_widget(
                'Custo de Início Morno Heavy Duty GE 7F.05 ($/MW)', 58),
            Heavy_Duty_cold_start_cost=criar_widget(
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

        # Calcular o custo de combustível para a CCGT
        novo_namespace.CCGT_Fuel_cost = round(calcular_combustivel(
            novo_namespace.CCGT_power, novo_namespace.CCGT_efficiency) * novo_namespace.NG_price * novo_namespace.cubic_ft_to_m, 2)

        self.values = novo_namespace

    def get_values(self):
        return self.values


if __name__ == "__main__":
    c = Constants()
    c.set_values()
    print(c.get_values())

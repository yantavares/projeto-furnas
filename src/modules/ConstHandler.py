from types import SimpleNamespace
from ipywidgets import FloatText, Layout
if __name__ == "__main__":
    from validData import ValidData
else:
    from .validData import ValidData

VALID = ValidData.get_valid_data()


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


def map_simple_namespace(a, f):
    # Convert SimpleNamespace to dictionary
    a_dict = vars(a)
    # Apply function f to each value of the dictionary
    b_dict = {k: f(v) for k, v in a_dict.items()}
    # Convert the modified dictionary back to SimpleNamespace
    b = SimpleNamespace(**b_dict)
    return b


def convert_to_widget(a):
    # Convert SimpleNamespace to dictionary
    a_dict = vars(a)

    # Apply function f to each value of the dictionary
    try:
        b_dict = {k: criar_widget(VALID[k], v)
                  for k, v in a_dict.items()}

        b = SimpleNamespace(**b_dict)
        return b
    except:
        print("Valor inválido de variável. Verifique os dados inseridos!")
        return a


class Constants:
    """
    Fontes:
    - https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2020.pdf
    - https://www.ge.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/products/gas-turbines/7ha-fact-sheet-product-specifications.pdf
    - https://etn.global/wp-content/uploads/2018/09/Startup_time_reduction_for_Combined_Cycle_Power_Plants.pdf
    - https://www.nrel.gov/docs/fy12osti/55433.pdf
    """

    def __init__(self):

        self.values = SimpleNamespace(
            inflation_multiplier_2012=1.35,
            inflation_multiplier_2019=1.19,
            cubic_ft_to_m=28.3,
            NG_price=7.66,
            interest_rate=0.05,
            time_to_pay_turbine=20 * 12,
            CCGT_power=430,
            CCGT_capital_cost=1084,
            CCGT_OM_cost=14.1 * 1000,
            CCGT_efficiency=0.623,
            CCGT_hot_start_time=105,
            CCGT_warm_start_time=105,
            CCGT_cold_start_time=105,
            CCGT_hot_start_cost=35,
            CCGT_warm_start_cost=55,
            CCGT_cold_start_cost=79,
            Aero_power=106,
            Aero_total_cost=1175,
            Aero_OM_cost=16.3 * 1000,
            Aero_efficiency=0.408,
            Aero_hot_start_time=2,
            Aero_warm_start_time=4,
            Aero_cold_start_time=5,
            Aero_hot_start_cost=19,
            Aero_warm_start_cost=24,
            Aero_cold_start_cost=32,
            Heavy_Duty_power=239,
            Heavy_Duty_total_cost=713,
            Heavy_Duty_OM_cost=7 * 1000,
            Heavy_Duty_efficiency=0.385,
            Heavy_Duty_hot_start_time=20,
            Heavy_Duty_warm_start_time=25,
            Heavy_Duty_cold_start_time=25,
        )

        self.widget_constants = convert_to_widget(self.values)

    def get_widgets(self):
        return self.widget_constants

    def set_values(self):
        novo_namespace = map_simple_namespace(
            self.widget_constants, lambda x: x.value)

        self.values = novo_namespace

    def set_personalized_values(self, values):
        try:
            for key, _ in vars(values).items():
                if key not in VALID.keys():
                    raise ValueError("Chave inválida!", key)

            self.widget_constants = convert_to_widget(values)

        except Exception as e:
            raise ValueError(
                "Erro ao atualizar valores personalizados: ", e)

    def get_values(self):
        return self.values


if __name__ == "__main__":
    c = Constants()
    c.set_values()
    print(c.get_values())

from types import SimpleNamespace


class ValidData:
    VALID = {
        "inflation_multiplier_2012": "Multiplicador de inflação (2012)",
        "inflation_multiplier_2019": "Multiplicador de inflação (2019)",
        "cubic_ft_to_m": "Conversão de pés cúbicos para metros cúbicos",
        "NG_price": "Preço do gás natural",
        "interest_rate": "Taxa de juros",
        "time_to_pay_turbine": "Tempo para pagar a turbina (meses)",
        "CCGT_power": "Potência da CCGT (MW)",
        "CCGT_capital_cost": "Custo de capital da CCGT (US$/kW)",
        "CCGT_OM_cost": "Custo de manutenção da CCGT (US$/MW por ano)",
        "CCGT_efficiency": "Eficiência da CCGT",
        "CCGT_hot_start_time": "Tempo de partida quente da CCGT (min)",
        "CCGT_warm_start_time": "Tempo de partida morna da CCGT (min)",
        "CCGT_cold_start_time": "Tempo de partida fria da CCGT (min)",
        "CCGT_hot_start_cost": "Custo de partida quente da CCGT (US$/MW)",
        "CCGT_warm_start_cost": "Custo de partida morna da CCGT (US$/MW)",
        "CCGT_cold_start_cost": "Custo de partida fria da CCGT (US$/MW)",
        "Aero_power": "Potência da Aero GT (MW)",
        "Aero_total_cost": "Custo total da Aero GT (US$/kW)",
        "Aero_OM_cost": "Custo de manutenção da Aero GT (US$/MW por ano)",
        "Aero_efficiency": "Eficiência da Aero GT",
        "Aero_hot_start_time": "Tempo de partida quente da Aero GT (min)",
        "Aero_warm_start_time": "Tempo de partida morna da Aero GT (min)",
        "Aero_cold_start_time": "Tempo de partida fria da Aero GT (min)",
        "Aero_hot_start_cost": "Custo de partida quente da Aero GT (US$/MW)",
        "Aero_warm_start_cost": "Custo de partida morna da Aero GT (US$/MW)",
        "Aero_cold_start_cost": "Custo de partida fria da Aero GT (US$/MW)",
        "Heavy_Duty_power": "Potência da Heavy Duty (MW)",
        "Heavy_Duty_total_cost": "Custo total da Heavy Duty (US$/kW)",
        "Heavy_Duty_OM_cost": "Custo de manutenção da Heavy Duty (US$/MW por ano)",
        "Heavy_Duty_efficiency": "Eficiência da Heavy Duty",
        "Heavy_Duty_hot_start_time": "Tempo de partida quente da Heavy Duty (min)",
        "Heavy_Duty_warm_start_time": "Tempo de partida morna da Heavy Duty (min)",
        "Heavy_Duty_cold_start_time": "Tempo de partida fria da Heavy Duty (min)",
    }

    INITIAL_VALUES = SimpleNamespace(
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

    @staticmethod
    def is_valid(data):
        return data in ValidData.VALID

    @staticmethod
    def get_valid_data():
        return ValidData.VALID

    @staticmethod
    def get_valid_data_by_key(key):
        return ValidData.VALID[key]

    @staticmethod
    def get_valid_data_by_value(value):
        return list(ValidData.VALID.keys())[list(ValidData.VALID.values()).index(value)]

    @staticmethod
    def get_initial_values():
        return ValidData.INITIAL_VALUES

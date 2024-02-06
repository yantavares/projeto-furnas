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
        "CCGT_hot_start_time": "Tempo de partida quente da CCGT (minutos)",
        "CCGT_warm_start_time": "Tempo de partida morna da CCGT (minutos)",
        "CCGT_cold_start_time": "Tempo de partida fria da CCGT (minutos)",
        "CCGT_hot_start_cost": "Custo de partida quente da CCGT (US$/MW)",
        "CCGT_warm_start_cost": "Custo de partida morna da CCGT (US$/MW)",
        "CCGT_cold_start_cost": "Custo de partida fria da CCGT (US$/MW)",
        "Aero_power": "Potência da Aero GT (MW)",
        "Aero_total_cost": "Custo total da Aero GT (US$/kW)",
        "Aero_OM_cost": "Custo de manutenção da Aero GT (US$/MW por ano)",
        "Aero_efficiency": "Eficiência da Aero GT",
        "Aero_hot_start_time": "Tempo de partida quente da Aero GT (minutos)",
        "Aero_warm_start_time": "Tempo de partida morna da Aero GT (minutos)",
        "Aero_cold_start_time": "Tempo de partida fria da Aero GT (minutos)",
        "Aero_hot_start_cost": "Custo de partida quente da Aero GT (US$/MW)",
        "Aero_warm_start_cost": "Custo de partida morna da Aero GT (US$/MW)",
        "Aero_cold_start_cost": "Custo de partida fria da Aero GT (US$/MW)",
        "Heavy_Duty_power": "Potência da Heavy Duty (MW)",
        "Heavy_Duty_total_cost": "Custo total da Heavy Duty (US$/kW)",
        "Heavy_Duty_OM_cost": "Custo de manutenção da Heavy Duty (US$/MW por ano)",
        "Heavy_Duty_efficiency": "Eficiência da Heavy Duty",
        "Heavy_Duty_hot_start_time": "Tempo de partida quente da Heavy Duty (minutos)",
        "Heavy_Duty_warm_start_time": "Tempo de partida morna da Heavy Duty (minutos)",
        "Heavy_Duty_cold_start_time": "Tempo de partida fria da Heavy Duty (minutos)",
    }

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

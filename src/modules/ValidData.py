from types import SimpleNamespace


class ValidData:
    VALID = {
        "inflation_multiplier_2012": "Multiplicador de inflação (2012)",
        "inflation_multiplier_2019": "Multiplicador de inflação (2019)",
        "cubic_m_to_ft": "Conversão de metros cúbicos para pés cúbicos",
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
        "Heavy_Duty_OM_cost": "Custo de manutenção Heavy Duty (US$/MW por ano)",
        "Heavy_Duty_efficiency": "Eficiência da Heavy Duty",
        "Heavy_Duty_hot_start_time": "Tempo de partida quente da Heavy Duty (min)",
        "Heavy_Duty_warm_start_time": "Tempo de partida morna da Heavy Duty (min)",
        "Heavy_Duty_cold_start_time": "Tempo de partida fria da Heavy Duty (min)",
        "Heavy_Duty_hot_start_cost": "Custo de partida quente da Heavy Duty (US$/MW)",
        "Heavy_Duty_warm_start_cost": "Custo de partida morna da Heavy Duty (US$/MW)",
        "Heavy_Duty_cold_start_cost": "Custo de partida fria da Heavy Duty (US$/MW)",
    }

    # Definição de constantes que serão utilizadas como constantes no programa
    INITIAL_VALUES = SimpleNamespace(
        # taxa de inflação em dólares corrigida em dólares https://www.bls.gov/data/inflation_calculator.htm
        inflation_multiplier_2012=1.35,
        inflation_multiplier_2019=1.19,
        # Transformação de BTU/ft^3 (BTU sobre pé cubico) para MJ/m^3 (Megajoule sobre metro cúbico)
        # Encontrado em: https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion-calculators.php
        cubic_m_to_ft=35.3,
        # Considerando que o preço do pé cúbico do gás natural é 0,27051 USD
        # De acordo com: https://www.eia.gov/dnav/ng/hist/n3035us3A.htm
        NG_price=7.66,
        # Taxa de juros de 5% ao ano
        interest_rate=0.05,
        # Tempo para pagar o valor da turbina em 20 anos de 12 meses
        time_to_pay_turbine=20 * 12,
        # Para a CCGT - modelo GE 7HA.01 Combined Cycle 1x1: https://www.ge.com/gas-power/products/gas-turbines/7ha
        CCGT_power=430,  # MW
        CCGT_capital_cost=1084,  # $/kW
        CCGT_OM_cost=14.1 * 1000,  # US$/MW por ano
        CCGT_efficiency=0.623,  # 62.3%
        CCGT_hot_start_time=105,  # Minutos
        CCGT_warm_start_time=105,  # Minutos
        CCGT_cold_start_time=105,  # Minutos
        CCGT_hot_start_cost=35,  # $/MW
        CCGT_warm_start_cost=55,  # $/MW
        CCGT_cold_start_cost=79,  # $/MW
        # Para a Aero GT - modelo GE LM600: https://www.ge.com/gas-power/products/gas-turbines/lm6000
        Aero_power=106,  # MW
        Aero_total_cost=1175,  # $/kW
        Aero_OM_cost=16.3 * 1000,  # US$/MW por ano
        Aero_efficiency=0.408,  # 40.8%
        Aero_hot_start_time=2,  # Minutos
        Aero_warm_start_time=4,  # Minutos
        Aero_cold_start_time=5,  # Minutos
        Aero_hot_start_cost=19,  # $/MW
        Aero_warm_start_cost=24,  # $/MW
        Aero_cold_start_cost=32,  # $/MW
        # Para a Heavy Duty - modelo GE 7F.05: https://www.ge.com/gas-power/products/gas-turbines/7f
        Heavy_Duty_power=239,  # MW
        Heavy_Duty_total_cost=713,  # $/kW
        Heavy_Duty_OM_cost=7 * 1000,  # US$/MW por ano
        Heavy_Duty_efficiency=0.385,  # 38.5%
        Heavy_Duty_hot_start_time=20,  # Minutos
        Heavy_Duty_warm_start_time=25,  # Minutos
        Heavy_Duty_cold_start_time=25,  # Minutos
        Heavy_Duty_hot_start_cost=36,  # $/MW
        Heavy_Duty_warm_start_cost=58,  # $/MW
        Heavy_Duty_cold_start_cost=75,  # $/MW

        # Fontes:
        # - https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2020.pdf
        # - https://www.ge.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/products/gas-turbines/7ha-fact-sheet-product-specifications.pdf
        # - https://etn.global/wp-content/uploads/2018/09/Startup_time_reduction_for_Combined_Cycle_Power_Plants.pdf
        # - https://www.nrel.gov/docs/fy12osti/55433.pdf
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

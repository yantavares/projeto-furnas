from types import SimpleNamespace


class ValidData:
    header_positions = [0, 6, 16, 26]  # This means: After index x put header
    # To get that: (index in valid) - (how many were before)

    VALID = {
        "header0": "Geral",

        "inflation_multiplier_2012": "Multiplicador de inflação (2012)",
        "inflation_multiplier_2019": "Multiplicador de inflação (2019)",
        "cubic_m_to_ft": "Conversão de metros cúbicos para pés cúbicos",
        "interest_rate": "Taxa de juros",
        "NG_price": "Preço do gás natural",
        "time_to_pay_turbine": "Tempo para pagar a turbina (meses)",

        "header6": "CCGT",

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

        "header16": "AeroGT",

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

        "header26": "Heavy Duty",

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
        inflation_multiplier_2019=1.22,
        # Transformação de BTU/ft^3 (BTU sobre pé cubico) para MJ/m^3 (Megajoule sobre metro cúbico)
        # Encontrado em: https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion-calculators.php
        cubic_m_to_ft=35.3,
        # Taxa de juros de 5% ao ano
        interest_rate=0.05,
        # Considerando que o preço do pé cúbico do gás natural é 0,27051 USD
        # De acordo com: https://www.eia.gov/dnav/ng/hist/n3035us3A.htm
        NG_price=7.66,
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

    # This means: After index x put header
    header_positions_batteries = [0, 3, 6, 9, 12, 15, 18]
    VALID_BATTERIES = {
        "header0": "Bateria: Chumbo-Ácido",

        "lead_acid_kw": 1976,
        "lead_acid_kwh": 494.5,
        "lead_acid_lifespan": 3,

        "header3": "Bateria: Lítio-Íon",

        "li_ion_kw": 1946,
        "li_ion_kwh": 487,
        "li_ion_lifespan": 10,

        "header6": "Bateria: Sódio-Enxofre",

        "sodium_sulfur_kw": 3782,
        "sodium_sulfur_kwh": 946,
        "sodium_sulfur_lifespan": 13.5,

        "header9": "Bateria: Fluxo de oxidação",

        "redox_flow_kw": 3984,
        "redox_flow_kwh": 996.5,
        "redox_flow_lifespan": 15,

        "header12": "Bateria: Sódio-Metal",

        "sodium_metal_halide_kw": 3952,
        "sodium_metal_halide_kwh": 988.5,
        "sodium_metal_halide_lifespan": 12.5,

        "header15": "Bateria: Zinco-Catodo Híbrido",

        "zinc_hybrid_cathode_kw": 2200,
        "zinc_hybrid_cathode_kwh": 550.5,
        "zinc_hybrid_cathode_lifespan": 10,

        "header18": "Ultracapacitor",

        "ultracapacitor_kw": 930,
        "ultracapacitor_kw": 74480,
        "ultracapacitor_lifespan": 16

    }

    INITIAL_VALUES_BATTERIES = SimpleNamespace(
        # Data from DOE
        lead_acid_kw=1976,
        lead_acid_kwh=494.5,
        lead_acid_lifespan=3,

        li_ion_kw=1946,
        li_ion_kwh=487,
        li_ion_lifespan=10,

        sodium_sulfur_kw=3782,
        sodium_sulfur_kwh=946,
        sodium_sulfur_lifespan=13.5,

        redox_flow_kw=3984,
        redox_flow_kwh=996.5,
        redox_flow_lifespan=15,

        sodium_metal_halide_kw=3952,
        sodium_metal_halide_kwh=988.5,
        sodium_metal_halide_lifespan=12.5,

        zinc_hybrid_cathode_kw=2200,
        zinc_hybrid_cathode_kwh=550.5,
        zinc_hybrid_cathode_lifespan=10,

        ultracapacitor_kw=930,
        ultracapacitor_kwh=74480,
        ultracapacitor_lifespan=16)

    @staticmethod
    def is_valid(data, mode):
        if mode == "turbines":
            return data in ValidData.VALID
        elif mode == "batteries":
            return data in ValidData.VALID_BATTERIES

    @staticmethod
    def get_valid_data(mode):
        if mode == "turbines":
            return ValidData.VALID
        elif mode == "batteries":
            return ValidData.VALID_BATTERIES

    @staticmethod
    def get_valid_data_by_key(key, mode):
        if mode == "turbines":
            return ValidData.VALID[key]
        elif mode == "batteries":
            return ValidData.VALID_BATTERIES[key]

    @staticmethod
    def get_valid_data_by_value(value, mode):
        if mode == "turbines":
            return list(ValidData.VALID.keys())[list(ValidData.VALID.values()).index(value)]
        elif mode == "batteries":
            return list(ValidData.VALID_BATTERIES.keys())[list(ValidData.VALID_BATTERIES.values()).index(value)]

    @staticmethod
    def get_initial_values(mode):
        if mode == "turbines":
            return ValidData.INITIAL_VALUES
        elif mode == "batteries":
            return ValidData.INITIAL_VALUES_BATTERIES
        else:
            raise ValueError("Modo inválido!")

    @staticmethod
    def get_header_positions(mode):
        if mode == "turbines":
            return ValidData.header_positions
        elif mode == "batteries":
            return ValidData.header_positions_batteries

# This means: After index x put header
header_positions_turbines = [0, 6, 16, 26]
# To get that: (index in valid) - (how many were before)
headers_turbines = {
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

# This means: After index x put header
header_positions_batteries = [0, 3, 6, 9, 12, 15, 18]

headers_batteries = {
    "header0": "Bateria: Chumbo-Ácido",

    "lead_acid_kw": "Custo de projeto por kW",
    "lead_acid_lifespan": "Vida útil (anos)",
    "lead_acid_kwh": "Custo de projeto por kWh",

    "header3": "Bateria: Lítio-Íon",

    "li_ion_kw": "Custo de projeto por kW",
    "li_ion_lifespan": "Vida útil (anos)",
    "li_ion_kwh": "Custo de projeto por kWh",

    "header6": "Bateria: Sódio-Enxofre",

    "sodium_sulfur_kw": "Custo de projeto por kW",
    "sodium_sulfur_lifespan": "Vida útil (anos)",
    "sodium_sulfur_kwh": "Custo de projeto por kWh",

    "header9": "Bateria: Fluxo de oxidação",

    "redox_flow_kw": "Custo de projeto por kW",
    "redox_flow_lifespan": "Vida útil (anos)",
    "redox_flow_kwh": "Custo de projeto por kWh",

    "header12": "Bateria: Sódio-Metal",

    "sodium_metal_halide_kw": "Custo de projeto por kW",
    "sodium_metal_halide_lifespan": "Vida útil (anos)",
    "sodium_metal_halide_kwh": "Custo de projeto por kWh",

    "header15": "Bateria: Zinco-Catodo Híbrido",

    "zinc_hybrid_cathode_kw": "Custo de projeto por kW",
    "zinc_hybrid_cathode_lifespan": "Vida útil (anos)",
    "zinc_hybrid_cathode_kwh": "Custo de projeto por kWh",

    "header18": "Ultracapacitor",

    "ultracapacitor_kw": "Custo de projeto por kW",
    "ultracapacitor_lifespan": "Vida útil (anos)",
    "ultracapacitor_kwh": "Custo de projeto por kWh",
}

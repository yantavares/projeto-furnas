from Headers import headers_turbinas, header_posicoes_turbinas, headers_baterias, header_posicoes_baterias
from types import SimpleNamespace


class Valores_Iniciais:
    # Definição de constantes que serão utilizadas como constantes no programa
    VALORES_INICIAIS = SimpleNamespace(

        # taxa de inflação em dólares corrigida  https://www.bls.gov/data/inflation_calculator.htm
        multiplicador_inflacao_2012=1.35,
        multiplicador_inflacao_2019=1.22,
        # Transformação de BTU/ft^3 (BTU sobre pé cubico) para MJ/m^3 (Megajoule sobre metro cúbico)
        # Encontrado em: https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion-calculators.php
        metro_cubico_para_pes=35.3,
        # Taxa de juros de 5% ao ano
        taxa_de_juros=0.05,
        # Considerando que o preço do pé cúbico do gás natural é 0,27051 USD
        # De acordo com: https://www.eia.gov/dnav/ng/hist/n3035us3A.htm
        preco_gas_natural=7.66,
        # Tempo para pagar o valor da turbina em 20 anos de 12 meses
        tempo_pagar_turbina=20 * 12,

        # Para a CCGT - modelo GE 7HA.01 Combined Cycle 1x1: https://www.ge.com/gas-power/products/gas-turbinas/7ha
        CCGT_potencia=430,  # MW
        CCGT_custo_total=1084,  # $/kW
        CCGT_custo_OM=14.1 * 1000,  # US$/MW por ano
        CCGT_eficiencia=0.623,  # 62.3%
        CCGT_tempo_hot_start=105,  # Minutos
        CCGT_tempo_warm_start=105,  # Minutos
        CCGT_tempo_cold_start=105,  # Minutos
        CCGT_custo_hot_start=35,  # $/MW
        CCGT_custo_warm_start=55,  # $/MW
        CCGT_custo_cold_start=79,  # $/MW

        # Para a Aero GT - modelo GE LM600: https://www.ge.com/gas-power/products/gas-turbinas/lm6000
        Aero_potencia=106,  # MW
        Aero_custo_total=1175,  # $/kW
        Aero_custo_OM=16.3 * 1000,  # US$/MW por ano
        Aero_eficiencia=0.408,  # 40.8%
        Aero_tempo_hot_start=2,  # Minutos
        Aero_tempo_warm_start=4,  # Minutos
        Aero_tempo_cold_start=5,  # Minutos
        Aero_custo_hot_start=19,  # $/MW
        Aero_custo_warm_start=24,  # $/MW
        Aero_custo_cold_start=32,  # $/MW

        # Para a Heavy Duty - modelo GE 7F.05: https://www.ge.com/gas-power/products/gas-turbinas/7f
        Heavy_Duty_potencia=239,  # MW
        Heavy_Duty_custo_total=713,  # $/kW
        Heavy_Duty_custo_OM=7 * 1000,  # US$/MW por ano
        Heavy_Duty_eficiencia=0.385,  # 38.5%
        Heavy_Duty_tempo_hot_start=20,  # Minutos
        Heavy_Duty_tempo_warm_start=25,  # Minutos
        Heavy_Duty_tempo_cold_start=25,  # Minutos
        Heavy_Duty_custo_hot_start=36,  # $/MW
        Heavy_Duty_custo_warm_start=58,  # $/MW
        Heavy_Duty_custo_cold_start=75,  # $/MW

        # Fontes:
        # - https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2020.pdf
        # - https://www.ge.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/products/gas-turbinas/7ha-fact-sheet-product-specifications.pdf
        # - https://etn.global/wp-content/uploads/2018/09/Startup_time_reduction_for_Combined_Cycle_Power_Plants.pdf
        # - https://www.nrel.gov/docs/fy12osti/55433.pdf
    )

    VALORES_INICIAIS_BATERIAS = SimpleNamespace(
        # Dados do site da DOE
        chumbo_acido_kw=1976,
        chumbo_acido_vida_util=3,
        chumbo_acido_kwh=494.5,

        li_ion_kw=1946,
        li_ion_vida_util=10,
        li_ion_kwh=487,

        sodio_enxofre_kw=3782,
        sodio_enxofre_vida_util=13.5,
        sodio_enxofre_kwh=946,

        fluxo_oxidacao_kw=3984,
        fluxo_oxidacao_vida_util=15,
        fluxo_oxidacao_kwh=996.5,

        sodio_metal_kw=3952,
        sodio_metal_vida_util=12.5,
        sodio_metal_kwh=988.5,

        zinco_catodo_kw=2200,
        zinco_catodo_vida_util=10,
        zinco_catodo_kwh=550.5,

        ultracapacitor_kw=930,
        ultracapacitor_vida_util=16,
        ultracapacitor_kwh=74480,
    )

    @staticmethod
    def valido(data, mode):
        if mode == "turbinas":
            return data in headers_turbinas
        elif mode == "baterias":
            return data in headers_baterias
        else:
            raise ValueError("Modo inválido!")

    @staticmethod
    def resgatar_valores_validos(mode):
        if mode == "turbinas":
            return headers_turbinas
        elif mode == "baterias":
            return headers_baterias
        else:
            raise ValueError("Modo inválido!")

    @staticmethod
    def resgatar_valores_validos_por_indice(key, mode):
        if mode == "turbinas":
            return headers_turbinas[key]
        elif mode == "baterias":
            return headers_baterias[key]
        else:
            raise ValueError("Modo inválido!")

    @staticmethod
    def resgatar_valores_validos_por_valor(value, mode):
        if mode == "turbinas":
            return list(headers_turbinas.keys())[list(headers_turbinas.values()).index(value)]
        elif mode == "baterias":
            return list(headers_baterias.keys())[list(headers_baterias.values()).index(value)]
        else:
            raise ValueError("Modo inválido!")

    @staticmethod
    def resgatar_valores_iniciais(mode):
        if mode == "turbinas":
            return Valores_Iniciais.VALORES_INICIAIS
        elif mode == "baterias":
            return Valores_Iniciais.VALORES_INICIAIS_BATERIAS
        else:
            raise ValueError("Modo inválido!")

    @staticmethod
    def resgatar_posicoes_header(mode):
        if mode == "turbinas":
            return header_posicoes_turbinas
        elif mode == "baterias":
            return header_posicoes_baterias
        else:
            raise ValueError("Modo inválido!")

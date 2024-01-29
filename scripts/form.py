from IPython.display import display, clear_output
# IPython Display: Exibição de objetos no Jupyter.

from ipywidgets import Button, Dropdown, FloatText, VBox, HBox, Layout
# Ipywidgets: Criação de widgets interativos para Jupyter.


# Criar widgets
dropdown = Dropdown(
    options=['Usar Dados Padrão', 'Usar Dados Personalizados'],
    description='Escolha:',
    disabled=False,
)

# Função para lidar com mudanças no dropdown


def manipulador_evento_dropdown(change):
    clear_output(wait=True)
    display(dropdown)
    if change.new == 'Usar Dados Personalizados':
        exibir_formulario_dados_personalizados()


def exibir_formulario_dados_personalizados():

    # Definição de estilo para os widgets
    style = {'description_width': '230px'}

    # Definição de layout para os widgets
    layout = Layout(width='auto', margin='5px auto')

    # Botão para enviar os dados
    botao_enviar = Button(description='Enviar', layout=Layout(
        width='auto', margin='0 auto'))

    def criar_widget(description, value, disabled=False, style=style, layout=layout):
        return FloatText(description=description,
                         value=value,
                         disabled=disabled,
                         style=style,
                         layout=layout)

    elementos_para_exibir = {
        "potencia_termo_input": criar_widget('Potência Termelétrica (W): ', 100),
        "custo_capital_termo_input": criar_widget('Custo de Capital Termelétrico ($/W): ', 100),
        "custo_oem_input": criar_widget('Custo de O&M ($/W): ', 100),
        "taxa_de_juros_input": criar_widget('Taxa de Juros (%): ', 100),
        "tempo_pagar_divida_input": criar_widget('Tempo para Pagar a Dívida (anos): ', 100),
        "eficiencia_aeroGT_input": criar_widget('Eficiência AeroGT (%): ', 100),
        "eficiencia_steam_input": criar_widget('Eficiência Steam (%): ', 100),
        "eficiencia_NG_input": criar_widget('Eficiência NG (%): ', 100),
        "energia_combustivel_input": criar_widget('Energia do Combustível (MJ/kg): ', 100),
        "preco_combustivel_input": criar_widget('Preço do Combustível ($/kg): ', 100),
        "custo_ciclo_aeroGT_cold_input": criar_widget('Custo do Ciclo AeroGT ($/W): ', 100),
        "custo_ciclo_steam_cold_input": criar_widget('Custo do Ciclo Steam ($/W): ', 100),
        "custo_ciclo_NG_cold_input": criar_widget('Custo do Ciclo NG ($/W): ', 100),
        "custo_ciclo_aeroGT_warm_input": criar_widget('Custo do Ciclo AeroGT ($/W): ', 100),
        "custo_ciclo_steam_warm_input": criar_widget('Custo do Ciclo Steam ($/W): ', 100),
        "custo_ciclo_NG_warm_input": criar_widget('Custo do Ciclo NG ($/W): ', 100),
        "custo_ciclo_aeroGT_hot_input": criar_widget('Custo do Ciclo AeroGT ($/W): ', 100),
        "custo_ciclo_steam_hot_input": criar_widget('Custo do Ciclo Steam ($/W): ', 100),
        "custo_ciclo_NG_hot_input": criar_widget('Custo do Ciclo NG ($/W): ', 100),
        "limite_ciclo_aeroGT_cold_input": criar_widget('Limite do Ciclo AeroGT (s): ', 100),
        "limite_ciclo_steam_cold_input": criar_widget('Limite do Ciclo Steam (s): ', 100),
        "limite_ciclo_NG_cold_input": criar_widget('Limite do Ciclo NG (s): ', 100),
        "limite_ciclo_aeroGT_warm_input": criar_widget('Limite do Ciclo AeroGT (s): ', 100),
        "limite_ciclo_steam_warm_input": criar_widget('Limite do Ciclo Steam (s): ', 100),
        "limite_ciclo_NG_warm_input": criar_widget('Limite do Ciclo NG (s): ', 100),
        "limite_ciclo_aeroGT_hot_input": criar_widget('Limite do Ciclo AeroGT (s): ', 100),
        "limite_ciclo_steam_hot_input": criar_widget('Limite do Ciclo Steam (s): ', 100),
        "limite_ciclo_NG_hot_input": criar_widget('Limite do Ciclo NG (s): ', 100),
    }

    def display_form(widgets):
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

        rows.append([botao_enviar])
        form = VBox([HBox([element for element in row]) for row in rows])
        display(form)

    def manipulador_evento_botao_enviar(_):
        try:
            potencia_termo = elementos_para_exibir["potencia_termo_input"].value
            custo_capital_termo = elementos_para_exibir["custo_capital_termo_input"].value
            custo_oem = elementos_para_exibir["custo_oem_input"].value
            taxa_de_juros = elementos_para_exibir["taxa_de_juros_input"].value
            tempo_pagar_divida = elementos_para_exibir["tempo_pagar_divida_input"].value
            eficiencia_aeroGT = elementos_para_exibir["eficiencia_aeroGT_input"].value
            eficiencia_steam = elementos_para_exibir["eficiencia_steam_input"].value
            eficiencia_NG = elementos_para_exibir["eficiencia_NG_input"].value
            energia_combustivel = elementos_para_exibir["energia_combustivel_input"].value
            preco_combustivel = elementos_para_exibir["preco_combustivel_input"].value
            custo_ciclo_aeroGT_cold = elementos_para_exibir["custo_ciclo_aeroGT_cold_input"].value
            custo_ciclo_steam_cold = elementos_para_exibir["custo_ciclo_steam_cold_input"].value
            custo_ciclo_NG_cold = elementos_para_exibir["custo_ciclo_NG_cold_input"].value
            custo_ciclo_aeroGT_warm = elementos_para_exibir["custo_ciclo_aeroGT_warm_input"].value
            custo_ciclo_steam_warm = elementos_para_exibir["custo_ciclo_steam_warm_input"].value
            custo_ciclo_NG_warm = elementos_para_exibir["custo_ciclo_NG_warm_input"].value
            custo_ciclo_aeroGT_hot = elementos_para_exibir["custo_ciclo_aeroGT_hot_input"].value
            custo_ciclo_steam_hot = elementos_para_exibir["custo_ciclo_steam_hot_input"].value
            custo_ciclo_NG_hot = elementos_para_exibir["custo_ciclo_NG_hot_input"].value
            limite_ciclo_aeroGT_cold = elementos_para_exibir["limite_ciclo_aeroGT_cold_input"].value
            limite_ciclo_steam_cold = elementos_para_exibir["limite_ciclo_steam_cold_input"].value
            limite_ciclo_NG_cold = elementos_para_exibir["limite_ciclo_NG_cold_input"].value
            limite_ciclo_aeroGT_warm = elementos_para_exibir["limite_ciclo_aeroGT_warm_input"].value
            limite_ciclo_steam_warm = elementos_para_exibir["limite_ciclo_steam_warm_input"].value
            limite_ciclo_NG_warm = elementos_para_exibir["limite_ciclo_NG_warm_input"].value
            limite_ciclo_aeroGT_hot = elementos_para_exibir["limite_ciclo_aeroGT_hot_input"].value
            limite_ciclo_steam_hot = elementos_para_exibir["limite_ciclo_steam_hot_input"].value
            limite_ciclo_NG_hot = elementos_para_exibir["limite_ciclo_NG_hot_input"].value\

            print("Dados enviados com sucesso!")
        except Exception as e:
            print("Não foi possível ler os dados inseridos")
            print(e)

    display_form(elementos_para_exibir)
    botao_enviar.on_click(manipulador_evento_botao_enviar)


def exibir_formulario():
    # Exibir dropdown inicial
    display(dropdown)
    dropdown.observe(manipulador_evento_dropdown, names='value')

from IPython.display import display, clear_output
from ipywidgets import Button, Dropdown, VBox, HBox, Layout
import pandas as pd
from types import SimpleNamespace
if __name__ == "__main__":
    from ConstHandler import Constants
else:
    from .ConstHandler import Constants


class FormularioFurnas:
    def __init__(self):
        self.consts = Constants()
        self.inicializar_widgets()
        self.configurar_observadores()

    def inicializar_widgets(self):
        self.dropdown = Dropdown(
            options=['Usar Dados Padrão', 'Usar Dados Personalizados'],
            description='Escolha:',
            disabled=False,
        )
        self.criar_widgets_dados()
        self.botao_enviar = Button(
            description='Enviar', layout=Layout(width='auto', margin='10px auto'))
        self.botao_exportar_csv = Button(
            description='Exportar CSV')
        self.botao_carregar_csv = Button(
            description='Carregar CSV')

    def configurar_observadores(self):
        self.dropdown.observe(self.manipulador_evento_dropdown, names='value')
        self.botao_enviar.on_click(self.manipulador_evento_botao_enviar)
        self.botao_exportar_csv.on_click(self.manipulador_evento_baixar_csv)
        self.botao_carregar_csv.on_click(self.manipulador_evento_carregar_csv)

    def criar_widgets_dados(self):
        widgets = self.consts.get_widgets()

    def exibir_formulario(self):
        display(self.dropdown)
        self.atualizar_valores()

    def manipulador_evento_dropdown(self, change):
        clear_output(wait=True)
        display(self.dropdown)
        if change.new == 'Usar Dados Personalizados':
            self.exibir_formulario_dados_personalizados()
        else:
            self.consts = Constants()

    def formulario_namespace(self, namespace):
        # Converte o SimpleNamespace em um dicionário
        widgets = vars(namespace)
        rows = []
        dict_iterator = iter(widgets.items())

        while True:
            try:
                _, element1 = next(dict_iterator)
                _, element2 = next(dict_iterator)
                rows.append([element1, element2])
            except StopIteration:
                try:
                    _, element1 = next(dict_iterator)
                    rows.append([element1])
                except StopIteration:
                    break

        rows.append([self.botao_enviar])

        form = VBox([HBox([element for element in row]) for row in rows])
        return form

    def exibir_formulario_dados_personalizados(self):
        # Exibir o formulário
        display(self.formulario_namespace(self.consts.get_widgets()))
        display(
            HBox([self.botao_exportar_csv, self.botao_carregar_csv]))

    def atualizar_valores(self):
        self.consts.set_values()

    def manipulador_evento_botao_enviar(self, _):
        try:
            self.atualizar_valores()
            print("Valores atualizados com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar valores: {e}")

    def recuperar_valores(self):
        return self.consts.get_values()

    def manipulador_evento_baixar_csv(self, _):
        try:
            valores = self.recuperar_valores()

            # Convert SimpleNamespace to dictionary
            if isinstance(valores, SimpleNamespace):
                valores_dict = vars(valores)
            else:
                valores_dict = valores

            # Now create a DataFrame
            # Use a list to ensure it's treated as a single row
            df = pd.DataFrame([valores_dict])
            df.to_csv('src/content/dados.csv', index=False)
            print("CSV exportado com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar csv: {e}")

    def exibir_formulario_dados_personalizados_e_dropdown(self):
        display(self.dropdown)
        self.exibir_formulario_dados_personalizados()

    def manipulador_evento_carregar_csv(self, _):
        try:
            clear_output(wait=True)
            try:
                df = pd.read_csv('src/content/dados.csv')
                # Convert DataFrame to SimpleNamespace
                valores = SimpleNamespace(**df.to_dict(orient='records')[0])
                self.consts.set_personalized_values(valores)
                self.exibir_formulario_dados_personalizados_e_dropdown()
                print("CSV carregado com sucesso!")
            except FileNotFoundError:
                self.exibir_formulario_dados_personalizados_e_dropdown()
                print("Arquivo não encontrado!")
                print(
                    "Por favor, exporte um arquivo CSV ou adicione um arquivo CSV na pasta 'content' e tente novamente")
        except Exception as e:
            self.exibir_formulario_dados_personalizados_e_dropdown()
            print(f"Erro ao carregar csv: verifique os dados inseridos!")
            print(f"Erro: {e}")


if __name__ == "__main__":
    formulario = FormularioFurnas()
    formulario.exibir_formulario()
    formulario.recuperar_valores()

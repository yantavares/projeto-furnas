from IPython.display import display, clear_output
from ipywidgets import Button, Dropdown, VBox, HBox, Layout
if __name__ == "__main__":
    from modules.ConstHandler import Constants
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
            description='Enviar', layout=Layout(width='auto', margin='0 auto'))

    def configurar_observadores(self):
        self.dropdown.observe(self.manipulador_evento_dropdown, names='value')
        self.botao_enviar.on_click(self.manipulador_evento_botao_enviar)

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


if __name__ == "__main__":
    formulario = FormularioFurnas()
    formulario.exibir_formulario()
    formulario.recuperar_valores()

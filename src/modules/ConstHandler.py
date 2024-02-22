# Importações necessárias para definir os widgets e manipular namespaces
from types import SimpleNamespace
from ipywidgets import FloatText, Layout, HTML
from collections import OrderedDict
from ValidData import ValidData


# Obtenção dos dados válidos a partir da classe ValidData
VALID = ValidData.get_valid_data()

# Obtenção dos dados iniciais a partir da classe ValidData
INITIAL = ValidData.get_initial_values()


def criar_widget(description, value, disabled=False, widget_style={'description_width': '325px'}, widget_layout=Layout(width='auto', margin='5px')):
    """
    Cria e retorna um widget FloatText para entrada de dados numéricos.

    :param description: Descrição do widget (aparece ao lado do campo de entrada).
    :param value: Valor inicial do widget.
    :param disabled: Define se o widget está desativado.
    :param widget_style: Estilo CSS do widget.
    :param widget_layout: Layout CSS do widget.
    :return: Instância do widget FloatText configurado.
    """
    return FloatText(description=description,
                     title=description,
                     label=description,
                     value=value,
                     disabled=disabled,
                     style=widget_style,
                     layout=widget_layout)


def criar_header(t):
    return HTML(f"<h2>{t}</h2>")


def calcular_combustivel(Turbine_Power, efficiency):
    """
    Calcula o volume de combustível necessário com base na potência da turbina e sua eficiência.

    :param Turbine_Power: Potência da turbina.
    :param efficiency: Eficiência da turbina.
    :return: Volume de combustível necessário.
    """
    Volume = Turbine_Power / efficiency
    return Volume


def map_simple_namespace(a, f):
    """
    Aplica uma função a cada valor dentro de um SimpleNamespace e retorna um novo SimpleNamespace com os resultados.

    :param a: SimpleNamespace original.
    :param f: Função a ser aplicada a cada valor.
    :return: Novo SimpleNamespace com valores modificados.
    """
    # Converte o SimpleNamespace em dicionário
    a_dict = vars(a)
    # Aplica a função f a cada valor do dicionário
    b_dict = {k: f(v) for k, v in a_dict.items()}
    # Converte o dicionário modificado de volta para SimpleNamespace
    b = SimpleNamespace(**b_dict)
    return b


def convert_to_widget(a):
    """
    Converte um SimpleNamespace em um conjunto de widgets, baseando-se nas chaves válidas.

    :param a: SimpleNamespace contendo os valores a serem convertidos em widgets.
    :return: SimpleNamespace contendo os widgets.
    """
    # Converte o SimpleNamespace em dicionário
    a_dict = vars(a)
    try:
        # Cria um dicionário de widgets usando criar_widget para cada valor
        count = 0
        headers = ValidData.get_header_positions()
        b_dict = {}
        for k, v in a_dict.items():
            if count in headers:
                b_dict["header" +
                       str(count)] = criar_header(VALID["header" + str(count)])
            if k in VALID.keys():
                b_dict[k] = criar_widget(VALID[k], v)
            count += 1

        b = SimpleNamespace(**b_dict)
        return b
    except:
        print("Valor inválido de variável. Verifique os dados inseridos!")
        return a


class Constants:
    """
    Classe para gerenciar constantes e valores do formulário, incluindo a criação de widgets correspondentes.

    As fontes para os dados incluem publicações da EIA, GE, ETN, e NREL.
    """

    def __init__(self):
        # Inicialização dos valores padrão
        self.values = ValidData.get_initial_values()

        # Conversão dos valores para widgets
        self.widget_constants = convert_to_widget(self.values)

    def get_widgets(self):
        """
        Retorna os widgets correspondentes às constantes.
        """
        return self.widget_constants

    def set_values(self):
        """
        Atualiza os valores das constantes com base nos valores inseridos nos widgets.
        """
        novo_namespace = map_simple_namespace(
            self.widget_constants, lambda x: x.value)
        self.values = novo_namespace

    def set_personalized_values(self, values):
        """
        Define valores personalizados, garantindo que as chaves sejam válidas.
        """
        try:
            for key, _ in vars(values).items():
                if key not in VALID.keys():
                    raise ValueError("Chave inválida!", key)

            values = self.patch_values(values)
            self.widget_constants = convert_to_widget(values)
        except Exception as e:
            raise ValueError("Erro ao atualizar valores personalizados: ", e)

    def get_values(self):
        """
        Retorna os valores atualizados das constantes.
        """
        return self.values

    def patch_values(self, new_values: SimpleNamespace, initial_values=INITIAL):
        """
        Adiciona campos faltantes com valores padrão e atualiza os valores das constantes com base nos valores inseridos.
        """
        new_values_pacthed = SimpleNamespace()
        try:
            for key, value in vars(initial_values).items():
                if key not in vars(new_values).keys():
                    print(f"Chave {key} não encontrada. Usando valor padrão.")
                    setattr(new_values_pacthed, key, value)
                else:
                    setattr(new_values_pacthed, key, getattr(new_values, key))

            return new_values_pacthed

        except Exception as e:
            raise ValueError("Erro ao atualizar valores personalizados: ", e)


# Bloco de execução principal para testar a classe Constants
if __name__ == "__main__":
    c = Constants()
    c.set_values()
    print(c.get_values())

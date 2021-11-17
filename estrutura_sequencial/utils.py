from collections.abc import Iterable


def input_number(prompt, numeric_type=int):
    """Retorna valor numérico conforme o tipo definido"""
    numeric_types = {
        float: 'ponto flutuante',
        int: 'inteiro'
    }
    if not issubclass(numeric_type, (float, int)):
        raise TypeError(
            f'"numeric_type" precisa ser uma subclasse de float ou int.'
        )
    while True:
        try:
            return numeric_type(input(prompt))
        except ValueError:
            print(
                'O valor informado não é um número válido do tipo '
                f'{numeric_types.get(numeric_type)}. Tente novamente.'
            )


def input_option(prompt, valid_options):
    """Retorna a opção selecionada entre as disponíveis"""
    if not isinstance(valid_options, Iterable):
        raise TypeError(
            f'"valid_options" deve ser um iterável.'
        )
    if not valid_options:
        raise ValueError('"valid_options" não deve estar vazio.')
    valid_options = [str(option) for option in valid_options]
    while True:
        option = input(prompt)
        if option in valid_options:
            return option
        print(
            f'A opção "{option}" não está entre as opções disponíveis '
            f'({list_as_text(valid_options)}). Tente novamente.'
        )


def list_as_text(items, last_sep='e'):
    """
    Converte um iterável em uma enumeração:
    >>> list_as_text([])
    ''
    >>> list_as_text(['Dona Flor'])
    'Dona Flor'
    >>> list_as_text(['Dona Flor', 'Vadinho', 'Teodoro'])
    'Dona Flor, Vadinho e Teodoro'
    >>> list_as_text(['Dona Flor', 'Vadinho', 'Teodoro'], last_sep='ou')
    'Dona Flor, Vadinho ou Teodoro'
    """
    if not items:
        text = ''
    elif len(items) == 1:
        text = str(items[0])
    else:
        text = (
            f'{", ".join(str(item) for item in items[:-1])} '
            f'{last_sep} {items[-1]}'
        )
    return text


def pluralize(items, singular, plural=None):
    """
    Retorna o singular ou plural de uma palavra baseado em um valor ou
    na contagem de uma sequência de items informada:
    >>> pluralize(0, 'item')
    'items'
    >>> pluralize(1, 'item')
    'item'
    >>> pluralize(2, 'item')
    'items'
    >>> pluralize([], 'class', 'classes')
    'classes'
    >>> pluralize([0], 'class', 'classes')
    'class'
    >>> pluralize([0, 1], 'class', 'classes')
    'classes'
    """
    try:
        count = len(items)
    except TypeError:
        count = int(items)
    if count == 1:
        return singular
    if not plural:
        return f'{singular}s'
    return plural
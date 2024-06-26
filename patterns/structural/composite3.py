"""Демонстратор взаимного компоновщика с классом-примесью."""

from collections.abc import Iterable


class Connectable(Iterable):
    """
    Примесь, обеспечивающая подключение любых нейронов друг к другу.
    """
    def connect_to(self, other: Iterable['Neuron']) -> None:
        if self is other:
            return
        for neuron_out in self:
            for neuron_in in other:
                neuron_out.outputs.append(neuron_in)
                neuron_in.inputs.append(neuron_out)


class Neuron(Connectable):
    """
    Каждый нейрон имеет входы и выходы, через которые может быть связан с другими нейронами.
    """
    def __init__(self, name: str):
        self.name = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []

    def __iter__(self):
        yield self

    def __str__(self):
        return f'<{self.name}>'

    def show_connections(self):
        res = '\tinputs:\n'
        res += '\n'.join(f'\t\t{neuron}' for neuron in self.inputs)
        res += '\n\toutputs:\n'
        res += '\n'.join(f'\t\t{neuron}' for neuron in self.outputs)
        return res


class NeuronLayer(list, Connectable):
    """
    Объединение нейронов в один слой.
    """
    def __init__(self, name: str, count: int = 2):
        super().__init__()
        self.name = name
        for i in range(1, count+1):
            self.append(Neuron(f'{self.name} Нейрон {i}'))

    def __str__(self):
        return '\n'.join(str(neuron) for neuron in self)


# >>> nl1 = NeuronLayer('Слой 1')
# >>> nl2 = NeuronLayer('Слой 2', 3)
# >>> 
# >>> nl2.connect_to(nl1)
# >>> 
# >>> print(nl1, end='\n\n')
# <Слой 1 Нейрон 1>
# <Слой 1 Нейрон 2>

# >>> print(nl2, end='\n\n\n')
# <Слой 2 Нейрон 1>
# <Слой 2 Нейрон 2>
# <Слой 2 Нейрон 3>


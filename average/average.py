
class Average:
    def __init__(self):
        self.serie = list()

    @property
    def sum_serie(self):
        return sum(self.serie)

    @property
    def avg(self):
        return self.sum_serie / self.__len__()

    def __len__(self):
        return len(self.serie)

    def __call__(self, value):
        self.serie.append(value)
        return self.sum_serie / self.__len__()


if __name__ == '__main__':
    notas_poo = Average()
    print('Adicionando nota %d, Média: %d' % (10, notas_poo(10)))
    print('Adicionando nota %d, Média: %d' % (5, notas_poo(5)))
    print('Adicionando nota %d, Média: %d' % (9, notas_poo(9)))
    print('Soma dos elementos da série:', notas_poo.sum_serie)
    print('Tamanho da série:', len(notas_poo))
    print('Média da série:', notas_poo.avg)

"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            itens     - informado
            valornota - calculado.
"""
import datetime
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal:
    def __init__(self, id3, codigo, cliente):
        self._Id = id3
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def dataNotaFiscal(self):
        lista_data_e_hora = str(self._data).split()
        data_lista = lista_data_e_hora[0].split('-')
        data_final_nota = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'
        return data_final_nota

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularTotalNota(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item.get_valor_item()
        self._valorNota = valor

    def getValorNota(self):
        return self._valorNota

    def imprimirNotaFiscal(self):
        linhaDivisoria = '-' * 111

        formataNota = '{}\n' \
                          'NOTA FISCAL{:>100}\n' \
                          'Cliente:{:>6}{:>4}Nome: {}\n' \
                          'CPF/CNPJ: {}\n' \
                          '{}\n' \
                          'ITENS\n' \
                          '{}\n' \
                          'Seq{:>3}Descricao{:>52}QTD{:>7}Valor Unit{:19}Preço\n' \
                          '{}  {}    {}     {}     {}'.format(linhaDivisoria,
                                                              self.dataNotaFiscal(),
                                                              self._cliente.get_codigo(), ' ', self._cliente.get_nome(),
                                                              self._cliente.get_cnpjcpf(),
                                                              linhaDivisoria,
                                                              linhaDivisoria,
                                                              ' ', ' ', ' ', ' ',
                                                              '-' * 4, '-' * 56, '-' * 5, '-' * 12, '-' * 18)

        if len(self._itens) > 0:
            for item_nota in self._itens:
                formataNota += '\n\n{}{:>3}{}'.format(item_nota.get_sequencial(), ' ', item_nota.get_descricao())
                formataNota += ' ' * (60 - len(item_nota.get_descricao()))
                formataNota += '{:.2f}             {:.2f}                  {:.2f}'.format(
                                                            item_nota.get_quantidade(), item_nota.get_valor_unitario(),
                                                            item_nota.get_valor_item())

        formataNota += '\n{}\nValor Total: {:.2f}'.format(linhaDivisoria, self._valorNota)
        print(formataNota)

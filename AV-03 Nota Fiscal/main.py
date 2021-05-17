from produto import Produto
from cliente import Cliente
from notafiscal import NotaFiscal
from itemnotafiscal import ItemNotaFiscal


def main():
    clienteMercado = Cliente(1, "Kelvin de Lima Rodrigues", 1446, "618.246.043-19", 1)

    produto1 = Produto(1, 100, "Grão de Bico", 4.5)
    itemAdd1 = ItemNotaFiscal(1, 1, 10, produto1)

    produto2 = Produto(2, 200, "Biscoito Maizena", 3.2)
    itemAdd2 = ItemNotaFiscal(2, 2, 10, produto2)

    produto3 = Produto(3, 300, "Flocão de Milho", 6.0)
    itemAdd3 = ItemNotaFiscal(3, 3, 10, produto3)

    nf = NotaFiscal(1, 100, clienteMercado)

    nf.adicionarItem(itemAdd1)

    nf.adicionarItem(itemAdd2)

    nf.adicionarItem(itemAdd3)

    nf.calcularTotalNota()

    nf.imprimirNotaFiscal()


if __name__ == '__main__':
    main()

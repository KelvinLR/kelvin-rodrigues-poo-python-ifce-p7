import datetime
from models.cliente import Cliente
from models.itemnotafiscal import ItemNotaFiscal

class NotaFiscal():
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota = valor

    def to_json(self):
        return {"id": self._Id, "codigo": self._codigo, "cliente": self._cliente.to_json(),
                "data": str(self._data), "itens": [i.to_json() for i in self._itens], "valorNota": self._valorNota}

    def imprimirNotaFiscal(self):
        pass
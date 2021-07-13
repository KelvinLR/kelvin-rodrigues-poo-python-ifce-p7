import datetime
from . import db

# model Cliente
class Cliente():
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    codigo = db.Column(db.Integer)
    cnpjcpf = db.Column(db.String(50))
    tipo = db.Column(db.String(50))

    NFiscais = db.relationship("NotaFiscal")

    def __init__(self, id, nome, codigo, cpfcnpj, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cpfcnpj = cpfcnpj
        self._tipo = tipo

    def to_json(self):
        return {"id": self._id, "nome": self._nome, "codigo": self._codigo, "cpfcnpj": self._cpfcnpj, "tipo": self._tipo}

# model Produto

class Produto():
    __tablename__ = 'Prods'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    descricao = db.Column(db.String(200))
    valorUnitario = db.Column(db.Float)

    itemID = db.Column(db.Integer, db.ForeignKey('itens.id'))

    def __init__(self, id, codigo, descricao, valorUnitario):
        self._id = id
        self._codigo = codigo
        self._descricao = descricao
        self._valorUnitario = valorUnitario

    def getDescricao(self):
        return self._descricao

    def getValorUnitario(self):
        return self._valorUnitario

    def to_json(self):
        return {"id": self._id, "codigo": self._codigo, "descricao": self._descricao,
                "valorUnitario": self._valorUnitario}

# model NotaFiscal

class NotaFiscal():
    __tablename__ = 'NFiscais'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(100))

    clienteID = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    itens = db.relationship("ItemNotaFiscal")

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

# model ItemNotaFiscal

class ItemNotaFiscal():
    __tablename__ = 'itens'

    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)

    Prods = db.relationship("Produto")
    notaID = db.Column(db.Integer, db.ForeignKey('NFiscais.id'))

    def __init__(self, id, sequencial, quantidade, produto):
        self._id = id
        self._sequencial = sequencial
        self._quantidade = quantidade
        self._produto = produto
        self._descricao = self._produto.getDescricao()
        self._valorUnitario = self._produto.getValorUnitario()
        self._valorItem = float(self._quantidade * self._valorUnitario)

    def to_json(self):
        return {"id": self._id, "sequencial": self._sequencial, "quantidade": self._quantidade,
                "produto": self._produto.to_json(), "descricao": self._descricao, "valorUnitario": self._valorUnitario, "valorItem": self._valorItem}


class Produto():

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

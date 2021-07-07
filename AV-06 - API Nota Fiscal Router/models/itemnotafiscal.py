from models.produto import Produto


class ItemNotaFiscal():

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


if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    item = ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())

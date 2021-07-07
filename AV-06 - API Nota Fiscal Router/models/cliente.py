"""
    Módulo cliente -
    Classe Cliente -
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo do cliente   - informado
                    (Pessoa Fisica ou Juridica)

"""

class Cliente():
    def __init__(self, id, nome, codigo, cpfcnpj, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cpfcnpj = cpfcnpj
        self._tipo = tipo

    def to_json(self):
        return {"id": self._id, "nome": self._nome, "codigo": self._codigo, "cpfcnpj": self._cpfcnpj, "tipo": self._tipo}


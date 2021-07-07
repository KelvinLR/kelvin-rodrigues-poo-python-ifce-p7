from flask import Flask, render_template, Response, request
from models.cliente import Cliente
from models.notafiscal import NotaFiscal
from models.produto import Produto
from models.itemnotafiscal import ItemNotaFiscal
import json

def geraResponse(status, nomeConteudo, conteudo, mensagem=False):
    body = {}
    body[nomeConteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

#clientes
cl01 = Cliente(0, "Kelvin Rodrigues", 101, '072.406.301-00', 'Pessoa física')
cl02 = Cliente(1, "Raquel Maciel", 102, '232.443.334-82', 'Pessoa física')
cl03 = Cliente(2, "Yuri Santiago", 103, '543.891.592-41', 'Pessoa física')

listaClientes = [cl01, cl02, cl03]

#produtos
pr01 = Produto(0, 100, 'Arroz Branco', 5.70)
pr02 = Produto(1, 200, 'Macarrão Parafuso', 6.25)
pr03 = Produto(2, 300, 'Feijão Preto', 4.99)

listaProdutos = [pr01, pr02, pr03]

#notafiscal
nf01 = NotaFiscal(0, 100, cl01)
nf02 = NotaFiscal(1, 200, cl02)
nf03 = NotaFiscal(2, 300, cl03)

listaNF = [nf01, nf02, nf03]

#itemnotafiscal
item1 = ItemNotaFiscal(0, 1, 2, pr01)
item2 = ItemNotaFiscal(1, 1, 5, pr01)
item3 = ItemNotaFiscal(2, 2, 3, pr02)
item4 = ItemNotaFiscal(3, 1, 1, pr01)
item5 = ItemNotaFiscal(4, 2, 1, pr02)
item6 = ItemNotaFiscal(5, 3, 2, pr03)
item7 = ItemNotaFiscal(6, 1, 5, pr01)
item8 = ItemNotaFiscal(7, 2, 3, pr02)
item9 = ItemNotaFiscal(8, 3, 7, pr03)

listaItens = [item1, item2, item3, item4, item5, item6, item7, item8, item9]

# add itens na nota
nf01.adicionarItem(item1)
nf02.adicionarItem(item2)
nf02.adicionarItem(item3)
nf03.adicionarItem(item4)
nf03.adicionarItem(item5)
nf03.adicionarItem(item6)
nf03.adicionarItem(item7)
nf03.adicionarItem(item8)
nf03.adicionarItem(item9)


app = Flask(__name__)

# ROTAS CLIENTE

@app.route('/clientes', methods=['GET'])
def verClientes():
    cliente = listaClientes
    clienteJSON = [cliente.to_json() for cliente in listaClientes]
    return geraResponse(200, "clientes", clienteJSON)

@app.route('/cliente/<int:id>', methods=['GET'])
def verCliente(id):
    cliente = listaClientes[id]
    clienteJSON = cliente.to_json()
    return geraResponse(200, "cliente", clienteJSON)

@app.route('/cliente', methods=['POST'])
def addCliente():
    body = request.get_json()
    try:
        cliente = Cliente(id=body["id"], nome=body["nome"], codigo=body["codigo"], cpfcnpj=body["cpfcnpj"], tipo=body["tipo"])
        listaClientes.append(cliente)
        return geraResponse(201, "cliente", cliente.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "cliente", {}, "Erro ao cadastrar")

@app.route('/cliente/<int:id>', methods=['PUT'])
def attCliente(id):
    cliente = listaClientes[id]
    body = request.get_json()
    try:
        if ('nome' in body):
            cliente._nome = body['nome']
        if ('cpfcnpj' in body):
            cliente._cpfcnpj = body['cpfcnpj']

        listaClientes.append(cliente)
        return geraResponse(200, "cliente", cliente.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "cliente", {}, "Erro ao atualizar")

@app.route('/cliente/delete/<int:id>', methods=['DELETE'])
def delCliente(id):
    cliente = listaClientes[id]
    try:
        listaClientes.remove(cliente)
        return geraResponse(200, "cliente", cliente.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "cliente", {}, "Erro ao deletar")

# ROTAS PRODUTO

@app.route('/produtos', methods=['GET'])
def verProdutos():
    produto = listaProdutos
    produtoJSON = [produto.to_json() for produto in listaProdutos]
    return geraResponse(200, "produtos", produtoJSON)

@app.route('/produto/<int:id>', methods=['GET'])
def verProduto(id):
    produto = listaProdutos[id]
    produtoJSON = produto.to_json()
    return geraResponse(200, "produto", produtoJSON)

@app.route('/produto', methods=['POST'])
def addProduto():
    body = request.get_json()
    try:
        produto = Produto(id=body["id"], codigo=body["codigo"], descricao=body["descricao"], valorUnitario=body["valorUnitario"])
        listaProdutos.append(produto)
        return geraResponse(201, "produto", produto.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "produto", {}, "Erro ao cadastrar")

@app.route('/produto/<int:id>', methods=['PUT'])
def attProduto(id):
    produto = listaProdutos[id]
    body = request.get_json()
    try:
        if ('descricao' in body):
            produto._descricao = body['descricao']
        if ('valorUnitario' in body):
            produto._valorUnitario = body['valorUnitario']

        listaProdutos.append(produto)
        return geraResponse(200, "produto", produto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "produto", {}, "Erro ao atualizar")

@app.route('/produto/delete/<int:id>', methods=['DELETE'])
def delProduto(id):
    produto = listaProdutos[id]
    try:
        listaProdutos.remove(produto)
        return geraResponse(200, "produto", produto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "produto", {}, "Erro ao deletar")

# ROTAS NOTA FISCAL

@app.route('/notasfiscais', methods=['GET'])
def verNFS():
    notafiscal = listaNF
    nfJSON = [notafiscal.to_json() for notafiscal in listaNF]
    return geraResponse(200, "notafiscal", nfJSON)

@app.route('/notafiscal/<int:id>', methods=['GET'])
def verNF(id):
    notafiscal = listaNF[id]
    nfJSON = notafiscal.to_json()
    return geraResponse(200, "notafiscal", nfJSON)

@app.route('/notafiscal', methods=['POST'])
def addNF():
    body = request.get_json()
    try:
        nf = NotaFiscal(Id=body["Id"], codigo=body["codigo"], cliente=body["cliente"])
        listaNF.append(nf)
        return geraResponse(201, "notafiscal", nf.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "notafiscal", {}, "Erro ao cadastrar")

@app.route('/notafiscal/<int:id>', methods=['PUT'])
def attNF(id):
    nf = listaNF[id]
    body = request.get_json()
    try:
        if ('cliente' in body):
            nf._cliente = body['cliente']
        if ('itens' in body):
            nf._itens = body['itens']

        listaNF.append(nf)
        return geraResponse(200, "produto", nf.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "produto", {}, "Erro ao atualizar")

@app.route('/notafiscal/delete/<int:id>', methods=['DELETE'])
def delNF(id):
    nf = listaNF[id]
    try:
        listaNF.remove(nf)
        return geraResponse(200, "notafiscal", nf.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "notafiscal", {}, "Erro ao deletar")

# ROTAS ITEM NOTA FISCAL

@app.route('/itensnf/<int:id>', methods=['GET'])
def verItensNF(id):
    try:
        itemnf = listaItens[id]
        itemnfJSON = itemnf.to_json()

        return geraResponse(200, itemnfJSON, 'Todos os itens da nota')
    except Exception as a:
        print(a)
        return geraResponse(400, 'itens', {}, 'ID inválido')

@app.route('/itemnf/<int:id>', methods=['GET'])
def verItemNF(id):
    itemnf = listaItens[id]
    itemnfJSON = itemnf.to_json()
    return geraResponse(200, "itemnotafiscal", itemnfJSON)

@app.route('/itemnf', methods=['POST'])
def addItemNF():
    body = request.get_json()
    try:
        itemnf = ItemNotaFiscal(quantidade=body["quantidade"], produto=['produto'], descricao=body["descricao"])
        listaItens.append(itemnf)
        return geraResponse(201, "itemnotafiscal", itemnf.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "itemnotafiscal", {}, "Erro ao cadastrar")

@app.route('/itemnf/<int:id>', methods=['PUT'])
def attItemNF(id):
    item = listaItens[id]
    body = request.get_json()
    try:
        if ('quantidade' in body):
            item._quantidade = body['quantidade']
        if ('descricao' in body):
            item._descricao = body['descricao']

        listaItens.append(item)
        return geraResponse(200, "itemnotafiscal", item.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "itemnotafiscal", {}, "Erro ao atualizar")

@app.route('/itemnf/delete/<int:id>', methods=['DELETE'])
def delItemNF(id):
    itemnf = listaItens[id]
    try:
        listaItens.remove(itemnf)
        return geraResponse(200, "itemnotafiscal", itemnf.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return geraResponse(400, "itemnotafiscal", {}, "Erro ao deletar")

if __name__ == '__main__':
    app.run(
        debug=True
    )

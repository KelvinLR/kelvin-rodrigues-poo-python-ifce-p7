from flask import Flask, request, flash, url_for, redirect, render_template
from cliente import Cliente

cl01 = Cliente(0, "Jose Maria", 100, '200.100.345-34', 'Pessoa física')
cl02 = Cliente(1, "Kelvin Rodrigues", 101, '072.406.301-00', 'Pessoa física')
cl03 = Cliente(2, "Raquel Maciel", 102, '232.443.334-82', 'Pessoa física')
cl04 = Cliente(3, "Yuri Santiago", 103, '543.891.592-41', 'Pessoa física')
cl05 = Cliente(4, "Pablo Silva", 104, '210.090.454-94', 'Pessoa física')

listClientes = [cl01, cl02, cl03, cl04, cl05]

app = Flask(__name__, template_folder='templates')
app.config['DEBUG'] = True

@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for cliente in listClientes:
        result += "<li>%s</li>" % str(cliente._nome)
    result += "</ul>"
    return result

@app.route('/usuario', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['_nome'] or not request.form['_codigo']:
            flash('Favor entrar todos os valores dos campos', 'error')
        else:
            cliente = listClientes(request.form['_nome'], request.form['_codigo'])
            listClientes(cliente)
            ## flash('Registro foi inserido com sucesso')
            return redirect(url_for('showUsuarios'))
    return render_template('form.html', title='Usuários')

@app.route('/usuario/del/<int:id>')
def delUsuario(id):
    result = "<h1>Exclusão de Registro</h1><br><ul>"
    cliente = listClientes[id]
    listClientes.remove(cliente)
    result += '<p>Usuário -> Id=' + str(cliente._id) + ' Excluido!</p>'
    return result

@app.route('/usuario/show/<int:id>')
def showUsario(id):
    cliente = listClientes[id]
    result = "<h1>Consulta a Registro</h1><br><ul>"
    result += "<p> Id=" + str(cliente._id) + "</p>"
    result += "<p> Nome="  + cliente._nome + "</p>"
    result += "<p> Codigo=" + str(cliente._codigo) + "</p>"
    return result

@app.route('/usuarios')
def showUsuarios():
    result =  '<h1>Usuários</h1><br><ul>'
    for cliente in listClientes:
        result += '<p>'
        result += 'Id=' + str(cliente._id)
        result += ' Nome=' + cliente._nome
        result += ' Codigo=' + str(cliente._codigo)
        result += '</p>'
    return result

if __name__ == '__main__':
    app.run()
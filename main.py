'''
* url_for * server para padronizar as urls das páginas, caso precise ser alteradas e
continuar funcionando, pois ao mensionar uma url, devemos usar {{ url_for('nome_da_funcao')}}
'''

from flask import Flask, render_template, url_for

# Serve para iniciar o flask
app = Flask(__name__)

lista_usuarios = ['Rodrigo', 'Ruan', 'Cintia', 'Delmar', 'Marcos']

# Rota para estipular em qual link a página estará disponível
@app.route("/")
# Função para regular o funcionamento da página, o que será exibido e como
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

# Para rodar a página somente pelo arquivo e não por importação
if __name__ == "__main__":
    app.run(debug=True) # debug=True faz com que o site seja atualizado conforme as alterações são feitas

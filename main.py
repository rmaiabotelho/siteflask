from flask import Flask, render_template

# Serve para iniciar o flask
app = Flask(__name__)

# Rota para estipular em qual link a página estará disponível
@app.route("/")
# Função para regular o funcionamento da página, o que será exibido e como
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

# Para rodar a página somente pelo arquivo e não por importação
if __name__ == "__main__":
    app.run(debug=True) # debug=True faz com que o site seja atualizado conforme as alterações são feitas

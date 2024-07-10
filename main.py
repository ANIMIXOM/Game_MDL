from flask import Flask, render_template

app = Flask(__name__)

@app.route('/game')
def game():
    return render_template("index.html")

@app.route('/')
def home():
    return "<a href='/game'>Переход...</a>"

@app.route("/end")
def end():
    return """<a href='/'>Повторить?</a>"""

if __name__ == '__main__':
    app.run(host="0.0.0.0")
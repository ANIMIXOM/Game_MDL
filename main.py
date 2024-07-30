from flask import Flask, render_template

app = Flask(__name__)


@app.route('/game/<index>')
def game(index):
    return render_template(f"index_{index}.html")


@app.route('/')
def home():
    return """<a href='/game/1'>LTZ</a>
    <a href='/game/3'>KABEL</a>"""


@app.route("/end")
def end():
    return """<a href='/'>Повторить?</a>"""


if __name__ == '__main__':
    app.run(host="0.0.0.0")

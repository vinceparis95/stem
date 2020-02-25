from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>y a  b a h a</h1>'

@app.route('/salam')
def user():
    return render_template('slime.html')

if __name__ == "__main__":

    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects/nba-trends')
def graph():
    return render_template('nba-trends.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/blog')
def blog():
    return render_template('blog/index.html', title='Blog')


@app.route('/projects')
def projects():
    return render_template('projects/index.html', title='Projects')


@app.route('/projects/nba-trends')
def nba_trends():
    return render_template('projects/nba-trends.html')


if __name__ == '__main__':
    app.run(debug=True)

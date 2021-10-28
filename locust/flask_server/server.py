from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return f'<h1>Hello, World!</h1>'


@app.route("/count_views")
def count_views(count=[0]):
    count[0] += 1
    return f'Запросов страницы: {str(count[0])}'


if __name__ == '__main__':
    app.run(host='localhost', debug=True)

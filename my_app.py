from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('welcome.html')
    #  return '<h1>Hello World!</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

# @app.route('/')
# @app.route('/jobs')
# def jobs():
#     return '<h1>Carrer Tracks</h1>'
#
#
# @app.route('/resources')
# def resources():
#     return'<h1>Resources</h1>'


if __name__ == '__main__':
    app.run(debug=True)

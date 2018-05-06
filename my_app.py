from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask.ext.wtf import Form
# from wtforms import StringField, SubmitField
# from wtforms.validators import Required


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('about.html')


@app.route('/concentrations')
def concentrations():
    return render_template('concentrations.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')


# class NameForm(Form):
#     name = StringField('What is your name?', validators=[Required()])
#     submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/')
# @app.route('/jobs')
# def jobs():
#     return '<h1>Carrer Tracks</h1>'
#
#
# @app.route('/resources')
# def resources():
#     return'<h1>Resources</h1>'

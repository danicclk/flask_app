from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/jobs')
def jobs():
	return '<h1>Carrer Tracks</h1>'

@app.route('/resources')
def resources():
	return '<h1>Resources</h1>'


if __name__ == '__main__':
	app.run(debug=True)
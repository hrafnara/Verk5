from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'h1>Hello World</h1><a href="/kauplisti/">kauplisti</a> <a href="/karfa/">Karfa</a>'

@app.route('/karfa/')
def karfa():
    return '<h3>halló</h3>'

@app.route('/kauplisti/')
def Kauplisti():
    '<h1>' gsda '</h1>'

if __name__ == "__main__":
	app.run(debug=True)

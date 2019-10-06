from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/Kauplisti/">Kauplisti</a> <a href="/Karfa/">Karfa</a>'

@app.route('Karfa')
def Karfa()
    return '<h3>halló</h3>'

@app.route('Kauplisti')
def Kauplisti()
    return <input type="submit" value = "Kaupa" />

if __name__ == "__main__":
	app.run(debug=True)

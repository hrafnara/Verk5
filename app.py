from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/Kauplisti/">Kauplisti</a> <a href="/Karfa/">Karfa</a>'

@app.route('Karfa')
def Karfa()
    pass

@app.route('Kauplisti')
def Kauplisti()
    return <input type="submit" value = "Kaupa" />

if __name__ == "__main__":
	app.run(debug=True)

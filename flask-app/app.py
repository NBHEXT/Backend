from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
	return "I will metamorph to a beautiful website later"


@app.route("/api/standings")
def standings():
	return "Some JSON about standings"


if __name__ == "__main__":
	app.run(debug=True)  # don't forget to change this line on production

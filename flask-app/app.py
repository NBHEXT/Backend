#!/usr/bin/env python3

from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def index():
	return "I will metamorph to a beautiful website later"


@app.route("/api/standings")
def standings():
	return jsonify({"result": "OK", 
                        "deltas": {
                                "TooSimple": 100500,
                                "Um_nik": -123123
                        }
                })


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)  # don't forget to change this line on production

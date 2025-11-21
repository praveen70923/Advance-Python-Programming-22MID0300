from flask import Flask
import random, webbrowser
from threading import Timer

app = Flask(__name__)

facts = [
    "Your heart beats around 100,000 times a day.",
    "Drinking water boosts your brain performance.",
    "Smiling can improve your mood instantly.",
    "Walking for 10 minutes improves mental clarity.",
    "Learning new things keeps your brain young."
]

@app.route('/')
def home():
    return (
        "<h1>🌟 Welcome to the Motivational Facts Generator</h1>"
        "<p>Visit <code>/fact</code> to receive a new motivational fact!</p>"
    )

@app.route('/fact')
def get_fact():
    return f"<h3>✨ {random.choice(facts)}</h3>"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5050/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, port=5050)

from flask import Flask
import plotly.graph_objects as go
import random, webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "<h2>Smart Water Level Monitoring System</h2>"
        "<p>Click here to view water levels: "
        "<a href='/water_levels'>/water_levels</a></p>"
    )

@app.route('/water_levels')
def water_levels():

    days = [f"Day {i}" for i in range(1, 31)]
    
    # Simulated IoT sensor data (in percentage)
    water_levels = [random.randint(30, 100) for _ in days]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days,
        y=water_levels,
        mode="lines+markers",
        name="Water Level (%)"
    ))

    fig.update_layout(
        title="🚰 Smart Water Level Monitoring (Daily Readings)",
        xaxis_title="Day",
        yaxis_title="Water Level (%)",
        template="plotly_dark"
    )

    return fig.to_html()


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5500/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True, port=5500)

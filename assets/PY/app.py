from pathlib import Path

from flask import Flask, jsonify, send_from_directory

from assets.PY.code import get_ins

PROJECT_ROOT = Path(__file__).resolve().parents[2]
app = Flask(__name__, static_folder=str(PROJECT_ROOT / "assets"), static_url_path="/assets")


@app.get("/")
def home():
    return send_from_directory(PROJECT_ROOT, "index.html")


@app.get("/api/insect")
def insect_of_the_day():
    insect = get_ins()
    if insect is None:
        return jsonify({"error": "Could not retrieve today's insect. Please try again later."}), 502
    return jsonify(insect)

if __name__ == "__main__":
    app.run(debug=True)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, jsonify
from emotion_detector.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text', '')
    if not text.strip():
        return jsonify({"error": "Please enter some text."}), 400
    result = emotion_predictor(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

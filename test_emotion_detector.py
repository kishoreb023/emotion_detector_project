import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from emotion_detector.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def get_emotion():
    text = request.args.get('textToAnalyze')
    if not text:
        return jsonify({"error": "Please provide 'textToAnalyze' parameter"}), 400
    
    result = emotion_predictor(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

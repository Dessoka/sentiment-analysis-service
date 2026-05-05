from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Sentiment Analysis Service",
        "status": "running"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not data or "text" not in data:
        return jsonify({"error": "Please provide a JSON body with a 'text' field."}), 400

    text = data["text"]

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Text must be a non-empty string."}), 400

    prediction = predict_sentiment(text)
    return jsonify({
        "input_text": text,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

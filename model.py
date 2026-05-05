from transformers import pipeline

# The model is loaded once when the application starts.
# This avoids reloading the model for every request.
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict_sentiment(text: str) -> dict:
    """
    Predict the sentiment of the provided text.

    Args:
        text: Input text from the user.

    Returns:
        A dictionary containing the predicted label and confidence score.
    """
    result = sentiment_analyzer(text)[0]

    return {
        "label": result["label"],
        "score": round(float(result["score"]), 4)
    }

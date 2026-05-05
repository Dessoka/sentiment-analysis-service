import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="Test the deployed sentiment analysis service.")
    parser.add_argument("text", help="Text to analyze")
    parser.add_argument(
        "--url",
        default="http://127.0.0.1:5000/predict",
        help="Prediction endpoint URL"
    )

    args = parser.parse_args()

    try:
        response = requests.post(args.url, json={"text": args.text}, timeout=30)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

if __name__ == "__main__":
    main()

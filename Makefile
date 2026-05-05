install:
	pip install -r requirements.txt

run:
	python app.py

test-home:
	curl http://127.0.0.1:5000/

test-predict:
	curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"text":"I love this service"}'

docker-build:
	docker build -t sentiment-analysis-service .

docker-run:
	docker run -p 5000:5000 sentiment-analysis-service

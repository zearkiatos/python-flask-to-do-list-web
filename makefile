install:
	pip install -r requirements.txt

deploy-gcp:
	gcloud app deploy app.yaml --project=${PROJECT}

docker-up:
	docker compose up --build -d

docker-dev-up:
	docker compose -f=docker-compose.develop.yml up --build

docker-down:
	docker compose down
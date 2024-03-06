APP_NAME=fastapi-proj-boilerplate
TAG=latest
PORT=8000

build:
	DOCKER_BUILDKIT=1 docker build . -t $(APP_NAME):$(TAG)

run:
	docker run --rm -p $(PORT):$(PORT) -it $(APP_NAME):$(TAG)

test:
	http get http://localhost:8000/health
	http get http://localhost:8000/users


k8s-run:
	skaffold dev --profile api-srv

APP_NAME=fastapi-proj-boilerplate
TAG=latest
PORT=8000
TARGET_PORT=80

build:
	DOCKER_BUILDKIT=1 docker build --tag=$(APP_NAME):$(TAG) .

run:
	docker run --rm -p $(PORT):$(TARGET_PORT) -it $(APP_NAME):$(TAG)

test:
	http get http://localhost/users

k8s-run:
	skaffold dev --profile api-srv

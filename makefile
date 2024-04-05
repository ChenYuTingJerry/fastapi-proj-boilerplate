APP_NAME=fastapi-proj-boilerplate
TAG=latest
PORT=8000
TARGET_PORT=80

build:
	DOCKER_BUILDKIT=1 docker build --tag=$(APP_NAME):$(TAG) .

run: build
	docker run --rm -p $(PORT):$(TARGET_PORT) -it $(APP_NAME):$(TAG)

test:
	http get http:localhost:3000/users

port-forward:
	kubectl port-forward svc/api-srv 3000:80

k8s-run:
	skaffold run --profile api-srv

k8s-clear:
	skaffold delete --profile api-srv

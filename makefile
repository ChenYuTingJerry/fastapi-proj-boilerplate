APP_NAME=fastapi-proj-boilerplate
TAG=latest
PORT=8000

build:
	DOCKER_BUILDKIT=1 docker build . -t $(APP_NAME):$(TAG)

run:
	docker run --rm -p $(PORT):$(PORT) -it $(APP_NAME):$(TAG)

test:
	http get http://localhost:8000
	http post http://localhost:8000/items/ name=John age=40

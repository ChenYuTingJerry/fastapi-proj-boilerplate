APP_NAME=fastapi-proj-boilerplate
TAG=latest
PORT=8000
TARGET_PORT=8000

build:
	DOCKER_BUILDKIT=1 docker build --tag=$(APP_NAME):$(TAG) .

run: build
	docker run --rm -p $(PORT):$(TARGET_PORT) -it $(APP_NAME):$(TAG)

test:
	http get localhost:$(PORT)/users


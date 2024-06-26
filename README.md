# fastapi-proj-boilerplate

## Prerequisites
- python 3.12 up
- [docker](https://docs.docker.com/desktop/install/mac-install/)
- (optional) [httpie](https://httpie.io/docs/cli/installation)
- (optional) [stern](https://github.com/stern/stern)

## Project structure

### /app
Application code.

### /app/main.py
It is the entry point of the application and loading the routes here.


### /app/routes
This folder contains the definitions of each route. Each route corresponds to a file.

### /app/domain
It contains the definitions or implementation of domain models, services and repositories for the domain business.

### /app/services
It contains the definitions and implementation of services for the specific business logic.  

### /app/domain/services
It contains the definitions and implementation of services for the specific domain logic.

### /app/domain/repository
It contains the definitions and implementation of repositories for communicating with data sources.

### /app/infra
It contains code related to infrastructure, such as database access, cache access, external services and domain repository implementation, etc.

## Run

### Docker
#### Build service

```shell
make build
```

#### Run service

```shell
make run
```

#### Test service

```shell
make test
```

### k8s
#### Build & run service

```shell
make k8s-run
```

#### Test service

```shell
make test
```

# fastapi-proj-boilerplate

## Prerequisites
- python 3.11 up
- [docker](https://docs.docker.com/desktop/install/mac-install/)
- (optional) [httpie](https://httpie.io/docs/cli/installation)

## Project structure

### /app
Application code.

### /app/main.py
It is the entry point of the application and loading the routes here.

### /app/api
Put the definitions of API endpoints.

### /app/api/routes
This folder contains the definitions of each route. Each route corresponds to a file.

### /app/domain
It contains the definitions or implementation of domain models, services and repositories for the domain business.

### /app/domain/services
It contains the definitions and implementation of services for the specific business logic.

### /app/domain/repositories
It contains the definitions and implementation of repositories for communicating with data sources.

### /app/infra
It contains code related to infrastructure, such as database access, cache access, external services, etc.

## Examples

### Build service

```shell
make build
```

### Run service

```shell
make run
```

### Test service

```shell
make test
```
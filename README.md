# fastapi-proj-boilerplate

## Prerequisites
- python 3.11 up
- [docker](https://docs.docker.com/desktop/install/mac-install/)
- (optional) [httpie](https://httpie.io/docs/cli/installation)

## Project structure
```
project/
│
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── item.py
│   │   │   └── ...
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── domain/
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repositories.py
│   │   │   └── services.py
│   │   └── infra/
│   │       ├── __init__.py
│   │       ├── database.py
│   │       └── ...
│   │
│   └── main.py
│
├── Dockerfile
│
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ...
│
└── tests/
    ├── __init__.py
    ├── unit/
    │   ├── __init__.py
    │   ├── test_user.py
    │   ├── test_item.py
    │   └── ...
    └── integration/
        ├── __init__.py
        ├── test_user_integration.py
        ├── test_item_integration.py
        └── ...
```
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
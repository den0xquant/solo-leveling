# Project Template

A minimal backend template.

## Tech Stack

- **Python 3.13**
- **FastAPI** (API framework)
- **PostgreSQL** (database)
- **Redis** (key/value db)
- **Docker** (containerization)
- **Traefik** (proxy)

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/)

### Development

Clone the repository and start the local stack with Docker Compose:

```bash
git clone git@github.com:den0xquant/template-microservice.git
cd template-microservice
docker compose watch
```

Backend, JSON based web API based on OpenAPI: [http://localhost:8000](http://localhost:8000)

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): [http://localhost:8000/docs](http://localhost:8000/docs)

Adminer, database web administration: - [http://localhost:8080](http://localhost:8080)

Traefik UI, to see how the routes are being handled by the proxy: [http://localhost:8090](http://localhost:8090)

## License

MIT

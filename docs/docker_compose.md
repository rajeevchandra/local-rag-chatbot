# Docker Compose Cheat Sheet

Quick reference for managing multi-container apps.

## Commands

- `docker-compose up` – Start services
- `docker-compose down` – Stop and clean up
- `docker-compose logs -f` – Follow logs
- `docker-compose ps` – Check status

## Example

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  db:
    image: postgres
```
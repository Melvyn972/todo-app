# Todo List Application avec CI/CD

## Configuration des Secrets GitHub

Pour utiliser la pipeline, configurez ces secrets :
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `SERVER_IP`
- `SERVER_USERNAME`
- `SERVER_SSH_KEY`

## Développement Local

### Prérequis
- Docker
- Docker Compose

### Lancer l'application en développement
```bash
docker-compose up --build
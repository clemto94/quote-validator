# Quote Validator

Un service de validation de devis.

## Prérequis

- Python 3.12 ou supérieur
- Poetry (gestionnaire de dépendances Python)
- Docker (optionnel)
- Docker Compose (optionnel)

## Installation

1. Cloner le repository :
```bash
git clone [URL_DU_REPO]
cd quote-validator
```

2. Installer les dépendances avec Poetry :
```bash
poetry install
```

## Tests

Pour exécuter les tests unitaires :

```bash
poetry run pytest
```

## Déploiement avec Docker

### Construction de l'image

```bash
docker build -t quote-validator .
```

### Exécution du conteneur

```bash
docker run -p 8000:8000 quote-validator
```

Le service sera accessible à l'adresse : http://localhost:8000

### Utilisation de Docker Compose

Pour démarrer le service avec Docker Compose :

```bash
docker-compose up
```

Pour démarrer en arrière-plan :

```bash
docker-compose up -d
```

Pour arrêter les services :

```bash
docker-compose down
```

Pour reconstruire l'image et redémarrer les services :

```bash
docker-compose up --build
```

## Développement

Pour lancer le serveur en mode développement :

```bash
poetry run uvicorn main:app --reload
```

## Documentation API

Une fois le serveur lancé, la documentation de l'API est disponible aux adresses suivantes :
- Swagger UI : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc 
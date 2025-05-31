# ERP/CRM Starter

## Start het project:
```bash
docker-compose up --build
```

Frontend: http://localhost:5173  
Backend: http://localhost:8000/docs

## GitHub Actions CI/CD
1. Voeg je `RAILWAY_TOKEN` toe aan je GitHub repo onder Settings > Secrets.
2. Bij elke push naar `main` wordt de app automatisch gedeployed naar Railway.

## Auth0-integratie (voor later)
1. Voeg Auth0 client ID/secret toe aan `.env`
2. Gebruik Auth0 SDK in frontend (bijv. `@auth0/auth0-react`)
3. Beveilig FastAPI routes met JWT validatie

#!/bin/bash

echo "✅ Starten van lokale ERP/CRM stack met Docker..."

# Zorg dat je in de juiste map zit
cd "$(dirname "$0")"

# Docker Compose build + up
docker-compose up --build

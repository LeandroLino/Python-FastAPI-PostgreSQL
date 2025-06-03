#!/bin/bash

echo "🚀 Iniciando projeto FastAPI + PostgreSQL..."

docker-compose up --build

echo "✅ Projeto iniciado!"
echo "🌐 API disponível em: http://localhost:8000"
echo "📋 Documentação em: http://localhost:8000/docs"
echo "🏥 Health check em: http://localhost:8000/health"

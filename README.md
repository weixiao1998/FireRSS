# FireRSS
🔥 A free, open source, self-host, web-based RSS reader and aggregator

## Architecture
#### frontend
- vue3

#### backend
- flask

## Develop
1. `make install-dev && make run-backend`: setup backend
2. `cd Docker && docker compose -f docker-compose.dev.yml --env-file .dev.env up -d`: setup middleware/db
3. `cd frontend && npm install && npm run dev`: setup frontend

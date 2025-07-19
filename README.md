# FireRSS
🔥 A free, open source, self-host, web-based RSS reader and aggregator

## Architecture
#### frontend
- vue3

#### backend
- fastapi

## Develop
0. pre install
    - `python`: >=3.13
    - `node`: >=22.17.1
    - `pnpm`: node package manager
1. setup backend: `make install-dev`
2. setup middleware/db: `cd Docker && docker compose -f docker-compose.dev.yml --env-file dev.env up -d`
3. setup frontend: `cd frontend && pnpm install`
4. change config: `cd backend/fire_rss/config && cp config.dev.py config.py && vim config.py`
5. run dev
    - `make run-backend`
    - `pnpm run dev`

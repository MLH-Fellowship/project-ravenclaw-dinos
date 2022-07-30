#!/bin/bash
cd MLHPortfolio
git fetch && git reset origin/main --hard # get any Github updates

# spin containers down to prevent out of memory issues on our VPS instances
docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build

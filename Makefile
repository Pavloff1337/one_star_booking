# ----------------------------
# Настройки
# ----------------------------

DEV_COMPOSE = docker compose -f docker-compose.dev.yml
PROD_COMPOSE = docker compose -f docker-compose.prod.yml

# ----------------------------
# Команды для разработки
# ----------------------------

dev-up:
	$(DEV_COMPOSE) up --build

dev-down:
	$(DEV_COMPOSE) down -v

dev-logs:
	$(DEV_COMPOSE) logs -f web

# ----------------------------
# Команды для продакшена
# ----------------------------

prod-up:
	$(PROD_COMPOSE) up -d --build

prod-down:
	$(PROD_COMPOSE) down -v

prod-logs:
	$(PROD_COMPOSE) logs -f web

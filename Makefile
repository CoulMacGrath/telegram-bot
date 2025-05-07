restart:
	docker compose restart
build: 
	docker compose up -d --build
logs:
	docker compose logs -f faqup-bot

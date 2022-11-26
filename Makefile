build:
	poetry build

install:
	poetry install

lock:
	poetry lock

update:
	poetry update

start:
	poetry run bot

lint:
	poetry run flake8 telegram_bot

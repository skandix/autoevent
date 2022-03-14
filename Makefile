docker:
	tag="$(git rev-parse --short HEAD)"
	docker build -t autoevent:$tag .
	docker run autoevent:$tag --rm


install:
	pipenv install && pipenv shell


dev:
	pipenv install --dev && pipenv shell


format:
	pipenv run black .

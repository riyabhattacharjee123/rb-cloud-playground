build:
	docker build -t cloud-playground:dev .

run:
	docker run --rm -p 8000:8000 cloud-playground:dev

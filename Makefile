install:
	pip install -r requirements.txt

check:
	flake8 --ignore=E501 --per-file-ignores="__init__.py:F401"

format:
	black .

run:
	python main.py ${args}

test:
	python test.py ${args}

down:
	python down.py

up:
	python up.py

fresh:
	make down
	make up
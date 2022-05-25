install:
	poetry install
	
brain-games: 
	poetry run brain-games

brain-progression:
	poetry run brain-progression

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-prime:
	poetry run brain-prime

sympy:
	poetry run sympy

brain-gcd:
	poetry run brain-gcd

prompt:
	poetry add prompt

build:
	poetry build

publish:
	poetry publish --dry-run

package-install: 
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 brain_games

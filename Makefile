startlinters:
	black . && isort . && pylint src/ && mypy src/

startpytest:
	pytest
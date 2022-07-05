VENV = .venv
PIP = $(VENV)/Scripts/pip
PYTHON = $(VENV)/Scripts/python

init: venv/Scripts/activate requirements.txt
	$(PIP) install -r requirements.txt

# run: venv/bin/activate
# 	./venv/bin/python3 <my-python3>

venv/Scripts/activate: 
	/c/Users/User/anaconda3/python -m venv $(VENV)

test: init requirements-test.txt tests/
	$(PIP) install -r requirements-test.txt
	py.test tests/

find:
	find . -type d -name "__pycache__" -or -type d -name "$(VENV)"

clean: find
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete -or -type d -name "$(VENV)" -delete
	rm -r ".pytest_cache"

.PHONY: init test clean
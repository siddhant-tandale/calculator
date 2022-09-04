create-venv:
	python3 -m pip install --upgrade pip
	pip3 install virtualenv

	test -d calc-venv || virtualenv -p python3 calc-venv

install-dependencies:
	. calc-venv/bin/activate; pip install pandas plotly numpy
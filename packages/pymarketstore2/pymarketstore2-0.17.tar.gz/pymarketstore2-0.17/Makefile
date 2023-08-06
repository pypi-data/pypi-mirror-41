all:
	python3 setup.py build && python3 setup.py install
pack:
	python3 setup.py sdist bdist_wheel && python3 -m twine upload dist/*

install: all

unittest: all
	pytest -s -v -q ./pymarketstore/test_client.py

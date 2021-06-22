install: build
	python setup.py install

build:
	python setup.py build_ext --inplace	

uninstall:
	python setup.py install --record .manifest.txt
	for i in $$(less .manifest.txt); do rm -f $$i; done
	rm .manifest.txt


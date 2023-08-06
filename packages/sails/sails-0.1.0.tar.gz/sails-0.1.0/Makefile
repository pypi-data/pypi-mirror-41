# vim: set noexpandtab ts=4 sw=4:

# There must be a nicer way to do this
PYTHONARCH=$(shell python utils/pythonarch)
PYTHONARCH3=$(shell python3 utils/pythonarch)

BINS=$(shell python setup.py --list-scripts)

DEVELVERSION ?= 0.DEVEL.$(shell date +%Y%m%d%H%M)
RELEASEVERSION ?= $(DEVELVERSION)

all: all-python2 all-python3

doc: doc-html

doc-html: all
	# For some reason, we have issues with figure generation when running this
	# the first time
	# TODO: Debug and fix this
	python setup.py build_sphinx
	python setup.py build_sphinx

clean:
	python setup.py clean
	# Stupid python setuptools don't even clean the build directory
	rm -fr build
	rm -fr doc/build
	rm -fr sails.egg-info

test2: all-python2
	cd build && PYTHONPATH=lib$(PYTHONARCH)/:$${PYTHONPATH} nosetests -c ../nose.cfg lib$(PYTHONARCH)/sails

testv2: all-python2
	cd build && PYTHONPATH=lib$(PYTHONARCH)/:$${PYTHONPATH} nosetests --with-coverage --cover-package=sails -c ../nose.cfg -v lib$(PYTHONARCH)/sails

test3: all-python3
	cd build && PYTHONPATH=lib$(PYTHONARCH3)/:$${PYTHONPATH} nosetests3 -c ../nose.cfg lib$(PYTHONARCH3)/sails

testv3: all-python3
	cd build && PYTHONPATH=lib$(PYTHONARCH3)/:$${PYTHONPATH} nosetests3 --with-coverage --cover-package=sails -c ../nose.cfg -v lib$(PYTHONARCH3)/sails

all-python2:
	python setup.py build

all-python3:
	python3 setup.py build

install-python2: all-python2
	python setup.py install --prefix=$(DESTDIR)/usr

install-python3: all-python3
	python3 setup.py install --prefix=$(DESTDIR)/usr

.PHONY: clean doc doc-html all all-python2 all-python3 test2 testv2 test3 testv3 pythonarch install-python2 install-python3

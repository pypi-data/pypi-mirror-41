#!/bin/bash
DIRECTORY=`pwd`/virtualenv
if [ ! -d "$DIRECTORY" ]; then
	echo "Creating new enviroment"
    easy_install --user pip
    python -m pip install --user virtualenv
	python -m virtualenv $DIRECTORY
	source $DIRECTORY/bin/activate
	pip install pika cernservicexml
	pip install --extra-index-url https://lhcb-pypi.web.cern.ch/lhcb-pypi/simple/ --trusted-host lhcb-pypi.web.cern.ch lbmessaging
fi

source $DIRECTORY/bin/activate
python setup.py install

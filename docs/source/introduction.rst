Installation
************

Mist.ansible consists of custom modules for mist.io services. In order to use then you have to have ``andsible`` and
``mist.client`` packages installed.

Install using pip
=================
This is the easiest way to obtain the mist ansible modules. What the package does is find where ansible is installed
and patch the mist modules into the share folder of the package ansible::

    pip install mist.ansible

Clone from Github
=================
You can manually patch the mist modules into your installation of ansible. You have to find where the ansible share
folder is and patch the modules::

    git clone https://github.com/mistio/mist.ansible
    cd mist.ansible
    cp -r mist.modules /bin/ansible/share/


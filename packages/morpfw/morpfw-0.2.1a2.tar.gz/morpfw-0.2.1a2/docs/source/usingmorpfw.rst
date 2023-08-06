===========
Using Morp
===========

Bootstrapping a new project
============================

The recommended way to install morpfw is to use 
`pipenv <http://pipenv.rtfd.org>`_, or you can also use pip or virtualenv.

If you don't have pipenv installed yet, do:

.. code-block:: bash

   sudo pip install pipenv>=2018.11.26

Lets create a new project. You can initialize new project using 
``cookiecutter-morpfw``:

.. code-block:: bash

   sudo pip install cookiecutter
   cookiecutter https://github.com/morpframework/cookiecutter-morpfw


And start your project using:

.. code-block:: bash

   cd $PROJECTNAME/ # replace with your project directory name
   pipenv install .
   pipenv run morpfw start -s settings.yml


Creating a simple CRUD model
===================================

.. literalinclude:: exampleapp.py
   :language: python

save as ``pages.py``, and lets start the application::

   pipenv run morpfw start -s settings.yml


Accessing API
==============

Morp API endpoints requires authentication (we haven't figure out how to make
it optional yet), and the default authentication policy is to acquire current
username from ``user.id`` GET parameter.

.. code-block:: python

   >>> import requests
   >>> resp = requests.get('http://localhost:5000/pages?user.id=foo')
   >>> resp.json()
   {...}

Lets create a page

.. code-block:: python

   >>> resp = requests.post('http://localhost:5000/pages/?user.id=foo', json={
   ...     'body': 'hello world'
   ... })
   >>> objid = resp.json()['data']['uuid']
   >>> resp = requests.get('http://localhost:5000/pages/%s?user.id=foo' % objid)
   >>> resp.json()
   {...}

Lets update the body text

   >>> resp = requests.patch(
   ...   'http://localhost:5000/pages/%s?user.id=foo' % objid, json={
   ...       'body': 'foo bar baz'
   ... })
   >>> resp = requests.get('http://localhost:5000/pages/%s?user.id=foo' % objid)
   >>> resp.json()
   {...}

Lets do a search

   >>> resp = requests.get('http://localhost:5000/pages/+search')
   >>> resp.json()
   {...}

Lets delete the object

   >>> resp = requests.delete('http://localhost:5000/pages/%s?user.id=foo' % objid)
   >>> resp.status_code
   200

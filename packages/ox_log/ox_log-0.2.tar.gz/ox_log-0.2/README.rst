Introduction
============

The ``ox_log`` python package is used to do some very simple,
lightweight log analysis (especially in the flask web framework).

If you want to do something complicated, there are lots and lots of log
parsing, sending, and visualization tools. Unfortunately, some of those
systems take some time to understand and setup.

If you just want a very simple, easy to setup system to show some
information from your logs, then ``ox_log`` is for you!

Quickstart
==========

First install ``ox_log`` using something like ``pip install ox_log`` or
however you typically install python packages.

with flask
----------

If you are using flask, you can add ``ox_log`` to your project simply by
creating an instance of the ``ox_log`` blueprint and registering. For
example, you could do something like

.. code:: python

    from ox_log.ui.flask_web_ui.ox_log import views as ox_log_views
    from import ox_log.core import loader

    ox_log_views.register(APP, readers={
        'pickle_reader': loader.PickleReader,
        'file_reader': loader.FileReader},
                          topics={
        '/tmp/log_items.pkl': 'pickle_reader',
        '/tmp/log.txt': 'file_reader'}

The first line will import the ``ox_log`` views so routes will be
registered correctly. The second line imports the loader. The final line
registers the ``ox_log`` blueprint and defines a couple of readers to
read pickled data and text log files along with some specific topics.
The ``APP`` variable is the flask app.

With the configuration above, you can point your browser to ``/ox_log``
after starting your flask app and refresh your data, view your logs, add
or drop topics and so on.

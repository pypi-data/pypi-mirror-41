wsgi_lineprof
=============
.. image:: https://badge.fury.io/py/wsgi-lineprof.svg
   :target: https://pypi.python.org/pypi/wsgi-lineprof/
   :alt: PyPI version
.. image:: https://img.shields.io/pypi/pyversions/wsgi_lineprof.svg
   :target: https://pypi.python.org/pypi/wsgi-lineprof/
   :alt: PyPI Supported Python Versions
.. image:: https://travis-ci.org/ymyzk/wsgi_lineprof.svg?branch=master
   :target: https://travis-ci.org/ymyzk/wsgi_lineprof
   :alt: Build Status
.. image:: https://ci.appveyor.com/api/projects/status/cjhft69q2hq1gdoj?svg=true
   :target: https://ci.appveyor.com/project/ymyzk/wsgi-lineprof
   :alt: AppVeyor Build Status

**wsgi_lineprof** is a WSGI middleware for line-by-line profiling.

wsgi_lineprof has the following features:

* *WSGI middleware*: It can be integrated with any WSGI-compatible applications and frameworks including Django, Pyramid, Flask, Bottle, and more.
* *Easily pluggable*: All configurations for profiling in one place. Users don't need to make any changes to their application.

wsgi_lineprof is *not recommended to be used in production environment* because of the overhead of profiling.

At a Glance
-----------
You can use wsgi_lineprof as a WSGI middleware of existing applications.

::

   $ pip install wsgi_lineprof

Example usage with Bottle:

.. code-block:: python

   import time

   import bottle
   from wsgi_lineprof.middleware import LineProfilerMiddleware

   app = bottle.default_app()


   @app.route('/')
   def index():
       time.sleep(1)
       return "Hello world!!"

   if __name__ == "__main__":
       # Add wsgi_lineprof as a WSGI middleware!
       app = LineProfilerMiddleware(app)
       bottle.run(app=app)

Run the above script to start web server, then access http://127.0.0.1:8080.

wsgi_lineprof writes results to stdout every time an HTTP request is processed by default.
You can see the output like this in your console:

::

   ... (snip) ...

   File: ./app.py
   Name: index
   Total time: 1.00518 [sec]
     Line      Hits         Time  Code
   ===================================
        9                         @app.route('/')
       10                         def index():
       11         1      1005175      time.sleep(1)
       12         1            4      return "Hello world!!"

   ... (snip) ...

Results contain many other functions, you can remove unnecessary results by
using *filters*.

Requirements
------------
* Python 2.7
* Python 3.4
* Python 3.5
* Python 3.6
* Python 3.7

Filters
-------
You can get results from specific files or sort results by using filters.
For example, use ``FilenameFilter`` to filter results with ``filename``
and use ``TotalTimeSorter`` to sort results by ``total_time``.

.. code-block:: python

    import time

    import bottle
    from wsgi_lineprof.filters import FilenameFilter, TotalTimeSorter
    from wsgi_lineprof.middleware import LineProfilerMiddleware

    app = bottle.default_app()


    def get_name():
        # Get some data...
        time.sleep(1)
        return "Monty Python"

    @app.route('/')
    def index():
        name = get_name()
        return "Hello, {}!!".format(name)

    if __name__ == "__main__":
        filters = [
            # Results which filename contains "app2.py"
            FilenameFilter("app2.py"),
            # Sort by total time of results
            TotalTimeSorter(),
        ]
        # Add wsgi_lineprof as a WSGI middleware
        app = LineProfilerMiddleware(app, filters=filters)

        bottle.run(app=app)

Run the above script to start web server, then access http://127.0.0.1:8080.
You can see results in stdout.

::

    $ ./app2.py
    Bottle v0.12.10 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8080/
    Hit Ctrl-C to quit.

    Time unit: 1e-06 [sec]

    File: ./app2.py
    Name: index
    Total time: 1.00526 [sec]
      Line      Hits         Time  Code
    ===================================
        15                         @app.route('/')
        16                         def index():
        17         1      1005250      name = get_name()
        18         1           11      return "Hello, {}!!".format(name)

    File: ./app2.py
    Name: get_name
    Total time: 1.00523 [sec]
      Line      Hits         Time  Code
    ===================================
        10                         def get_name():
        11                             # Get some data...
        12         1      1005226      time.sleep(1)
        13         1            4      return "Monty Python"

    127.0.0.1 - - [30/Nov/2016 17:21:12] "GET / HTTP/1.1" 200 21

There are more useful filters in ``wsgi_lineprof.filters``. Examples:

* ``FilenameFilter("(file1|file2).py", regex=True)``
* ``NameFilter("(fun1|fun2).py", regex=True)``

Stream
------
By using ``stream`` option, you can output results to a file.
For example, you can output logs to ``lineprof.log``.

.. code-block:: python

    f = open("lineprof.log", "w")
    app = LineProfilerMiddleware(app, stream=f)
    bottle.run(app=app)

Async Stream
------------
By using ``async_stream`` option, wsgi_lineprof starts a new thread for writing results.
This option is useful when you do not want the main thread blocked for writing results.

.. code-block:: python

    # Start a new thread for writing results
    app = LineProfilerMiddleware(app, async_stream=True)
    bottle.run(app=app)

Accumulate Mode
---------------
By default, wsgi_lineprof writes results every time a request is processed.
By enabling ``accumulate`` option, wsgi_lineprof accumulate results of all requests and writes the result on interpreter termination.

.. code-block:: python

    app = LineProfilerMiddleware(app, accumulate=True)
    bottle.run(app=app)

Links
-----
* `GitHub: ymyzk/wsgi_lineprof <https://github.com/ymyzk/wsgi_lineprof>`_
* `WSGI ミドルウェアとして使えるラインプロファイラを作った話 – ymyzk’s blog <https://blog.ymyzk.com/2016/12/line-profiler-as-a-wsgi-middleware/>`_
* `Python ウェブアプリのためのプロファイラ wsgi_lineprof の仕組み – ymyzk’s blog <https://blog.ymyzk.com/2018/12/how-wsgi-lineprof-works/>`_

Special Thanks
^^^^^^^^^^^^^^
This project uses code from the following project:

* `rkern/line_profiler <https://github.com/rkern/line_profiler>`_

This project is inspired by the following project:

* `kainosnoema/rack-lineprof <https://github.com/kainosnoema/rack-lineprof>`_

wsgi_lineprof is integrated with the following projects:

* `kobinpy/wsgicli <https://github.com/kobinpy/wsgicli>`_
* `denzow/wsgi_lineprof_reporter <https://github.com/denzow/wsgi_lineprof_reporter>`_

wsgi_lineprof is mentioned in the following entries:

* `1日目 Peter Wang氏キーノート，変数アノテーション，自然言語処理，PythonでWebセキュリティ自動化～新企画「メディア会議」に注目：PyCon JP 2017カンファレンスレポート｜gihyo.jp … 技術評論社 <http://gihyo.jp/news/report/01/pyconjp2017/0001?page=4>`_
* `DjangoにDjangoミドルウェアとWSGIミドルウェアを組み込んでみた - メモ的な思考的な <http://thinkami.hatenablog.com/entry/2016/12/13/061856>`_
* `PythonのWSGIラインプロファイラを試してみた(wsgi_lineprof) - [Dd]enzow(ill)? with DB and Python <http://www.denzow.me/entry/2017/09/18/162154>`_
* `PythonのWSGIラインプロファイラの結果を使いやすくしてみた(wsgi_lineprof_reporter) - [Dd]enzow(ill)? with DB and Python <http://www.denzow.me/entry/2017/09/20/233219>`_
* `Server-side development — c2cgeoportal documentation <https://camptocamp.github.io/c2cgeoportal/master/developer/server_side.html>`_

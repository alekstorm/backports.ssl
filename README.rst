-------------
backports.ssl
-------------

What is it?
-----------

It's the Python 3.4 standard ``ssl`` module API implemented on top of
pyOpenSSL::

    import backports.ssl as ssl
    import socket

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_REQUIRED

    conn = context.wrap_socket(socket.socket(socket.AF_INET))
    conn.connect(('google.com', 443))
    print conn.getpeercert()
    conn.close()

Why?
----

Because the latest web technologies should be available to those running older
versions of Python.

Isn't this obsoleted by `PEP 466`_?
-----------------------------------

If you're on Python 2.7, then probably. But PEP 466 doesn't cover Python 2.6,
3.2, or 3.3, and the ``ssl.RAND_*()`` functions are explicitly out of scope.
This package supports it all.

How do I use it with third-party libraries?
-------------------------------------------

Monkey-patching support is included a la `gevent`_::

    import backports.ssl.monkey as monkey
    import requests

    monkey.patch()
    requests.get('https://google.com')


Why am I getting ``AttributeError``\ s for newer features?
------------------------------------------------------

Like the standard ``ssl`` module, certain attributes will not be available if
your OpenSSL does not support them. See `Installing OpenSSL`_ for instructions.

Installing OpenSSL
------------------

TODO
----

- Verify that we play nicely with gevent's monkey-patching.
- Backport and pass the standard Python ``ssl`` test suite.
- If not that, automate testing against hyper, urllib3, requests, and Tornado
  test suites.
- Use the bundled 3.x OpenSSL, if available and newer than the default.

.. _`PEP 466`: http://legacy.python.org/dev/peps/pep-0466
.. _`gevent`: http://gevent.org

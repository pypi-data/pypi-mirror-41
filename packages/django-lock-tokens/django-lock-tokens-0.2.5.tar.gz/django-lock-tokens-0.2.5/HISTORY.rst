.. :changelog:

History
-------

0.2.5 (2019-02-07)
^^^^^^^^^^^^^^^^^^

- Fix issue #10_

.. _10: https://github.com/rparent/django-lock-tockens/issues/10

0.2.4 (2018-11_30)
^^^^^^^^^^^^^^^^^^
- The HTTP API endpoint to get token information now returns the token information even when it has expired, because it is still valid to use (see this_)

.. _this: https://github.com/rparent/django-lock-tokens#how-it-works

0.2.3 (2018-10-31)
^^^^^^^^^^^^^^^^^^
- Fixes ``LockableModel`` for Python 2.7

0.2.2 (2018-10-31)
^^^^^^^^^^^^^^^^^^
- Fixes ``LockableModel`` to allow to use it as a proxy

0.2.1 (2018-10-04)
^^^^^^^^^^^^^^^^^^
- Fixes ``LockToken.save`` method to prevent potential transaction errors
- Adds a template tag to handle lock on the client side when overriding default ``change_form_template`` in ``LockableModelAdmin``
- Better handling of invalid lock token strings (see discussion here_) to prevent overwriting

.. _here: https://github.com/rparent/django-lock-tokens/issues/6

0.1.4 (2017-09-07)
^^^^^^^^^^^^^^^^^^

- Adds a ``created`` field to the ``LockToken`` model


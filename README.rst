Flask
=====

For demo purposes, the USSD Flask app runs on Flask-Ngrok, this automatically gives a you a ngrok link that shall be used as the callback URL. 
Copy the link given (https) and paste it at the callback for the USSD code.
After the testing is done, we shall now deploy our system using apache and setup the database, instructions to be provided on the next commit.


Installing and Running.
-----------------------

Install and update using `pip`_:

.. code-block:: text

    $ pip3 install -U Flask

.. _pip: https://pip.pypa.io/en/stable/quickstart/


.. code-block:: text

    $ pip3 install flask-ngrok


.. code-block:: text

$ pip3 install flask-ngrok

.. code-block:: text

    $ flask run
      * Runs on "NGROK LINK PROVIDED" (Press CTRL+C to quit)



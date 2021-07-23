Flask USSD
==========

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

    $ pip3 install flask-ngrok (SKIP INSTALLATION IF YOU WISH TO RUN ON SERVER)


.. code-block:: text

$ pip3 install flask-ngrok (SKIP STEP IF YOU WISH TO RUN ON SERVER)

.. code-block:: text

    $ flask run
      * Runs on "NGROK LINK PROVIDED" (Press CTRL+C to quit)

Configure and Enable a New Virtual Host.
-----------------------------------------

Issue the command below to:

.. code-block:: text

    $ sudo nano /etc/apache2/sites-available/FlaskApp.conf

Add the following lines of code to the file to configure the virtual host. Be sure to change the ServerName to your domain or cloud server's IP address:

``
<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

``

Save and close the file.

Enable the virtual host with the following command:

.. code-block:: text

    $ sudo a2ensite FlaskApp
    
Configure the .wsgi File by entering the python path and the path for flask conf file

Restart apache

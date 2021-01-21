# T9107_SW1000 Software Delivery Server

This repo contains the sourcecode of the luetze sofware delivery system.
The system uses the python django web framework to provide a human readable
website as well as a machine readable rest api.

## Interfaces

The LSD system shall be accessible via a rest api to register new builds during
the ci pipeline run.

The LSD system shall be accessible via a standard web browser to access the
build results and software documentation.

The LSD system shall be accessible via a rest api to download software binaries
to the production systems during manufacturing.

## Installation

Clone this Repo wherever you want your tools to be.

### Requirements

Install the following requirements (should work on an Ubuntu 18.04 system)

Python 3.x
```
sudo apt-get install python3 python3-venv python3-pip
```

Python Virtualenvwrapper
```
python3 -m pip install virtualenvwrapper
```
Add shell extensions to your .bashrc
```
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
. /home/<your username>/.local/bin/virtualenvwrapper.sh
```

For python-ldap authentication OpenLDAP is needed:
```
sudo apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
```

For the postgresql server (used as production database + needed to install python requirements):
```
sudo sudo apt-get install postgresql postgresql-contrib libpq-dev
```

Generate a new virtual environment using:
```
mkvirtualenv -p python3 t9107_sw1000_lsd
```

And switch to this Venv to work on it:
```
workon t9107_sw1000_lsd
```

The correct setup of all required Packages is acomplished by pip-tools, to install it run the following command in your venv:
```
python -m pip install pip-tools
```

all required python packets can be installed using:
```
pip-compile
pip-sync
```

### credentials
The passwords and the django secret key are held by a json file outside of this repository.
The file needs to be in the same directory as the repository.
The filename has to be ``config.json``
The file has to provide these variables:
```
{
    "lsd_secret_key": "<django secret key - used for security features>",
    "lsd_dbpass": "<password of the db or "" in case of internal sqlite db>",
    "lsd_ldappass": "<password of the luetze ldap user ricoh.ldap@luetze.int>",
    "lsd_testserver": true/false, (optional - true: django uses an internal sqlite db - for test/develop purpose)
    "lsd_debug": true/false (optional - if not set it will be set through the lsd_testserver)
}
```

If this file is not found the LSD defaults to testserver state without LDAP
access and uses the internal sqlite dummy database.

### database

The productive LSD system uses a postgres sql database.
A postgresql database has to be setup with name 'lsd' and a user named 'lsd'

#### Database setup:

Create user and databse
```
sudo su - postgres
createuser -P lsd
createdb -O lsd lsd
exit
```

Export and import data
```
# create dump
pg_dump -C -h localhost -U lsd lsd > lsd.dump

# apply dump
psql -h localhost -U lsd lsd < lsd.dump
```

The password of the lsd user must match the one configured in the config.json
file

If you want to setup a test instance the included sqlite database will be used.

### static files

Django needs some static files to be provided to the client.
In the current implementation all software and documentation is provided as
static files as well.

The static files are kept in the single django apps in this repository.
For production systems they have to be copied and held on the system.

run:
```
sudo python djangoProject/manage.py collectstatic
```

This will collect all static files in the repository and merges it with the
static files on the file system of the production machine.

When a file needs to be accesed, make sure to access the path like: 
    cur_dir = os.path.dirname(__file__)
    path    = os.path.join(cur_dir, "../media/"+name_of_file)

## Usage

### Running the server

Start Django

Start a Shell at the top level of the repository:

```
python manage.py runserver 0:8080
```

Now you can access the running LSD server(or testserver) by connecting with a
browser of your choice.

### Testserver admin credentials:

You can access the admin console of the Testserver with at /admin with the
following credentials.

```
username: admin
pw:       1234
```

### Debugging the server

The repository comes with .vscode directory specifying a simple debug
configuration.
Just open the repository as directory in vscode and hit F5.

You need to have the python plugin installed (on both your host and your ssh target (if used)).
You have to choose the correct python interpreter first (the virtualenv).

After all that the server should start in a debug context and you can simply add
breakpoints anywhere you like.

### WSGI configuration - production server

To run the LSD (or any django app) in a production environment you can run it
as WSGI service.

See the following demo config for an apache2 webserver:

```
<VirtualHost *:80>
        ServerAdmin stefan.strobel@luetze.de
        ServerName software.luetze.int
        ServerAlias www.software.luetze.int

        Redirect permanent / https://software.luetze.int/
</VirtualHost>

<VirtualHost *:443>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin stefan.strobel@luetze.de
        ServerName software.luetze.int
        ServerAlias www.software.luetze.int

        SSLEngine on
        SSLCertificateFile      /etc/apache2/sw_int_ssl_certs/sw.luetze.int.crt
        SSLCertificateKeyFile   /etc/apache2/sw_int_ssl_certs/sw.luetze.int.key
        SSLCertificateChainFile /etc/apache2/sw_int_ssl_certs/DE-CA-01-CA.pem

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf

        Alias /static /var/lsd/static
        <Directory /var/lsd/static>
                Require all granted
        </Directory>

        <Directory /home/stefan/gitRepos/T9107/t9107_sw1000_lsd/djangoProject/djangoProject>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIScriptAlias / /home/stefan/gitRepos/T9107/t9107_sw1000_lsd/djangoProject/djangoProject/wsgi.py
        WSGIDaemonProcess lsd_app python-path=/home/stefan/gitRepos/T9107/t9107_sw1000_lsd/djangoProject python-home=/home/stefan/.virtualenvs/t910$
        WSGIProcessGroup lsd_app

</VirtualHost>
```

Please mind:

- grant access to the static directory (STATIC_ROOT from settings.py file)
- grant access to wsgi file
- setup WSGI config (look into apache2 documentation for more information)

The rest is ssl and some basic config.
Please look into the apache2 documentation for more information.

### Testing

Tests are written for each module and stored in the corresponding tests module.
Tests are executed using the following command:

./djangoProject/manage.py test djangoProject

To test just one specific application specify the application in question:

./djangoProject/manage.py test <aplicationname>

## Documentation

This project is documented using the LBS Sphinx integration.
To rebuild the documentation just run:

```
# build html and pdf
make all

# build only html
make sphinx_html

# build only pdf
make sphinx_pdf

# run the sphinx autobuilder (rebuilds on every detected code change)
make sphinx_autobuilder
```

If you have troubles building the documentation please ensure:

1. is the lbs submodule checked out (git submodule init && git submodule update)
2. are the lbs python requirements installed (requirements txt insit the lbs)
3. is your lbs environment setup correctly

dephp
=====

Unofficial CLI application that decodes files through http://www.unphp.net web service.

Help
----

::

	usage: dephp [-h] [-V] [-m] [-a APIKEY] [-o OUTPUT] [file]

	Unofficial CLI application that decodes files through unphp.net web service

	positional arguments:
	  file                  The file to read. If not specified it will be read
	                        from STDIN

	optional arguments:
	  -h, --help            show this help message and exit
	  -V, --version         show program's version number and exit
	  -m, --metadata        Print response metadata
	  -a APIKEY, --apikey APIKEY
	                        Unphp.net API key
	  -o OUTPUT, --output OUTPUT
	                        Write the result to OUTPUT. If not specified it will
	                        be printed to STDOUT

Configuration file
------------------

You can save the unphp API key in a configuration file, either globally in */etc/dephp.conf* or locally in *$HOME/.dephp.conf*.

Sample configuration::

	[DEFAULT]
	apikey     = ABCDE # get one at http://www.unphp.net/api/request/
	entrypoint = http://www.unphp.net/api/v2/post # default

LICENSE
-------
Copyright (c) 2014 Massimiliano Torromeo

dephp is free software released under the terms of the BSD license.

See the LICENSE file provided with the source distribution for full details.

Contacts
--------

* Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
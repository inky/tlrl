tlrl (too long; read later)
====

[Instapaper](http://www.instapaper.com/)'s _Read Later_ for terminal junkies.

Requires Python 2.5 or greater.

Usage
-----

The first time you run `tlrl`, a sample config file will be created in
your home folder:

    $ ./tlrl
    Empty configuration file created at $HOME/.tlrl

    $ cat ~/.tlrl
    [Instapaper]
    username =
    password =

Open this file and fill in your username (or email address), and your
password if you set one. You can verify that your settings are correct
by running `tlrl` with the `-a` (or `--auth`) option:

    $ ./tlrl -a
    Username and password are correct!

To add a URL to your reading list, simply run `tlrl URL`:

    $ ./tlrl http://filer.case.edu/dts8/thelastq.htm
    URL added!

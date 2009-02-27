tlrl (too long; read later)
====

[Instapaper](http://www.instapaper.com/)'s _Read Later_ for terminal junkies.

Requires Python 2.5 or greater.

Usage
-----

The first time you run `tlrl`, a sample config file will be created in
your home folder. Open it in your editor of choice and fill in your
Instapaper credentials.

    $ ./tlrl
    Empty configuration file created at $HOME/.tlrl

    $ cat ~/.tlrl
    [Instapaper]
    username =
    password =

Once you've done this, you can verify your username and password with
the `-a` (or `--auth`) option.

    $ ./tlrl -a
    Username and password are correct!

To add a URL to your reading list, simply run `tlrl URL`:

    $ ./tlrl http://filer.case.edu/dts8/thelastq.htm
    URL added!

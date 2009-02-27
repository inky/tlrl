tldr (too long; didn't read)
====

[Instapaper](http://www.instapaper.com/)'s _Read Later_ for terminal junkies.

Usage
-----

The first time you run `tldr`, a sample config file will be created in
your home folder. Open it in your editor of choice and fill in your
username and password for Instapaper.

    $ ./tldr
    Empty configuration file created at $HOME/.tldr

Once you've done this, you can verify your username and password with
the `-a` or `--auth` option.

    $ ./tldr -a
    Username and password are correct!

To add a URL to your reading list, simply run `tldr URL`:

    $ ./tldr http://filer.case.edu/dts8/thelastq.htm
    URL added!

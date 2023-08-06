=========
Rattledin
=========

A Python library to communicate with Linkedin using an asynchronous interface

-------------
Environment
-------------

.............
Dependencies
.............
Necessary for use:

* Python >= 3.6
* Pip
* Git (development)
* Make (development)
* Python Venv (development)
    
It's recommended the use of Python virtual environments, to use only needed dependencies.
With the `python venv` installed, to create an environment, just do:

    $ python3.6 -m venv venv

    $ . venv /bin/activate

The bash will start using the virtual environment for now on.

.............
Build
.............

This library can be imported to be used in another applications. So, after the git clone
to install the library inside the virtual environment:

  $ make deploy


This way, the application will be completely installed, and all it's dependencies.
When finished, the library can be imported inside `python` or a `.py` file with:

    from rattledin import LinkedinCore
    
This library depends on `Linkedin API`, that can be found [here](https://github.com/jabolina/linkedin-api),
so it's recommended to install this before Rattledin installation, it's better to clone the repo
because the PyPi version will not always be in the latest version. Install the `Linkedin API` inside
the same virtual environment. With `make deploy` the library will be cloned and installed.

-------------
Examples
-------------

In the `examples` folder exists and example on how to use the library to communicate with Linkedin.
At the moment only exists message methods, but someday, I'll extends this. If you want to create more
methods, fell free to contribute and create a pull request.


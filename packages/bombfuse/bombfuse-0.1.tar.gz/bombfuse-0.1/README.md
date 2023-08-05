# bombfuse
Python module for specifying timeouts when executing functions

## Installation
To install this package, run the following command:

    $ pip install bombfuse

## Usage

    >>> import time
    >>> from bombfuse import timeout
    >>> def func(msg):
    >>>     while True:
    >>>         time.sleep(1)
    >>>         print msg
    >>>
    >>> timeout(5, func, "Hello world!")
    Hello world!
    Hello world!
    Hello world!
    Hello world!	
    >>>
# oct2pypower

Python bridge to [MATPOWER](https://github.com/MATPOWER/matpower/) using
[Oct2Py](https://blink1073.github.io/oct2py/).

## Usage

`oct2pypower` is available on [Docker Hub](https://hub.docker.com/r/rlincoln/oct2pypower):

```
$ docker run -it rlincoln/oct2pypower
```

This command starts an [IPython](https://ipython.org) shell initialized with
a variable `mp` for calling MATPOWER functions, for example:

```
In [1]: mp.runpf()
```

See the [MATPOWER function reference](http://www.pserc.cornell.edu/matpower/docs/ref/)
for further details.


# README #

This is (or will be) a set of Python functions to detect steps in raw accelerometer data.

### Prereqs: ###

Python libraries:

* numpy

* scipy

* pandas

* geneactiv (currently private) for running tests

### How do I use it? ###

    from pydometer import Pedometer

    # Your data goes here:
    gx, gy, gz = [x data], [y data], [z data]
    sr = sample rate

    p = Pedometer(gx=gx, gy=gy, gz=gz, sr=sr)
    step_count, step_locations = p.get_steps()

### Who do I talk to? ###

* Alex Page, alex.page@rochester.edu

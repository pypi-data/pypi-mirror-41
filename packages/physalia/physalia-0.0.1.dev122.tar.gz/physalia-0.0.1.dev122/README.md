[![Build Status](https://travis-ci.org/TQRG/physalia.svg?branch=master)](https://travis-ci.org/TQRG/physalia)
[![PyPI version](https://badge.fury.io/py/physalia.svg)](https://badge.fury.io/py/physalia)
[![PyPI downloads](https://img.shields.io/pypi/d/physalia.svg)](https://pypi.python.org/pypi/physalia)
[![PyPI status](https://img.shields.io/pypi/status/physalia.svg)](https://pypi.python.org/pypi/physalia)
[![Code Health](https://landscape.io/github/TQRG/physalia/master/landscape.svg?style=flat)](https://landscape.io/github/TQRG/physalia/master)


# Physalia

Energy measurement framework for Mobile Apps.

More info and documentation in the [website](https://tqrg.github.io/physalia/).

## Install

```
$ pip install https://github.com/luiscruz/PyMonsoon
$ pip install physalia
```

## Example

The simplest way to measure something:

```
from physalia.power_meters import MonsoonPowerMeter
from time import sleep
 
 # change voltage and serial number accordingly:
power_meter = MonsoonPowerMeter(voltage=3.8, serial=12886) 
power_meter.start()
sleep(2) # some work
energy_consumption, duration, error_flag = power_meter.stop()
```

Several things need to be done to make sure we can measure energy consumption in Android devices (e.g., setup WiFi control and disable USB).
Physalia takes care of that already:



````
from physalia.power_meters import MonsoonPowerMeter
from physalia.energy_profiler import AndroidUseCase
from time import sleep

 # change voltage and serial number accordingly:
power_meter = MonsoonPowerMeter(voltage=3.8, serial=12886)

def run(usecase):
	sleep(2) # some work
	
use_case = AndroidUseCase(
  'login',
  'path/to/apk',
  'com.test.app',
  '0.0',
  prepare=None,
  run=run,
  cleanup=None
)
measurement = use_case.run(power_meter=power_meter)
print(measurement)
````

## Contributing

Please help us improve this library!

If you have ideas for new features or anything behaves unexpectedly please report an issue.

If you find an issue you can actually help fixing please make a pull request of your code.

### Running tests

To run all tests and checks locally run:

`$ detox -e py27,py36`

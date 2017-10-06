# airsensor-py

[![PyPI version](https://badge.fury.io/py/airsensor-py.svg)](https://badge.fury.io/py/airsensor-py)

Python package for getting sensor values from an Ambient Air Sensor such as offered by [Rehau](https://www.amazon.co.uk/Rehau-USB-Stick-Ambient-Sensor/dp/B00ZXP6EI4).

## Getting Started

This section will introduce you to airsensor-py and how to install and use it for fun and profit.

### Prerequisites

Make sure that python 3 + pip is installed.

### Installing

```
pip install airsensor-py
```

## Usage

You can either use this package as a library in your code or using the bundled CLI. You'll have to run it as root or set up a udev rule to grant r/w access to the device to the user. For more instructions on that, see [here](https://github.com/tuxedo0801/usb-sensors-linux).

### Library

```
from airsensor.core import AirSensor
airsensor = AirSensor()
voc = airsensor.get_voc()
print(voc)

> 450
```

### CLI

```
$ airsensor-py

> 450
```

## Built With

* [PyUSB](https://walac.github.io/pyusb/)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Contribution

Want to add a feature or report a bug? Open an issue or a pull request for me!

## Acknowledgments

* [A C implementation](https://code.google.com/archive/p/airsensor-linux-usb/) was done by Rodric Yates which I used to see how the interaction with the device works.
# pirev

[![pypi version](https://img.shields.io/pypi/v/pirev.svg?style=flat)](https://pypi.org/project/pirev/)
[![license](https://img.shields.io/npm/l/pirev.svg?style=flat)](https://opensource.org/licenses/MIT)

A tiny, zero-dependency utility providing hardware revision information for Raspberry Pi devices. All information is parsed from the device's [revision code](https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md) located in `/proc/cpuinfo`.

## Installation

```
pip install pirev
```

## Usage

```
from pirev import getInfo

info = getInfo()

print('Raspberry Pi {type}'.format(type=info['revision']['type']))
```

## Error handling

Running the utility on a device which is **not** a Raspberry Pi will result in an error being raised.

```
try:
  info = getInfo()
  print('Raspberry Pi {type}'.format(type=info['revision']['type']))
except ReferenceError:
  print('Not a Raspberry Pi device!')
```

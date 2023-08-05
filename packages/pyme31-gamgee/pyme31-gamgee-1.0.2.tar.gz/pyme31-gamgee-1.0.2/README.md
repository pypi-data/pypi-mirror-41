# pyme31

Module for reading data from Digital Multimeter Metex ME-31 via RS-232

## Install

```bash
pip install pyme31
```

## Usage

```python
from pyme31 import Me31

def main():
  # on windows use COM1, COM2...
  dmm = Me31('COM1')

  # on unix machines use /dev/ttyXX
  dmm = Me31('/dev/ttyXX')

  measurment = dmm.get_measurment()

  print(measurment)
  print(measurment.value)
  print(measurment.unit)
  print(measurment.measuring_mode)

if __name__ == "__main__":
  main()
```

example output

```bash
AC 19.1 mV
19.1
Unit.MILIVOLT
MeasuringMode.AC
```
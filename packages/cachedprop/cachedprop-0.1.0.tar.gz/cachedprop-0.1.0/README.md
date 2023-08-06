# cachedprop
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Build Status](https://travis-ci.com/Spin14/cachedprop.svg?branch=master)](https://travis-ci.com/Spin14/cachedprop) 

cached property method decorator

## Demo
```python
from cachedprop import cpd


class LabRat:
    def __init__(self) -> None:
        self._hp = None
    
    def expensive_hp_getter(self) -> int:
        ...
       
    @cpd
    def hp(self):
        return self.expensive_hp_getter()
        

rat = LabRat()
print(rat.hp) # expensive_hp_getter is called, value gets "cached", prints value
print(rat.hp) # prints "cached" value only.
```
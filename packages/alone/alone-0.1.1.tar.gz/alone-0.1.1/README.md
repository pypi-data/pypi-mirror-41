# Alone
Metaclass that defines a class as a singleton.

[Kudo to theheadofabroom from SO for the implementation][so-post]

## Getting started

Python 2:
```python
import alone.MetaSingleton

class YourClass(alone.MetaSingleton):
    pass
```
Python 3:
```python
import alone.MetaSingleton

class YourClass(metaclass=alone.MetaSingleton):
    pass
```

[so-post]: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


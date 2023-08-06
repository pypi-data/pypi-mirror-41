# py-singleton
Metaclass that defines a class as a singleton.

[Kudo to theheadofabroom from SO for the implementation][so-post]

## Getting started

Python 2:
```python
import singletons.MetaSingleton

class YourClass(singletons.MetaSingleton):
    pass
```
Python 3:
```python
import singletons.MetaSingleton

class YourClass(metaclass=singletons.MetaSingleton):
    pass
```

[so-post]: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


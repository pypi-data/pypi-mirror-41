rekey
======
Transform collections into dicts by deriving keys from each item.


### Install
```pip install rekey```


### Usage
```
from rekey import rekey

# key a list of records by id
people = [
  { 'id' : 1, 'name' : 'alice', 'age' : 30 },
  { 'id' : 2, 'name' : 'bob', 'age' : 24 },
  { 'id' : 3, 'name' : 'charlie', 'age' : 88 },
]
rekey(people, 'id')
=> {
  1 => { 'id' : 1, 'name' : 'alice', 'age' : 30},
  2 => { 'id' : 2, 'name' : 'bob', 'age' : 24},
  3 => { 'id' : 3, 'name' : 'charlie', 'age' : 88},
}

# create an id => value map
rekey(people, 'id', 'name')
=> {
  1 => 'alice',
  2 => 'bob',
  3 => 'charlie',
}


# use Rekeyables for built-in functionality

from rekey.rekeyable import RekeyableSet

Point = namedtuple('Point', ['name', 'x', 'y'])  # hashable
points = RekeyableSet([
    Point(name='home', x=1, y=2),
    Point(name='work', x=3, y=6),
])
points.rekey('name') 
=> {
    'home' : Point(name='home', x=1, y=2),
    'work' : Point(name='work', x=3, y=6),
}


# use the Rekeyable mixin to build your own

from rekey.rekeyable import Rekeyable
class MyDict(dict, Rekeyable): pass

MyDict({
  'home' : {'distance' : 1, 'weather' : 'sunny' },
  'work' : {'distance' : 5, 'weather' : 'foggy' },
}).rekey('weather', 'distance')
> {
  'sunny' : 1,
  'foggy' : 5,
}
```

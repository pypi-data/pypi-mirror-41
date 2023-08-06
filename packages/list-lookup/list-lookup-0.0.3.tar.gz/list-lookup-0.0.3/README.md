# ListLookup
Wrapper for faster lookups in a list of objects/dictionaries.
**ATTENTION** Do not modify list once index are created!

```
from listlookup import ListLookup
cities = ListLookup([
  {"id": 1, "country": "us", name: "Atlanta"},
  {"id": 2, "country": "us", name: "Miami"},
  {"id": 3, "country": "uk", name: "Britain"},
])

cities.index("id", lambda d: d['id'], True)
cities.index("country", lambda d: d['country'])

list(cities.lookup(id=1))
>>> [{"id": 1, "country": "us", name: "Atlanta"}]

list(cities.lookup(country="us", preserve_order=True))
>>> [{"id": 1, "country": "us", name: "Atlanta"}, {"id": 2, "country": "us", name: "Miami"}]

list(cities.lookup(id=2, country="uk"))
>>> []
```

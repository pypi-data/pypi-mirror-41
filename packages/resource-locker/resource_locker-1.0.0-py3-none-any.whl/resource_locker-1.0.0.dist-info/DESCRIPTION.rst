# Resource Locker
One at a time, please!

[![CircleCI](https://circleci.com/gh/ARMmbed/resource_locker.svg?style=shield&circle-token=992df378a72010c9b4ed32c14c1a354cda9664d2)](https://circleci.com/gh/ARMmbed/resource_locker)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://circleci.com/gh/ARMmbed/resource_locker)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ARMmbed/resource_locker)

_Resource Locker_ assumes arbitrary resources, each with their own deterministic, unique identifier.
The usage state is retained in a lock server (e.g. a single redis instance, redlock cluster, or similar).
Resources are assumed to be discoverable and filterable by the clients that intend to use them.
This reduces the need to categorise and filter resources on the client's behalf, in comparison to
a resource allocation system with a database of all resources (in which typically only the resource
server is performing discovery).

A comparison of approaches:

| feature | locks only | resource server |
|-|:-|-|
| Collision protection | Y | Y |
| Lease timeout | Y | Y |
| Resource database | N | Y |
| Server-side resource filtering | N | Y |
| Arbitrary resource types | Y | Maybe (depends on db schema) |
| Pool growth/reduction | N (SoC*, other service) | Maybe (ideally SoC, but often mixed in) |
| Discovery queries | O(C**) | O(1) |

(*separation of concerns, **number of clients)

In practise, the intent is for resource sharing between parallel testruns on a constrained resource pool.
A separate service tracks resource presence, so discovery (querying for them) is assumed to be trivial.

## Install
The usual:

`pipenv install resource_locker`

or

`pipenv install -e git+https://github.com/ARMmbed/resource_locker.git#egg=resource_locker`

## Usage

### Locking
```python
# some resource thing
devices = list_connected_devices()

from resource_locker import Lock, R, P
from operator import attrgetter
req1 = R(*devices, need=2, key_gen=attrgetter('id'))
req2 = R(P('this one thing'))
with Lock(req1, req2, 'other thing') as obtained:
    print(obtained[0][0]) # first requirement, first device
    print(obtained[0][1]) # first requirement, second device
    print(obtained[2][0]) # `other thing`

    # alternatively
    req1[1]  # second device
    req2[0]  # 'this one thing'
```
#### Configuration
Lock backend can be configured as follows:

```python
from redis import StrictRedis
from resource_locker import RedisLockFactory
from resource_locker import Lock
custom = RedisLockFactory(client=StrictRedis(db=7))
Lock('a', lock_factory=custom)
```

### Reporting
The `RedisReporter` class can be used to track lock usage automatically:

```python
import time
from resource_locker import reporter
from resource_locker import Lock
from resource_locker import P
with Lock(P('a', model='T1000'), reporter_class=reporter.RedisReporter):
    time.sleep(1)
reporter.Query().all_tags()  # ['key', 'model']
reporter.Query().all_values('model')  # ['T1000']
reporter.Query().all_aspects('model', 'T1000') # ...

{'lock_acquire_count': 1,
 'lock_acquire_wait': 0.008001565933228,
 'lock_release_count': 1,
 'lock_release_wait': 1.000413179397583,
 'lock_request_count': 1}
```

#### Configuration
Reporter backend can be configured as follows:
```python
from functools import partial
from redis import StrictRedis
from resource_locker import reporter
from resource_locker import Lock
client = StrictRedis(db=9)
custom_reporter = partial(reporter.RedisReporter, client=client)
Lock(reporter_class=custom_reporter)
```

## Related reading
[Distributed Lock Manager](https://en.wikipedia.org/wiki/Distributed_lock_manager)
| [Pareto Efficiency](https://en.wikipedia.org/wiki/Pareto_efficiency)
| [Ordered Locking](http://www.informit.com/articles/article.aspx?p=30188&seqNum=7)
| [Simultaneous Locking](http://www.informit.com/articles/article.aspx?p=30188&seqNum=6)



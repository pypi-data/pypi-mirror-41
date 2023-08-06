# BZFlag Networking

![](https://img.shields.io/pypi/v/bzflag-networking.svg)
![](https://img.shields.io/pypi/pyversions/bzflag-networking.svg)
![](https://img.shields.io/github/license/allejo/bzflag-networking.py.svg)

A Python 3 package for reading and handling BZFlag network packets.

BZFlag Replay files are simply the raw packets stored in a file together, so this library will let you read replay files and unpack them into Python objects that can be serialized into JSON.

```python
import json

from bzflag.utilities.json_encoder import RRLogEncoder
from bzflag.replay import Replay


replay = Replay('my-bz-replay.rec')

with open('my-bz-replay.json', 'w') as json_file:
    json_file.write(json.dumps(replay, cls=RRLogEncoder, indent=2))
```

## License

[MIT](./LICENSE.md)

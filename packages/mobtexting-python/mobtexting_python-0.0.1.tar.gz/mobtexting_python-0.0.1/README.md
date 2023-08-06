# python plugin for mobtexting

This package makes it easy to send [Mobtexting notifications](https://mobtexting.com).

## Installation

You can install the package via:

``` bash
```

## Usage

### Send an SMS

```python
from mobtexting.client import Client

access_token = 'xxxxxxxxxxxxxxxxxx'

client = Client(access_token)

response = client.send(
    to="1234567890",
    _from="MobTxt",
    body="Hello from Python!",
    service="P"
)

print response.json()
```


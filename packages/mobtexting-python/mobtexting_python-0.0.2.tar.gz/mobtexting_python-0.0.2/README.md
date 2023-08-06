# python plugin for mobtexting

This package makes it easy to send [Mobtexting notifications](https://mobtexting.com).

## Installation

You can install the package via pip :

``` bash
pip install git+git://github.com/mobtexting/mobtexting-python.git --user
```

## Send SMS Usage

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

## Verify Usage

### Send

```python
from mobtexting.verify import Verify

access_token = 'xxxxxxxxxxxxxxxxxx'

verify = Verify(access_token)

response = verify.send(
    to="1234567890",
)

print response.json()
```
### Check

```python
from mobtexting.verify import Verify

access_token = 'xxxxxxxxxxxxxxxxxx'

verify = Verify(access_token)

response = verify.check(
    id='b51be650-fdb2-4633-b101-d450e8d9ec64', # id you received while sending
    token='123456' # token entered by user
)

print response.json()
```


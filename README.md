# LayerZero-Scan

A minimal Python Wrapper for the LayerZero Scan API.

___

## Installation

``` bash
pip install git+https://github.com/kamilgg/layerzero-scan
```

Or install from [PyPI](https://pypi.org/project/layerzero-scan/)::

``` bash
pip install layerzero-scan==1.0.0
```

## Tests

In `bash` test that everything looks OK before proceeding:

``` bash
bash run_tests.sh
````

## Usage

In `python` create a client:

``` python
# For mainnet
from layerzero import LayerZero
client = LayerZero()

# For testnet
from layerzero import LayerZeroTestnet, Chains
client = LayerZeroTestnet()  # Testnet
client = LayerZeroTestnet(Chains.TESTNET)  # Also testnet
client = LayerZeroTestnet(Chains.SANDBOX)  # Sandbox
```

Then you can call all available methods, e.g.:
``` python
latest_messages = client.get_latest_messages()

latest_messages.count

> 63747514

tx_hash = "0xdbb9456feb829f67c2d26df00ba1f6f383463a0a7dc6ebc5d48c025800ed901b"
message = client.get_message_by_hash(tx_hash)

message.src_ua_nonce

> 1866644

message.status

> DELIVERED
```

___


By **kamgg.eth**
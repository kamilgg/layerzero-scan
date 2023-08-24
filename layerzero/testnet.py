from typing import Union

from layerzero.wrappers import TestnetWrapper
from layerzero.enums import EndpointsEnum
from layerzero.types import Message


class LayerZeroTestnet:
    def __init__(self, url: str = EndpointsEnum.TESTNET):
        self.wrapper = TestnetWrapper(url)

    def get_message_by_hash(self, tx_hash: str) -> Union[Message, None]:
        raw_json = self.wrapper.get_message_by_hash(tx_hash)["messages"]
        if len(raw_json) == 1:
            return Message.de_json(raw_json[0])
        else:
            return None

from typing import Union

from layerzero.wrappers import MainnetWrapper
from layerzero.enums import EndpointsEnum
from layerzero.types import LatestMessages, Message, MessagesByHash


class LayerZero:
    def __init__(self, url: str = EndpointsEnum.MAINNET):
        self.wrapper = MainnetWrapper(url)

    def get_latest_messages(self, next_token=None) -> LatestMessages:
        raw_json = self.wrapper.get_latest_messages(next_token)["data"]["messages"]
        return LatestMessages.de_json(raw_json)

    def get_message_by_hash(self, tx_hash: str) -> Union[Message, None]:
        raw_json = self.wrapper.get_message_by_hash(tx_hash)["data"]
        return MessagesByHash.de_json(raw_json)

    def get_message_by_params(
            self,
            src_chain_id: int,
            dst_chain_id: int,
            src_ua_address: str,
            dst_ua_address: str,
            src_ua_nonce: int
    ) -> Union[Message, None]:
        raw_json = self.wrapper.get_message_by_params(
            src_chain_id=src_chain_id,
            dst_chain_id=dst_chain_id,
            src_ua_address=src_ua_address,
            dst_ua_address=dst_ua_address,
            src_ua_nonce=src_ua_nonce,
        )["data"]["message"]
        if raw_json is not None:
            return Message.de_json(raw_json)
        return raw_json

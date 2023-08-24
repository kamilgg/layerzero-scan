from requests import Session

from layerzero.enums import OperationsEnum, QueriesEnum
from layerzero.exceptions import APIError


class MainnetWrapper:
    def __init__(self, url: str):
        self.url = url
        self.session = Session()

    def get_latest_messages(self, next_token: str = None):
        variables = {
            "nextToken": next_token,
        }
        payload = {
            "operationName": OperationsEnum.GET_LATEST_MESSAGES,
            "query": QueriesEnum.GET_LATEST_MESSAGES,
            "variables": variables,
        }
        return self._make_post_request(payload)

    def get_message_by_hash(self, tx_hash: str):
        variables = {"hash": tx_hash}
        payload = {
            "operationName": OperationsEnum.GET_MESSAGE_BY_ANY_HASH,
            "query": QueriesEnum.GET_MESSAGE_BY_ANY_HASH,
            "variables": variables,
        }
        return self._make_post_request(payload)

    def get_message_by_params(
            self,
            src_chain_id: int,
            dst_chain_id: int,
            src_ua_address: str,
            dst_ua_address: str,
            src_ua_nonce: int
    ):
        variables = {
            "srcChainId": src_chain_id,
            "dstChainId": dst_chain_id,
            "srcUaAddress": src_ua_address,
            "dstUaAddress": dst_ua_address,
            "srcUaNonce": src_ua_nonce
        }
        payload = {
            "operationName": OperationsEnum.GET_MESSAGE_BY_PARAMS,
            "query": QueriesEnum.GET_MESSAGE_BY_PARAMS,
            "variables": variables,
        }
        return self._make_post_request(payload)

    def _make_post_request(self, payload):
        response = self.session.post(
            url=self.url,
            json=payload,
        )
        if response.ok:
            return response.json()
        else:
            raise APIError("Error with LayerZero API!")

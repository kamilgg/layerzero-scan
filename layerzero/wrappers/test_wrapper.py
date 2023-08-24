from requests import Session

from layerzero.enums import EndpointsEnum
from layerzero.exceptions import APIError


class TestnetWrapper:
    def __init__(self, url: str = EndpointsEnum.TESTNET):
        self.url = url
        self.session = Session()

    def get_message_by_hash(self, tx_hash: str):
        method = f"/tx/{tx_hash}"
        return self._make_get_request(method)

    def _make_get_request(self, method):
        response = self.session.get(url=f"{self.url}{method}")
        if response.ok:
            return response.json()
        else:
            raise APIError("Error with LayerZero API!")



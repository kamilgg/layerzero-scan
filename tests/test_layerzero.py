from layerzero import LayerZero, LayerZeroTestnet
from layerzero.types import LatestMessages, Message


class TestLayerZeroMainnet:
    def test_latest_messages(self):
        client = LayerZero()
        latest_messages = client.get_latest_messages()
        assert type(latest_messages) == LatestMessages
        assert type(latest_messages.count) == int
        assert type(latest_messages.messages) == list

    def test_message_by_hash(self):
        client = LayerZero()
        tx_hash = "0xdbb9456feb829f67c2d26df00ba1f6f383463a0a7dc6ebc5d48c025800ed901b"
        message = client.get_message_by_hash(tx_hash)
        assert type(message) == Message

    def test_fake_message(self):
        client = LayerZero()
        tx_hash = "fake_hash"
        message = client.get_message_by_hash(tx_hash)

        assert message is None

    def test_message_by_params(self):
        dst_chain_id = 125
        dst_ua_address = "0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123"
        src_chain_id = 145
        src_ua_address = "0xfa5ed56a203466cbbc2430a43c66b9d8723528e7"
        src_ua_nonce = 1866644
        client = LayerZero()
        message = client.get_message_by_params(
            src_chain_id=src_chain_id,
            dst_chain_id=dst_chain_id,
            src_ua_address=src_ua_address,
            dst_ua_address=dst_ua_address,
            src_ua_nonce=src_ua_nonce
        )

        assert type(message) == Message

    def test_fake_message_by_params(self):
        dst_chain_id = 125
        dst_ua_address = "fake_address"
        src_chain_id = 145
        src_ua_address = "fake_address"
        src_ua_nonce = 1866644
        client = LayerZero()
        message = client.get_message_by_params(
            src_chain_id=src_chain_id,
            dst_chain_id=dst_chain_id,
            src_ua_address=src_ua_address,
            dst_ua_address=dst_ua_address,
            src_ua_nonce=src_ua_nonce
        )

        assert message is None


class TestLayerZeroTestnet:
    def test_message_by_hash(self):
        client = LayerZeroTestnet("https://api-mainnet.layerzero-scan.com")
        tx_hash = "0xdbb9456feb829f67c2d26df00ba1f6f383463a0a7dc6ebc5d48c025800ed901b"
        message = client.get_message_by_hash(tx_hash)

        assert type(message) == Message

    def test_fake_message(self):
        client = LayerZeroTestnet("https://api-mainnet.layerzero-scan.com")
        tx_hash = "fake_hash"
        message = client.get_message_by_hash(tx_hash)

        assert message is None

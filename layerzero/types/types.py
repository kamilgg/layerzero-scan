from typing import List

from layerzero.types.json_deserializable import JsonDeserializable


class Message(JsonDeserializable):
    @classmethod
    def de_json(cls, raw_json):
        obj = cls.check_json(raw_json)
        src_ua_address = obj.get("srcUaAddress")
        dst_ua_address = obj.get("dstUaAddress")
        updated = int(obj.get("updated"))
        created = int(obj.get("created"))
        src_chain_id = int(obj.get("srcChainId"))
        dst_chain_id = int(obj.get("dstChainId"))
        dst_tx_hash = obj.get("dstTxHash")
        dst_tx_error = obj.get("dstTxError")
        src_tx_hash = obj.get("srcTxHash")
        src_block_hash = obj.get("srcBlockHash")
        src_block_number = (
            int(obj.get("srcBlockNumber")) if obj.get("srcBlockNumber") else None
        )
        src_ua_nonce = int(obj.get("srcUaNonce")) if obj.get("srcUaNonce") else None
        status = obj.get("status")
        adapter_params = obj.get("adapterParams")

        return cls(
            src_ua_address=src_ua_address,
            dst_ua_address=dst_ua_address,
            updated=updated,
            created=created,
            src_chain_id=src_chain_id,
            dst_chain_id=dst_chain_id,
            dst_tx_hash=dst_tx_hash,
            dst_tx_error=dst_tx_error,
            src_tx_hash=src_tx_hash,
            src_block_hash=src_block_hash,
            src_block_number=src_block_number,
            src_ua_nonce=src_ua_nonce,
            status=status,
            adapter_params=adapter_params,
        )

    def __init__(
        self,
        src_ua_address: str,
        dst_ua_address: str,
        updated: int,
        created: int,
        src_chain_id: int,
        dst_chain_id: int,
        dst_tx_hash: str,
        dst_tx_error: str,
        src_tx_hash: str,
        src_block_hash: str,
        src_block_number: int,
        src_ua_nonce: int,
        status: str,
        adapter_params: str,
    ):
        self.src_ua_address = src_ua_address
        self.dst_ua_address = dst_ua_address
        self.updated = updated
        self.created = created
        self.src_chain_id = src_chain_id
        self.dst_chain_id = dst_chain_id
        self.dst_tx_hash = dst_tx_hash
        self.dst_tx_error = dst_tx_error
        self.src_tx_hash = src_tx_hash
        self.src_block_hash = src_block_hash
        self.src_block_number = src_block_number
        self.src_ua_nonce = src_ua_nonce
        self.status = status
        self.adapter_params = adapter_params


class LatestMessages(JsonDeserializable):
    @classmethod
    def de_json(cls, raw_json):
        obj = cls.check_json(raw_json)
        next_token = obj.get("nextToken")
        count = int(obj.get("count"))

        messages = []
        for item in obj["items"]:
            messages.append(Message.de_json(item))

        return cls(next_token=next_token, count=count, messages=messages)

    def __init__(self, next_token, count: int, messages: List[Message]):
        self.next_token = next_token
        self.count = count
        self.messages = messages


class MessagesByHash(JsonDeserializable):
    @classmethod
    def de_json(cls, raw_json):
        obj = cls.check_json(raw_json)
        dst_tx = obj.get("dstTx")
        src_tx = obj.get("srcTx")

        if len(dst_tx["items"]) == 1:
            return Message.de_json(dst_tx["items"][0])

        if len(src_tx["items"]) == 1:
            return Message.de_json(src_tx["items"][0])

        return None

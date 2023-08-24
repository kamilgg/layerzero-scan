from dataclasses import dataclass


@dataclass(frozen=True)
class OperationsEnum:
    GET_LATEST_MESSAGES: str = "getLatestMessages"
    GET_MESSAGE_BY_ANY_HASH: str = "getMessageByAnyHash"
    GET_MESSAGE_BY_PARAMS: str = "getMessageChainIdsSrcUAAddressAndSrcOutboundNonce"

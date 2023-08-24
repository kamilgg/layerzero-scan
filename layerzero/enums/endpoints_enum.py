from dataclasses import dataclass


@dataclass(frozen=True)
class EndpointsEnum:
    MAINNET: str = "https://qtrhqncfi4.execute-api.us-east-1.amazonaws.com/prod/graphql"
    TESTNET: str = "https://api-testnet.layerzero-scan.com"
    SANDBOX: str = "https://api-sandbox.layerzero-scan.com"

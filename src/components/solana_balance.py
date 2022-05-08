import csv
import theblockchainapi
from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork, SolanaCurrencyUnit

API_KEY = "2yqJ2XYLJUcAAbZ"
SECRET_KEY = "XTmm7praz1fZlD0"

if __name__ == '__main__':
    resource = TheBlockchainAPIResource(
        api_key_id=API_KEY,
        api_secret_key=SECRET_KEY
    )
    public_key = "GLSj3eDnrEMrgKuohW4beS3a9vMqvtGqsArbLUApH4f8"
    balance = resource.get_balance(public_key, unit=SolanaCurrencyUnit.SOL, network=SolanaNetwork.MAINNET_BETA)
    print(f"Score: {balance}")
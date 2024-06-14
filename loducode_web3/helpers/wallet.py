from web3 import Web3

def create_wallet():
    """
    Create a wallet for a person.
    """
    connection = Web3()
    connection.eth.account.enable_unaudited_hdwallet_features()
    account = connection.eth.account.create_with_mnemonic()
    seed_phrase = account[1]
    address = account[0].address
    private_key = account[0].key.hex()
    return (seed_phrase, address, private_key)
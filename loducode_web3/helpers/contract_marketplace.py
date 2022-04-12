import json
from abc import ABC

from django.conf import settings
from web3 import Web3


class ContractMarketplace(ABC):  # pylint: disable=R0904

    def __init__(self, bsc: str = settings.CONTRACT_MARKETPLACE_NET,
                 abi: str = json.loads(settings.CONTRACT_MARKETPLACE_ABI),
                 address_contract: str = settings.CONTRACT_MARKETPLACE_ADDRESS,
                 chain_id: int = settings.CONTRACT_MARKETPLACE_CHAIN_ID):
        self.bsc = bsc
        self.abi = abi
        self.address_contract = address_contract
        self.chain_id = chain_id

    def is_connetct(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        return web3.isConnected()

    def get_active_listings_count(self, ):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = 0
        try:
            response = int(_contract.functions.getActiveListingsCount().call())
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_active_listings_for_id(self, token_id: int):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = 0
        try:
            response = int(_contract.functions.getActiveListings(token_id).call())
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_active_listings(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.NftListingsActive().call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_listings_for_token(self, token_id: int):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = 0
        try:
            response = _contract.functions.getListingsForToken(token_id).call()
        except Exception as err:  # pylint: disable=W0703
            print("error: ", err)
        return response

    def get_price_listing(self, listing_id: int):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = 0.0
        try:
            response = _contract.functions.getPriceListing(listing_id).call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_listing_index(self, listing_index: int):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = 0.0
        try:
            response = _contract.functions.listings(listing_index).call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

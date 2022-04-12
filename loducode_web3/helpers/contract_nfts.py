import json
from abc import ABC

from django.conf import settings
from web3 import Web3


class ContractNft(ABC):  # pylint: disable=R0904

    def __init__(self, bsc: str = settings.CONTRACT_NFT_NET, abi: str = json.loads(settings.CONTRACT_NFT_ABI),
                 address_contract: str = settings.CONTRACT_NFT_ADDRESS,
                 chain_id: int = settings.CONTRACT_NFT_CHAIN_ID):
        self.bsc = bsc
        self.abi = abi
        self.address_contract = address_contract
        self.chain_id = chain_id

    def is_connetct(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        return web3.isConnected()

    def get_mints(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        try:
            mints = _contract.functions.totalMint().call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
            mints = 0
        return mints

    def get_id_tokens(self, address: str):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        id_token = {}
        try:
            check_token = Web3.toChecksumAddress(address)
            id_token = _contract.functions.walletOfOwner(check_token).call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return id_token

    def mint(self, address: str, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
             secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            mints = _contract.functions.mint(address, 1).buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'value': web3.toWei("0.0025", "ether"),
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                mints,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def start_pre_sale(self, start=True, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
                       secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            if start:
                pre_sale_func = _contract.functions.startPresale().buildTransaction({
                    'chainId': self.chain_id,
                    'gas': 1728712,
                    'gasPrice': web3.eth.gas_price,
                    'from': address_owner,
                    'nonce': web3.eth.get_transaction_count(address_owner)
                })
            else:
                pre_sale_func = _contract.functions.stopPresale().buildTransaction({
                    'chainId': self.chain_id,
                    'gas': 1728712,
                    'gasPrice': web3.eth.gas_price,
                    'from': address_owner,
                    'nonce': web3.eth.get_transaction_count(address_owner)
                })
            signed_txn = web3.eth.account.sign_transaction(
                pre_sale_func,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def start_sale(self, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
                   secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            pre_sale_func = _contract.functions.startSale().buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                pre_sale_func,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_contract(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        return _contract

    def get_web3(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        return web3

    def pause(self, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
              secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER, pause_status: bool = True):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            pre_sale_func = _contract.functions.pause(pause_status).buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                pre_sale_func,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_paused(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.paused().call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_presale(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.presale().call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_total_mint(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.totalMint().call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_total_supply(self):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.totalSupply().call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_token_uri(self, token_id: int):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = 0
        try:
            response = _contract.functions.tokenURI(token_id).call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def withdraw_all(self, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
                     secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            mints = _contract.functions.withdrawAll().buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                mints,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def update_base_extension(self, prefix: str = '', address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
                              secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            mints = _contract.functions.updateBaseExtension(prefix).buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                mints,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def update_max_mint_ammount(self, max_mint: int = 1000, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
                                secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            mints = _contract.functions.updateMaxMintAmount(max_mint).buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                mints,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def burn(self, token_id: int, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
             secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.burn(token_id).buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                response,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def update_token_price(self, new_value: float, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
                           secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.updateTokenPrice(new_value).buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                response,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def transfer_contract(self, new_owner: str, address_owner: str = settings.CONTRACT_NFT_ADDRESS_OWNER,
                          secret_owner: str = settings.CONTRACT_NFT_SECRET_OWNER):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = []
        try:
            response = _contract.functions.transferOwnership(new_owner).buildTransaction({
                'chainId': self.chain_id,
                'gas': 1728712,
                'gasPrice': web3.eth.gas_price,
                'from': address_owner,
                'nonce': web3.eth.get_transaction_count(address_owner)
            })
            signed_txn = web3.eth.account.sign_transaction(
                response,
                private_key=secret_owner)
            web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
            response = web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_transaction(self, transaction_hash: str):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        return web3.eth.get_transaction(transaction_hash)

    def get_owner(self, token_id: int):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            response = _contract.functions.ownerOf(token_id).call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def get_tokens(self, owner: str):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            response = _contract.functions.walletOfOwner(owner).call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

    def transfer_nft(self, transmitter: str, to: str, token_id: int):
        web3 = Web3(Web3.HTTPProvider(self.bsc))
        _contract = web3.eth.contract(address=self.address_contract, abi=self.abi)
        response = {}
        try:
            response = _contract.functions.transferFrom(transmitter, to, token_id).call()
        except Exception as err:  # pylint: disable=W0703
            print(err)
        return response

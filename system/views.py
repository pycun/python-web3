from email.headerregistry import Address
import json

from django.shortcuts import render

from web3 import Web3

# ======== Conectar a Ethereum ======= #
'''
from system.views import connect_to_web3
infura_url = "https://mainnet.infura.io/v3/9a4b03dcbc93487fa5be72288b8f3f59"
web3_connection = connect_to_web3()
'''


def connect_to_web3(infura_url):
    """
    Realiza la coneccion a web3 a la red ethereum mediante una url de tipo http proporcionada por infura
    :param infura_url: Datos de coneccion a web3 por medio de infura 
    :return eth conection:
    """
    # Se establece la coneccion
    web3_connection = Web3(Web3.HTTPProvider(infura_url))
    # Revisamos la coneccion
    print("Estado conexion: " + str(web3_connection.isConnected()))
    # Revisamos el numero de bloque en el que estamos
    print("La red de ETH se encuentra en el bloque: " + str(web3_connection.eth.blockNumber))

    return web3_connection

# ======== Consultar a un Wallet en la Red de Ethereum ======= #
'''
from system.views import connect_to_web3, consult_wallet

infura_url = "https://mainnet.infura.io/v3/9a4b03dcbc93487fa5be72288b8f3f59"
web3_connection = connect_to_web3(infura_url)

wallet_address = "0x4182649f33709ccb4E0CdD679983fb6b945a615F"

consult_wallet = consult_wallet(web3_connection, wallet_address)

'''

def consult_wallet(web3_connection, wallet_address):
    # Consultamos el balance, esto nos dara un valor decimal de 10 digitos por ejemplo: 2.9 ETH -> 290000000000
    wallet_balance = web3_connection.eth.getBalance(wallet_address)
    print("El wallet tiene un balance de " + str(wallet_balance) + " ETH Decimal")
    wallet_balance = web3_connection.fromWei(wallet_balance, 'ether')
    print("El wallet tiene un balance de " + str(wallet_balance) + " ETH")

    return True

# ======== Consultar Contrato ======= #

def consult_contract():
    infura_url = "https://mainnet.infura.io/v3/9a4b03dcbc93487fa5be72288b8f3f59"
    # Datos contratos Shiba Inu Token
    contract_address = "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"sender","type":"address"},{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"value","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"name","type":"string"},{"name":"symbol","type":"string"},{"name":"decimals","type":"uint8"},{"name":"totalSupply","type":"uint256"},{"name":"feeReceiver","type":"address"},{"name":"tokenOwnerAddress","type":"address"}],"payable":true,"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]')
    
    web3_connection = connect_to_web3(infura_url=infura_url)

    contract = web3_connection.eth.contract(address=contract_address, abi=abi)
    print("Instancia contrato: " + str(contract))

    total_supply = contract.functions.totalSupply().call()
    print("Total Supply: " + str(total_supply))

    total_supply = web3_connection.fromWei(total_supply, 'ether')
    print("Total Supply: " + str(total_supply))

    token_name = contract.functions.name().call()
    token_symbol = contract.functions.symbol().call()

    print("Mi token es: " + str(token_name))
    print("El symbolo de mi token es: " + str(token_symbol))
    
    wallet_address = "0x4182649f33709ccb4E0CdD679983fb6b945a615F"
    balance_address = contract.functions.balanceOf(wallet_address).call()
    balance_address = web3_connection.fromWei(balance_address, 'ether')
    print("El balance de " + str(token_name) + " es: " + str(balance_address))
    

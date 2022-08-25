from email.headerregistry import Address
import json

from django.shortcuts import render

from web3 import Web3

# ======== Conectar a Ethereum ======= #
'''
from system.views import connect_to_web3, consult_wallet, consult_contract, create_local_connection, send_transaction, write_smart_contracts, write_smart_contracts, deploy_smart_contracts, inspect_block
infura_url = "https://mainnet.infura.io/v3/<your_infura_api_key>"
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

infura_url = "https://mainnet.infura.io/v3/<your_infura_api_key>"
web3_connection = connect_to_web3(infura_url)

wallet_address = "0x4182649f33709ccb4E0CdD679983fb6b945a615F"

consult_wallet = consult_wallet(web3_connection, wallet_address)
'''


def consult_wallet(web3_connection, wallet_address):
    """
    Consulta un wallet en la blockchain de ethereum
    :param web3_connection:
    :return wallet_address:
    """
    # Consultamos el balance, esto nos dara un valor decimal de 10 digitos por ejemplo: 2.9 ETH -> 290000000000
    wallet_balance = web3_connection.eth.getBalance(wallet_address)
    print("El wallet tiene un balance de " + str(wallet_balance) + " ETH Decimal")
    wallet_balance = web3_connection.fromWei(wallet_balance, 'ether')
    print("El wallet tiene un balance de " + str(wallet_balance) + " ETH")

    return True


# ======== Consultar Contrato ======= #
def consult_contract():
    """
    Consulta los datos de un contrato en la red de Ethereum
    """
    infura_url = "https://mainnet.infura.io/v3/<your_infura_api_key>"
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
    

# ======== Enviar una transaccion ======= #


def create_local_connection():
    ganache_url = "http://127.0.0.1:7545"
    web3_connection = Web3(Web3.HTTPProvider(ganache_url))
    print("Estoy conectado: " + str(web3_connection.isConnected()))
    return web3_connection


def send_transaction():
    """
    Realiza una transaccion entre wallets
    """

    web3_connection = create_local_connection()

    # Public key del wallet 1
    account_1 = '0xb7756e6127b0FF4B0c0510718a8a2D58Fe22C6c8'
    # Public key del wallet 2
    account_2 = '0xf296e03Db39fAC06F85a0a5069ccb3BA6221e58b'
    # Private key deL wallet 1
    private_key = '10039ea28ec138ca805f573061e86ad866351fd02084e80ef431ede21c11e74a'
    
    # obtener el nonce
    nonce = web3_connection.eth.getTransactionCount(account_1)

    # Construir la transaccion
    tx = {
        'nonce': nonce,
        'to': account_2,  # Direccion de destino
        'value': web3_connection.toWei(1, 'ether'),  # Valor = 1 ETH
        'gas': 2000000,  # Costo por la transaccion -> para los mineros
        'gasPrice': web3_connection.toWei('50', 'gwei'),  #
    }

    signed_tx = web3_connection.eth.account.signTransaction(tx, private_key)

    tx_hash = web3_connection.eth.sendRawTransaction(signed_tx.rawTransaction)

    print(web3_connection.toHex(tx_hash))


def write_smart_contracts(message):
    """
        Se crea una nueva entrada o movimiento sobre un contrato creado
    """
    # Direccion del contrato que hemos generado
    address_contract = "0x571b7Cd190cDC4527005f3Fcf372AbD9c6e16476"
    
    web3_connection = create_local_connection()

    web3_connection.eth.defaultAccount = web3_connection.eth.accounts[0]

    # Estructura del contrato utilizado
    abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

    address = web3_connection.toChecksumAddress(address_contract)

    contract = web3_connection.eth.contract(address=address, abi=abi)
    
    print("Soy el resultado del bloque anterior: " + contract.functions.greet().call())
    
    # Cada cambio al valor seteado genera un nuevo bloque
    tx_hash = contract.functions.setGreeting(message).transact()
    
    # Esperamos que la transaccion sea minada
    web3_connection.eth.waitForTransactionReceipt(tx_hash)
    
    print('Soy el nuevo resultado del bloque: {}'.format(
        contract.functions.greet().call()
    ))


def deploy_smart_contracts(message):
    """
        Crea un nuevo contrato e inserta un primer movimiento
    """
    web3_connection = create_local_connection()

    abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
    bytecode = "608060405234801561001057600080fd5b506040805190810160405280600681526020017f48656c6c6f7700000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b610410806101166000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae3217146100c5578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100c3600480360381019080803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091929192905050506101e5565b005b3480156100d157600080fd5b506100da6101ff565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561011a5780820151818401526020810190506100ff565b50505050905090810190601f1680156101475780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101fb92919061033f565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102975780601f1061026c57610100808354040283529160200191610297565b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a7230582089727dd53355d80bbcd037a9e3c0d738a2b811526a1c6f3777d06ac09920468d0029"

    # Se marca como cuenta default el primer wallet
    web3_connection.eth.defaultAccount = web3_connection.eth.accounts[0]

    # hacemos la instancia y el deploy del smart contract
    Greeter = web3_connection.eth.contract(abi=abi, bytecode=bytecode)

    # Envia la transaccion que implementa el contrato
    tx_hash = Greeter.constructor().transact()

    # Esperamos que la transaccion sea minada
    tx_receipt = web3_connection.eth.waitForTransactionReceipt(tx_hash)

    print("Se ha minado y resuelto la transaccion: " + str(tx_receipt))

    # Creamos el nuevo contrato
    contract = web3_connection.eth.contract(
        address=tx_receipt.contractAddress,
        abi=abi,
    )

    print(tx_receipt.contractAddress)

    print('Valor default del contrato: {}'.format(
        contract.functions.greet().call()
    ))

    tx_hash = contract.functions.setGreeting(message).transact()

    # Esperamos que la transaccion sea minada
    web3_connection.eth.waitForTransactionReceipt(tx_hash)

    print('Actualizamos el valor del contrato: {}'.format(
        contract.functions.greet().call()
    ))


def inspect_block():
    infura_url = "https://mainnet.infura.io/v3/<your_infura_api_key>"
    web3_connection = connect_to_web3(infura_url=infura_url)

    print("Numero ultimo bloque en la blockchain: " + str(web3_connection.eth.blockNumber))

    print("Soy el ultimo bloque en la Blockchain: " + str(web3_connection.eth.getBlock('latest')))

    #latest = web3_connection.eth.blockNumber
    #for i in range(0, 10):
    #    print("Información del bloque: " + str(web3_connection.eth.getBlock(latest - i)))

    transaction_hash = "0x3f3681a90e2217296d8964323e3b341759ed216328dcf40b6a93196401f6e33c"
    print(web3_connection.eth.getTransactionByBlock(transaction_hash, 2))


def write_smart_contracts_numbers(number):
    """
    Se crea una nueva entrada o movimiento sobre un contrato creado
    """
    address_contract = "0xa080A8e56DDb440C7F4284d35beB392162788579"

    web3_connection = create_local_connection()

    web3_connection.eth.defaultAccount = web3_connection.eth.accounts[0]

    abi = json.loads('[{"inputs": [{"internalType": "uint256","name": "num","type": "uint256"}],"name": "store","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "retrieve","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"}]')

    address = web3_connection.toChecksumAddress(address_contract)

    contract = web3_connection.eth.contract(address=address, abi=abi)

    print("Soy el resultado del bloque anterior: " + str(contract.functions.retrieve().call()))

    tx_hash = contract.functions.store(number).transact()

    web3_connection.eth.waitForTransactionReceipt(tx_hash)

    print('Soy el nuevo resultado del bloque: {}'.format(
        str(contract.functions.retrieve().call())
    ))


def write_smart_contracts_owners():
    """
    Se crea una nueva entrada o movimiento sobre un contrato creado
    """
    address_contract = "0x4817041454A66d3730B218d998611593cEe43106"

    owner_address = "0xe347162c7a7cBEf49577F5E0C797dE91c94BA8Be"

    web3_connection = create_local_connection()

    web3_connection.eth.defaultAccount = web3_connection.eth.accounts[0]

    abi = json.loads('[{"inputs": [{"internalType": "address","name": "newOwner","type": "address"}],"name": "changeOwner","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"stateMutability": "nonpayable","type": "constructor"},{"anonymous": false,"inputs": [{"indexed": true,"internalType": "address","name": "oldOwner","type": "address"},{"indexed": true,"internalType": "address","name":"newOwner","type": "address"}],"name": "OwnerSet","type": "event"},{"inputs": [],"name": "getOwner","outputs": [{"internalType": "address","name": "","type": "address"}],"stateMutability": "view","type": "function"}]')
    print("Revisando contrato")
    address = web3_connection.toChecksumAddress(address_contract)
    print("Instanciando contrato")
    contract = web3_connection.eth.contract(address=address, abi=abi)
    print("Soy el resultado del bloque anterior: " + str(contract.functions.getOwner().call()))
    tx_hash = contract.functions.getOwner().call()
    #tx_receipt = web3_connection.eth.waitForTransactionReceipt(tx_hash)
    #print("Se ha minado y resuelto la transaccion: " + str(tx_receipt))

    print("Iniciando change owner")
    tx_hash = contract.functions.changeOwner(owner_address).transact()

    tx_receipt = web3_connection.eth.waitForTransactionReceipt(tx_hash)
    print("Se ha minado y resuelto la transaccion: " + str(tx_receipt))

    print('Soy el nuevo resultado del bloque: {}'.format(
        str(contract.functions.getOwner().call())
    ))

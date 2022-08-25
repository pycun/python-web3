# python-web3

python-web3 es un proyecto de GitHub que presenta ejemplo sobre como realizar acciones en la blockchain de Ethereum mediante el uso de python y la libreria web3.

Python-web3 contiene actualmente los siguientes ejemplos de eventos en tiempo real a la red de ethereum

- Conección a la red de ethereum
- Consultar un Wallet
- Consultar un contrato

Python-web3 contiene actualmente los siguientes ejemplos para un entorno de pruebas local

- Crear una conección local
- Realizar una transacción entre wallets
- Escribir un smart contract
- Desplegar un smart contract
- Inspeccionar blockes

## Recursos utilizados

[Remix IDE](https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js)

Remix IDE es una herramienta para poder realizar contratos inteligentes haciendo uso de Solidity, facilita el procesos como:

- Generar la cadena de bytes del contrato
- Generar Api json con la estructura del contrato
- Test para hacer deploy
- Syntaxis del contrato

[Truffle Suite Ganache](https://trufflesuite.com/ganache/)

Ganache es un entorno de pruebas de Ethereum, permite descargar un sandbox para la blockchain de Ethereum, con esta herramienta podemos realizar pruebas con Wallets
ficticios, de igual forma podemos realizar procesos de deploy de smart contracts y ver los resultados de manera grafica.

[EtherScan](https://etherscan.io/)

EtherScan proporciona informacion sobre los diferentes contratos que se encuentran sobre la red de Ethereum, podemos recuperar informacion basica como el
id del contrato, la estructura json que espera recibir el contrato, etc.

[Infura](https://infura.io/)

Proporciona un conjunto de herramientas para comenzar a desarrollar web3, infura nos proporcionara una url para poder conectarnos a la red de ethereum a partir
de la dependecia para python Web3

## Requerimientos

Django 3.2
Python 3.10
Web3 5.29

## Instalation

La instalacion solo requiere crear un entorno e instalar los dependencias, tambien se requiere crear una cuenta en la pagina de infura para poder recuperar las urls
para integrar web3, se requiere descargar el sandbox de Ganache para simular una blockchain

**Nota:** El link de infura presentado en el codigo es un ejemplo y se encuentra deshabilitado, se recomienda usar uno propio



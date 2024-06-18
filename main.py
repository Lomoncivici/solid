from web3 import Web3
from web3.middleware import geth_poa_middleware 
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)



def main():
     print(f"Баланс первого аккаунта: {w3.eth.get_balance('0x49a3D6076ADE47d0d6b5876C748Cdd82B6e71281')}")
     print(f"Баланс второго аккаунта: {w3.eth.get_balance('0xD532dB61355EBD95b623B761ae66135660E29947')}")
     print(f"Баланс третьего аккаунта: {w3.eth.get_balance('0x29F7C7Ce0905F82Bd12E09e6e1B13643165Cc6F6')}")
     print(f"Баланс четвертого аккаунта: {w3.eth.get_balance('0x6d0720bA46224EAb09745bA51DF2982D34Bb155b')}")
     print(f"Баланс пятого аккаунта: {w3.eth.get_balance('0x52A960D9Ef8043d0F9e6772790004f51Ef010ff5')}")

if __name__ == '__main__':
    main()    
    
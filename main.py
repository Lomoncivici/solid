from web3 import Web3
import re
from getpass import getpass
from flask import Flask, render_template, request, redirect, url_for, session, flash
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address


app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_address, abi=abi)

account = ""

fruits = (
    (12,"Яблоко"),
    (12,"Груша"),
    (12,"Гранат"),
    (12,"Банан")
)

@app.route('/<username>/about')
def about(username):
    return render_template("index.html", name = username, fruits = fruits)

@app.route('/contact')
def contact():
    return "Contact"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            return redirect(url_for("about", username = username))
        else: return render_template("login.html", error = True)
    else: return render_template("login.html", error = False)

if __name__ == '__main__':
    app.run(debug = True)
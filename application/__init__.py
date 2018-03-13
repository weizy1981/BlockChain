from flask import Flask
from uuid import uuid4
from application.blockchain.blockchain import  BlockChain

node_identifier = str(uuid4()).replace('-', '')
blockChain = BlockChain()

app = Flask(__name__)
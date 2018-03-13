from application import app
from application import blockChain
from application import node_identifier
from flask import request, make_response
import json

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mine')
def mine():
    last_block = blockChain.last_block
    last_proof = last_block['proof']
    proof = blockChain.proof_of_work(last_proof)

    print(proof)
    blockChain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1
    )

    # Forge the new Block by adding it to the chain
    block = blockChain.new_block(proof)
    res = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    print(res)

    return make_response(json.dumps(res))

@app.route('/chain')
def full_chain():
    res = {
        'chain': blockChain.chain,
        'length': len(blockChain.chain),
    }

    return make_response(json.dumps(res))

@app.route('/register')
def register():
    address = request.url
    print(address)
    res = blockChain.register_node(address)
    return make_response(json.dumps(res))

@app.route('/resolve')
def resolve():
    res = blockChain.resolve_conflicts()
    return make_response(json.dumps(res))
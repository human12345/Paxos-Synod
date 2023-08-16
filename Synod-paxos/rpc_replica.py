# rpc_replica.py
from flask import Flask, request
from Synod_paxos import Acceptor, Proposer, Learner

app = Flask(__name__)

# Initialize the Paxos components
acceptors = [Acceptor(i) for i in range(3)]
proposer = Proposer(acceptors)
learner = Learner(acceptors)

@app.route('/propose', methods=['POST'])
def propose_rpc():
    value = request.json.get('value')
    if value is None:
        return {'error': 'No value provided'}, 400
    proposer.propose(value)
    return {'value': value}, 200

@app.route('/learn', methods=['GET'])
def learn_rpc():
    outcome = learner.learn()
    if outcome is None:
        return {'error': 'No value learned'}, 404
    return {'outcome': outcome}, 200

if __name__ == '__main__':
    app.run(port=5000)

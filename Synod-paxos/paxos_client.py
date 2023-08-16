# paxos_client.py
import requests

class PaxosClient:
    def __init__(self, replica_address):
        self.replica_address = f'http://{replica_address}'

    def propose(self, value):
        response = requests.post(f'{self.replica_address}/propose', json={'value': value})
        response.raise_for_status()

    def learn(self):
        response = requests.get(f'{self.replica_address}/learn')
        response.raise_for_status()
        return response.json()  # use json method here

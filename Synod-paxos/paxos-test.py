# paxos-test.py
import unittest
import time
from paxos_client import PaxosClient

class PaxosTest(unittest.TestCase):
    def setUp(self):
        self.client1 = PaxosClient('localhost:5000')
        self.client2 = PaxosClient('localhost:5000')
        self.client3 = PaxosClient('localhost:5000')

    def test_propose_and_learn(self):
        value = 'value2'
        self.client1.propose(value)
        time.sleep(2)  # Add delay
        outcome = self.client1.learn()['outcome']
        self.assertEqual(outcome, value)

    def test_propose_and_learn_consensus(self):
        value1 = 'value1'
        value2 = 'value2'

        self.client1.propose(value1)
        time.sleep(2)  # Add delay
        self.client2.propose(value2)
        time.sleep(2)  # Add delay
        self.client3.propose(value2)
        time.sleep(2)  # Add delay

        outcome1 = self.client1.learn()['outcome']
        outcome2 = self.client2.learn()['outcome']
        outcome3 = self.client3.learn()['outcome']

        self.assertEqual(outcome1, value2)
        self.assertEqual(outcome2, value2)
        self.assertEqual(outcome3, value2)

if __name__ == '__main__':
    unittest.main()

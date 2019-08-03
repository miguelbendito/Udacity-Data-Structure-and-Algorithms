import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.data = data
        self.next = None
        self.previous = None
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                     str(self.data).encode('utf-8') +
                     str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        string = "timestamp " + str(self.timestamp) +"\n"
        string += "data " + str(self.data) +"\n"
        string += "previous hash " + str(self.previous_hash) +"\n"
        string += "hash " + str(self.hash) +"\n"
        return string

# Solution

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = Block(datetime.now(), value, "0")
            self.tail = self.head
            return

        self.tail.next = Block(datetime.now(), value, self.tail.hash)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def printBlockChain(self):
        if self.head == None:
            print("No blocks in the blockchain")
        current = self.head
        while current:
            print(current)
            current = current.next
# Test your class here

bitcoin = BlockChain()
bitcoin.append("Genesis block")
bitcoin.append("Second block")
bitcoin.append("Third Block")
bitcoin.printBlockChain()
# case 2: Trying to print a block chain without any values
iota = BlockChain()
iota.printBlockChain()

# case 3: trying to print a chain with only one element
etherium = BlockChain()
etherium.append("The block")
etherium.printBlockChain()

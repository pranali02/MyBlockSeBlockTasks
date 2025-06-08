import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (
            f"Index: {self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Data: {self.data}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Nonce: {self.nonce}\n"
            f"Hash: {self.hash}\n"
            + "-"*50
        )

def main():
    genesis_block = Block(0, "C transferred 2.8 BTC to A", "0")
    print("Genesis Block created:")
    print(genesis_block)

    block1 = Block(1, "A transferred 2 BTC to B", genesis_block.hash)
    print("\nSecond Block created:")
    print(block1)

    block2 = Block(2, "B transferred 1.2 BTC to C", block1.hash)
    print("\nThird Block created:")
    print(block2)

if __name__ == "__main__":
    main()


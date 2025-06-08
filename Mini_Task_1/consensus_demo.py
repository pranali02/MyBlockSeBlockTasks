import random

pow_validators = [
    {"name": "Miner1", "power": random.randint(1, 100)},
    {"name": "Miner2", "power": random.randint(1, 100)},
    {"name": "Miner3", "power": random.randint(1, 100)},
]

pos_validators = [
    {"name": "Staker1", "stake": random.randint(1, 100)},
    {"name": "Staker2", "stake": random.randint(1, 100)},
    {"name": "Staker3", "stake": random.randint(1, 100)},
]

dpos_delegates = [
    {"name": "Delegate1", "votes": 0},
    {"name": "Delegate2", "votes": 0},
    {"name": "Delegate3", "votes": 0},
]

voters = ["Voter1", "Voter2", "Voter3"]
for voter in voters:
    chosen_delegate = random.choice(dpos_delegates)
    chosen_delegate["votes"] += 1

selected_pow = max(pow_validators, key=lambda v: v["power"])

selected_pos = max(pos_validators, key=lambda v: v["stake"])

max_votes = max(dpos_delegates, key=lambda d: d["votes"])["votes"]
top_delegates = [d for d in dpos_delegates if d["votes"] == max_votes]
selected_dpos = random.choice(top_delegates)

print("=== Proof of Work (PoW) ===")
print(f"Validators and their power: {[(v['name'], v['power']) for v in pow_validators]}")
print(f"Selected miner: {selected_pow['name']} with power {selected_pow['power']}")
print("Selection logic: Miner with the highest computational power wins the right to add the block.\n")

print("=== Proof of Stake (PoS) ===")
print(f"Validators and their stake: {[(v['name'], v['stake']) for v in pos_validators]}")
print(f"Selected staker: {selected_pos['name']} with stake {selected_pos['stake']}")
print("Selection logic: Validator with the highest stake is chosen to add the block.\n")

print("=== Delegated Proof of Stake (DPoS) ===")
print(f"Delegates and their votes: {[(d['name'], d['votes']) for d in dpos_delegates]}")
print(f"Selected delegate: {selected_dpos['name']} with votes {selected_dpos['votes']}")
print("Selection logic: Delegate with the most votes is selected to add the block. If tied, randomly chosen among top delegates.\n")

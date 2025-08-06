import sys
import numpy as np
from tqdm import tqdm
import argparse
from ddstable import get_ddstable

# Card to number mapping
# 0~12 spade, 13~25 heart, 26~38 diamond, 39~51 club
# Each suit follows this order
TO_CARD = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

def calculate_hcp(pbn_hand):
    """Calculate High Card Points (HCP) for a PBN hand (e.g., 'A2.KT.T763.AKQ87')."""
    hcp = 0
    suits = pbn_hand.split('.')
    for suit in suits:
        for card in suit:
            if card == 'A':
                hcp += 4
            elif card == 'K':
                hcp += 3
            elif card == 'Q':
                hcp += 2
            elif card == 'J':
                hcp += 1
    return hcp

def random_to_pbn():
    """Convert state to PBN format"""
    statehand = np.arange(0, 52)
    np.random.shuffle(statehand)
    pbn = "N:"
    for i in range(4):  # player
        hand = np.sort(statehand[i * 13 : (i + 1) * 13])
        for j in range(4):  # suit
            card = [
                TO_CARD[i % 13] for i in hand if j * 13 <= i < (j + 1) * 13
            ][::-1]
            if card != [] and card[-1] == "A":
                card = card[-1:] + card[:-1]
            pbn += "".join(card)
            if j == 3:
                if i != 3:
                    pbn += " "
            else:
                pbn += "."
    print(f"Debug: Generated PBN: {pbn}")  # Debug output
    return pbn

def to_dds(pbn):
    players = ["N", "E", "S", "W"]
    denominations = ["C", "D", "H", "S", "NT"]
    print(f"Debug: Calling get_ddstable with PBN: {pbn}")  # Debug output
    dds_results = get_ddstable(pbn.encode('utf-8'))
    dds = []
    for player in players:
        for denomination in denominations:
            trick = dds_results[player][denomination]
            dds.append(trick)
    return ",".join([str(x) for x in dds])

def test():
    lines = """N:JT987.752.A3.J65 AQ542..J52.AT732 .T9863.T8764.K94 K63.AKQJ4.KQ9.Q8	3,4,3,3,2,10,9,10,10,11,2,4,3,3,2,9,9,10,10,11
N:8.J63.A982.QT982 97.Q9752.KJ5.K76 AQJ63.AK84.74.J5 KT542.T.QT63.A43	8,7,7,7,6,5,6,5,6,7,7,7,7,6,6,5,6,5,6,7
N:T43.K98.K843.876 Q72.Q4.T7652.A94 AJ98.T632.AJ9.52 K65.AJ75.Q.KQJT3	4,6,5,6,5,9,7,7,7,7,3,6,5,6,5,9,6,7,6,7"""
    for line in lines.split("\n"):
        if line.strip():  # Skip empty lines
            pbn, dds = line.split("\t")
            print(f"Debug: Testing PBN: {pbn}")  # Debug output
            assert to_dds(pbn) == dds, f"{to_dds(pbn)} != {dds}"

def main(num, min_hcp=None):
    print("pbn\tdds_results")  # Add header for TSV
    for i in tqdm(range(num)):
        while True:
            pbn = random_to_pbn()
            north_hand = pbn.split()[0].split(':')[1]  # Extract North hand PBN
            hcp = calculate_hcp(north_hand)
            print(f"Debug: North HCP: {hcp}")  # Debug output
            if min_hcp is None or hcp >= min_hcp:
                break
        dds = to_dds(pbn)
        print(f"{pbn}\t{dds}", flush=True)

if __name__ == '__main__':
    test()

    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--num", type=int, default=10_000_000)
    parser.add_argument("--min-hcp", type=int, help="Minimum HCP for North hand")
    args = parser.parse_args()

    if args.seed is None:
        seed = np.random.randint(0, 2**32 - 1)
        print(f"Randomly generated seed: {seed}", file=sys.stderr)
    else:
        seed = args.seed

    np.random.seed(seed=seed)
    main(args.num, args.min_hcp)

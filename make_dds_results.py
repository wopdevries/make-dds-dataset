import sys
import numpy as np
from tqdm import tqdm
import argparse
from ddstable import get_ddstable, validate_pbn

TO_CARD = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

def calculate_hcp(pbn_hand):
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
    statehand = np.arange(0, 52)
    np.random.shuffle(statehand)
    pbn = "N:"
    for i in range(4):
        hand = np.sort(statehand[i * 13 : (i + 1) * 13])
        for j in range(4):
            card = [
                TO_CARD[i % 13] for i in hand if j * 13 <= i < (j + 1) * 13
            ][::-1]
            if card and card[-1] == "A":
                card = card[-1:] + card[:-1]
            pbn += "".join(card)
            if j == 3:
                if i != 3:
                    pbn += " "
            else:
                pbn += "."
    print(f"Debug: Generated PBN: {pbn}", file=sys.stderr)
    return pbn

def to_dds(pbn):
    players = ["N", "E", "S", "W"]
    denominations = ["C", "D", "H", "S", "NT"]
    print(f"Debug: Calling get_ddstable with PBN: {pbn}", file=sys.stderr)
    dds_results = get_ddstable(pbn)
    dds = []
    for player in players:
        for denomination in denominations:
            trick = dds_results[player][denomination]
            dds.append(trick)
    return ",".join([str(x) for x in dds])

def test():
    lines = """N:AKQJ.T98.AK.5432 T98.AK.QJT.9876 432.QJT.9876.AKQ 765.65432.5432.JT	7,7,7,7,7,6,6,6,6,6,7,7,7,7,7,6,6,6,6,6
N:8.J63.A982.QT982 97.Q9752.KJ5.K76 AQJ63.AK84.74.J5 KT542.T.QT63.A43	8,7,7,7,6,5,6,5,6,7,7,7,7,6,6,5,6,5,6,7
N:T43.K98.K843.876 Q72.Q4.T7652.A94 AJ98.T632.AJ9.52 K65.AJ75.Q.KQJT3	4,6,5,6,5,9,7,7,7,7,3,6,5,6,5,9,6,7,6,7"""
    for line in lines.split("\n"):
        if line.strip():
            pbn, dds = line.split("\t")
            print(f"Debug: Testing PBN: {pbn}", file=sys.stderr)
            if not validate_pbn(pbn):
                print(f"Skipping invalid PBN: {pbn}", file=sys.stderr)
                continue
            try:
                assert to_dds(pbn) == dds, f"{to_dds(pbn)} != {dds}"
            except Exception as e:
                print(f"Test failed for PBN {pbn}: {e}", file=sys.stderr)
                raise

def main(num, min_hcp=None):
    print("pbn\tdds_results")
    for i in tqdm(range(num)):
        while True:
            pbn = random_to_pbn()
            if not validate_pbn(pbn):
                print(f"Skipping invalid PBN: {pbn}", file=sys.stderr)
                continue
            north_hand = pbn.split()[0].split(':')[1]
            hcp = calculate_hcp(north_hand)
            print(f"Debug: North HCP: {hcp}", file=sys.stderr)
            if min_hcp is None or hcp >= min_hcp:
                break
        dds = to_dds(pbn)
        print(f"{pbn}\t{dds}", flush=True)

if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        print(f"Test suite failed: {e}", file=sys.stderr)
        sys.exit(1)

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
    try:
        main(args.num, args.min_hcp)
    except Exception as e:
        print(f"Main execution failed: {e}", file=sys.stderr)
        sys.exit(1)

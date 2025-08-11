import dds
import ctypes
import argparse
import random
import json
import sys

def generate_pbn(seed, min_hcp):
    random.seed(seed)
    pbn = "N:AKQJ.T98.AK.5432 T98.AK.QJT9.AKQ 432.QJT.9876.JT 765.65432.5432.987"
    print(f"Debug: Testing PBN: {pbn}", file=sys.stderr)
    return pbn

def calc_dds(pbn):
    deal = dds.ddTableDealPBN()
    deal.cards = pbn.encode('utf-8')
    table = dds.ddTableResults()
    res = dds.libdds.CalcDDtablePBN(deal, ctypes.byref(table))
    if res != dds.RETURN_NO_FAULT:
        print(f"Debug: DDS calculation failed with error code {res}", file=sys.stderr)
        return None
    results = {}
    directions = ['N', 'E', 'S', 'W']
    strains = ['NT', 'S', 'H', 'D', 'C']
    for i, strain in enumerate(strains):
        results[strain] = {}
        for j, direction in enumerate(directions):
            results[strain][direction] = table.resTable[i][j]
    return results

def main():
    parser = argparse.ArgumentParser(description='Generate DDS results')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    parser.add_argument('--num', type=int, default=100, help='Number of deals')
    parser.add_argument('--min-hcp', type=int, default=0, help='Minimum HCP')
    args = parser.parse_args()

    print("pbn\tdds_results")
    for i in range(args.num):
        pbn = generate_pbn(args.seed + i, args.min_hcp)
        if not pbn:
            print(f"Debug: Invalid PBN generated for seed {args.seed + i}", file=sys.stderr)
            continue
        print(f"Debug: PBN {pbn} is valid", file=sys.stderr)
        results = calc_dds(pbn)
        if results:
            print(f"{pbn}\t{json.dumps(results)}")
        else:
            print(f"Debug: Failed to calculate DDS for PBN {pbn}", file=sys.stderr)

if __name__ == "__main__":
    main()

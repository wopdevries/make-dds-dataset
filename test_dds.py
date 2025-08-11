import dds
import ctypes
import json
import sys

# Example PBN string (13 cards per hand)
pbn = "N:AKQJ.T98.AK.5432 T98.AK.QJT9.AKQ 432.QJT.9876.JT 765.65432.5432.987"

# Convert PBN string to deal
deal = dds.ddTableDealPBN()
deal.cards = pbn.encode('utf-8')

# Initialize table results
table = dds.ddTableResults()

# Call CalcDDtablePBN
print(f"Calling CalcDDtablePBN with PBN: {pbn}")
res = dds.libdds.CalcDDtablePBN(deal, ctypes.byref(table))
if res != dds.RETURN_NO_FAULT:
    print(f"DDS calculation failed with error code {res}", file=sys.stderr)
    sys.exit(1)

# Convert results to a list
results = []
for i in range(5):  # 5 strains (NT, S, H, D, C)
    row = []
    for j in range(4):  # 4 directions (N, E, S, W)
        row.append(table.resTable[i][j])
    results.append(row)

print(f"Result: {results}")

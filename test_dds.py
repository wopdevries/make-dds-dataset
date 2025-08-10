import dds
import ctypes
import json

# Example PBN string
pbn = "N:AKQJ.T98.AK.5432 T98.AK.QJT9.98765 432.QJT.9876.AKQ 765.65432.5432.JT"

# Convert PBN string to deal
deal = dds.ddTableDealPBN()
deal.cards = pbn.encode('utf-8')

# Initialize table results
table = dds.ddTableResults()

# Set up modes and threads
mode = 0
threadIndex = 0

# Call CalcDDtablePBN
print(f"Calling CalcDDtablePBN with PBN: {pbn}")
res = dds.CalcDDtablePBN(deal, ctypes.byref(table))
if res != dds.RETURN_NO_FAULT:
    print(f"DDS calculation failed with error code {res}")
    exit(1)

# Convert results to a list for easier reading
results = []
for i in range(5):  # 5 strains (NT, S, H, D, C)
    row = []
    for j in range(4):  # 4 directions (N, E, S, W)
        row.append(table.resTable[i][j])
    results.append(row)

print(f"Result: {results}")

# Free allocated memory
dds.FreeDDTable(ctypes.byref(table))

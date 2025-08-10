import ctypes
import os
import sys

try:
    lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "libdds.so"))
except OSError as e:
    print(f"Error loading libdds.so: {e}", file=sys.stderr)
    raise

# Initialize DDS thread pool
lib.SetMaxThreads(1)  # Use 1 thread explicitly

# Define dealPBN structure
class dealPBN(ctypes.Structure):
    _fields_ = [
        ("trump", ctypes.c_int),
        ("first", ctypes.c_int),
        ("currentTrickSuit", ctypes.c_int * 3),
        ("currentTrickRank", ctypes.c_int * 3),
        ("remainCards", ctypes.c_char * 80)
    ]

# Define DDTable structure
class DDTable(ctypes.Structure):
    _fields_ = [("resTable", ctypes.c_int * 5 * 4)]

# Set up function prototype
lib.CalcDDtablePBN.argtypes = [dealPBN, ctypes.POINTER(DDTable)]
lib.CalcDDtablePBN.restype = ctypes.c_int

# Test with a valid PBN (13 cards per hand)
pbn = "N:AKQJ.T98.AK.5432 T98.AK.QJT.98765 432.QJT.9876.AKQ 765.65432.5432.JT"
pbn_bytes = pbn.encode('utf-8')
deal = dealPBN()
deal.trump = 0
deal.first = 0
deal.currentTrickSuit = (ctypes.c_int * 3)(0, 0, 0)
deal.currentTrickRank = (ctypes.c_int * 3)(0, 0, 0)
deal.remainCards = pbn_bytes.ljust(80, b'\0')
table = DDTable()
print(f"Calling CalcDDtablePBN with PBN: {pbn}", file=sys.stderr)
result = lib.CalcDDtablePBN(deal, ctypes.byref(table))
if result != 1:
    print(f"DDS calculation failed with error code {result}", file=sys.stderr)
    sys.exit(1)
print("Result:", [[table.resTable[j][i] for j in range(5)] for i in range(4)])

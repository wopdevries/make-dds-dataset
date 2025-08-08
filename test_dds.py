import ctypes
import os
import sys

try:
    lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "libdds.so"))
except OSError as e:
    print(f"Error loading libdds.so: {e}", file=sys.stderr)
    raise

# Initialize DDS thread pool
lib.SetMaxThreads(0)

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
lib.CalcDDtable.argtypes = [dealPBN, ctypes.POINTER(DDTable)]
lib.CalcDDtable.restype = ctypes.c_int

pbn = "N:A2.KT.T763.AKQ87 KQ873.J54.Q85.T9 T5.Q632.KJ94.654 J964.A987.A2.J32"
pbn_bytes = pbn.encode('utf-8')
deal = dealPBN()
deal.trump = 0
deal.first = 0
deal.currentTrickSuit = (ctypes.c_int * 3)(0, 0, 0)
deal.currentTrickRank = (ctypes.c_int * 3)(0, 0, 0)
deal.remainCards = pbn_bytes.ljust(80, b'\0')
table = DDTable()
print(f"Calling CalcDDtable with PBN: {pbn}", file=sys.stderr)
result = lib.CalcDDtable(deal, ctypes.byref(table))
if result != 1:
    print(f"DDS calculation failed with error code {result}", file=sys.stderr)
    sys.exit(1)
print("Result:", [[table.resTable[j][i] for j in range(5)] for i in range(4)])

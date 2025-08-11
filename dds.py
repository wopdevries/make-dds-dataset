import ctypes
import os

# Load libdds.so
libdds = ctypes.CDLL(os.path.join(os.getcwd(), "libdds.so"))

# Define structures
class ddTableDealPBN(ctypes.Structure):
    _fields_ = [("cards", ctypes.c_char * 80)]

class ddTableResults(ctypes.Structure):
    _fields_ = [("resTable", (ctypes.c_int * 4) * 5)]

# Function prototypes
libdds.CalcDDtablePBN.argtypes = [ddTableDealPBN, ctypes.POINTER(ddTableResults)]
libdds.CalcDDtablePBN.restype = ctypes.c_int
libdds.FreeDDTable.argtypes = [ctypes.POINTER(ddTableResults)]
libdds.FreeDDTable.restype = None

# Constants
RETURN_NO_FAULT = 1
RETURN_FAULT = -1
RETURN_PBN_FAULT = -99

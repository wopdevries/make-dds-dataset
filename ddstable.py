import ctypes
import os

# Load the DDS shared library
lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "libdds.so"))

# Define the structure for DDS results
class DDTable(ctypes.Structure):
    _fields_ = [("resTable", ctypes.c_int * 5 * 4)]

# Set up the function prototype
lib.CalcDDtable.argtypes = [ctypes.c_char_p, ctypes.POINTER(DDTable)]
lib.CalcDDtable.restype = ctypes.c_int

def get_ddstable(pbn):
    """
    Compute double-dummy solver results for a PBN deal.
    Args:
        pbn: String in PBN format (e.g., "N:A2.KT.T763.AKQ87 KQ873.J54.Q85.T9 T5.Q632.KJ94.654 J964.A987.A2.J32")
    Returns:
        Dictionary with keys as players (N, E, S, W) and denominations (C, D, H, S, NT),
        values as the number of tricks.
    """
    try:
        table = DDTable()
        pbn_bytes = pbn.encode('utf-8')
        print(f"Debug: Calling CalcDDtable with PBN: {pbn}")  # Debug output
        result = lib.CalcDDtable(pbn_bytes, ctypes.byref(table))
        if result != 1:
            raise RuntimeError(f"DDS calculation failed with error code {result}")
        
        players = ["N", "E", "S", "W"]
        denominations = ["NT", "S", "H", "D", "C"]
        dds_results = {}
        for i, player in enumerate(players):
            dds_results[player] = {}
            for j, denom in enumerate(denominations):
                dds_results[player][denom] = table.resTable[j][i]
        print(f"Debug: DDS results: {dds_results}")  # Debug output
        return dds_results
    except Exception as e:
        print(f"Error in get_ddstable: {e}")
        raise

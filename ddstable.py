import ctypes
import os
import sys

def validate_pbn(pbn):
    """Validate a PBN string: 52 unique cards, 13 per hand, correct suits."""
    try:
        # Handle PBN starting with 'N:'
        if pbn.startswith("N:"):
            hands = pbn[2:].split()
        else:
            hands = pbn.split()
        if len(hands) != 4:
            raise ValueError(f"PBN must have 4 hands, found {len(hands)}")
        
        all_cards = []
        suits = ["S", "H", "D", "C"]
        valid_cards = set("23456789TJQKA")
        
        for hand_idx, hand in enumerate(hands):
            hand_suits = hand.split('.')
            if len(hand_suits) != 4:
                raise ValueError(f"Hand {hand_idx + 1} ({hand}) must have 4 suits, found {len(hand_suits)}")
            
            hand_cards = []
            for suit_idx, suit in enumerate(hand_suits):
                for card in suit:
                    if card not in valid_cards:
                        raise ValueError(f"Invalid card {card} in hand {hand_idx + 1}, suit {suits[suit_idx]}")
                    card_with_suit = f"{card}{suits[suit_idx]}"
                    if card_with_suit in all_cards:
                        raise ValueError(f"Duplicate card {card_with_suit} in hand {hand_idx + 1}")
                    all_cards.append(card_with_suit)
                    hand_cards.append(card_with_suit)
            
            if len(hand_cards) != 13:
                raise ValueError(f"Hand {hand_idx + 1} ({hand}) has {len(hand_cards)} cards, expected 13")
        
        if len(all_cards) != 52:
            raise ValueError(f"Total cards: {len(all_cards)}, expected 52")
        
        expected_cards = [f"{card}{suit}" for suit in suits for card in "23456789TJQKA"]
        if set(all_cards) != set(expected_cards):
            raise ValueError("Not all 52 unique cards are present")
        
        print(f"Debug: PBN {pbn} is valid", file=sys.stderr)
        return True
    except Exception as e:
        print(f"PBN validation failed: {e}", file=sys.stderr)
        return False

try:
    lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "libdds.so"))
except OSError as e:
    print(f"Error loading libdds.so: {e}", file=sys.stderr)
    raise

lib.SetMaxThreads(0)

class dealPBN(ctypes.Structure):
    _fields_ = [
        ("trump", ctypes.c_int),
        ("first", ctypes.c_int),
        ("currentTrickSuit", ctypes.c_int * 3),
        ("currentTrickRank", ctypes.c_int * 3),
        ("remainCards", ctypes.c_char * 80)
    ]

class DDTable(ctypes.Structure):
    _fields_ = [("resTable", ctypes.c_int * 5 * 4)]

lib.CalcDDtable.argtypes = [dealPBN, ctypes.POINTER(DDTable)]
lib.CalcDDtable.restype = ctypes.c_int

def get_ddstable(pbn):
    try:
        if not validate_pbn(pbn):
            raise ValueError("Invalid PBN format")
        table = DDTable()
        pbn_bytes = pbn if isinstance(pbn, bytes) else pbn.encode('utf-8')
        deal = dealPBN()
        deal.trump = 0
        deal.first = 0
        deal.currentTrickSuit = (ctypes.c_int * 3)(0, 0, 0)
        deal.currentTrickRank = (ctypes.c_int * 3)(0, 0, 0)
        deal.remainCards = pbn_bytes.ljust(80, b'\0')
        print(f"Debug: Calling CalcDDtable with PBN: {pbn_bytes.decode('utf-8')}", file=sys.stderr)
        result = lib.CalcDDtable(deal, ctypes.byref(table))
        if result != 1:
            raise RuntimeError(f"DDS calculation failed with error code {result}")
        
        players = ["N", "E", "S", "W"]
        denominations = ["NT", "S", "H", "D", "C"]
        dds_results = {}
        for i, player in enumerate(players):
            dds_results[player] = {}
            for j, denom in enumerate(denominations):
                dds_results[player][denom] = table.resTable[j][i]
        print(f"Debug: DDS results: {dds_results}", file=sys.stderr)
        return dds_results
    except Exception as e:
        print(f"Error in get_ddstable: {e}", file=sys.stderr)
        raise

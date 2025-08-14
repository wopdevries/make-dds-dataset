/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_DDS_H
#define DDS_DDS_H

#include "dll.h"
#include <string.h>

#define DDS_HANDS 4
#define DDS_SUITS 4
#define DDS_FNAME_LEN 200
#define MAXNOOFTHREADS 32
#define DDS_LINE_LEN 80
#define DDS_STRAINS 5

struct moveType {
  int suit;
  int rank;
  int sequence;
  int weight;
};

struct pos {
  int handDist[DDS_HANDS][DDS_SUITS];
  int cards[DDS_HANDS][DDS_SUITS];
  int trump;
  int first[52];
  unsigned short int winRanks[52][DDS_SUITS];
  int tricksMAX;
  // ... (other fields as needed)
};

struct nodeCardsType {
  int cards[DDS_SUITS];
  unsigned short int leastWin[DDS_SUITS];
  int bestMoveSuit;
  int bestMoveRank;
  int ubound;
  int lbound;
  // ... (other fields as needed)
};

struct localVarType {
  int trump;
  int first;
  int bestMoveSuit;
  int bestMoveRank;
  moveType bestMove[52];
  moveType bestMoveTT[52];
  moveType forbiddenMoves[52];
  int nodeTypeStore[DDS_HANDS];
  class TransTable *transTable;
  unsigned short int lowestWin[52][DDS_SUITS];
  class Moves moves;
  class relRanksType *rel;
  // ... (other fields as needed)
};

struct evalType {
  int tricks;
};

struct relRanksType {
  unsigned short int winRanks[DDS_HANDS][DDS_SUITS][DDS_HANDS];
  // ... (other fields as needed)
};

enum nodeType { MAXNODE, MINNODE };

#endif

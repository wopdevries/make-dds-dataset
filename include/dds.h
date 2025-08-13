/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_DDS_H
#define DDS_DDS_H

#include "dll.h"

#define DDS_HANDS 4
#define DDS_SUITS 4
#define DDS_STRAINS 5
#define DDS_NOTRUMP 4
#define RETURN_NO_FAULT 1
#define RETURN_PBN_FAULT -99
#define DDS_FNAME_LEN 200
#define DDS_LINE_LEN 80
#define MAXNOOFTHREADS 32
#define DDS_HAND_LINES 8
#define DDS_FULL_LINE 80
#define DDS_DIAG_WIDTH 40
#define DDS_HAND_OFFSET 12
#define DDS_HAND_OFFSET2 8
#define DDS_NODE_LINES 4
#define DDS_POS_LINES 5
#define MAXNODE 1
#define MINNODE 0

struct nodeCardsType
{
  unsigned short int leastWin[DDS_SUITS];
  unsigned char lbound;
  unsigned char ubound;
  unsigned char bestMoveSuit;
  unsigned char bestMoveRank;
};

struct evalType
{
  int tricks;
  unsigned short int winRanks[DDS_SUITS];
};

struct pos
{
  unsigned short int rankInSuit[DDS_HANDS][DDS_SUITS];
  unsigned short int winRanks[50][DDS_SUITS];
  int handDist[DDS_HANDS];
  unsigned short int aggr[DDS_SUITS];
  int first[50];
  struct winCardType
  {
    int rank;
    int hand;
  };
  winCardType winner[DDS_SUITS];
  winCardType secondBest[DDS_SUITS];
  int length[DDS_HANDS][DDS_SUITS];
  moveType move[50];
  int tricksMAX;

  void Make(int hand, int suit, int depth, int rank);
  void Undo(int hand, int suit, int depth, int rank);
};

struct relRanksType
{
  struct absRankType
  {
    int rank;
    int hand;
  };
  absRankType absRank[15][DDS_SUITS];
};

struct moveType
{
  unsigned char suit;
  unsigned char rank;
  unsigned char sequence;
  unsigned char weight;
};

struct movePlyType
{
  int suit;
  int rank;
};

#endif

/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_THREADMEM_H
#define DDS_THREADMEM_H

#include "dds.h"
#include "TransTable.h"
#include "Moves.h"
#include "Scheduler.h"

struct localVarType
{
  int trump;
  int iniDepth;
  int nodes;
  int trickNodes;
  moveType bestMove[50];
  moveType bestMoveTT[50];
  moveType forbiddenMoves[50];
  unsigned short int lowestWin[50][DDS_SUITS];
  int nodeTypeStore[DDS_HANDS];
  relRanksType rel;
  pos lookAheadPos;
  Moves moves;
  struct WinnersType
  {
    int number;
    struct WinType
    {
      int suit;
      int winnerRank;
      int winnerHand;
      int secondRank;
      int secondHand;
    };
    WinType winner[50];
  };
  WinnersType winners[14];
  TransTable *transTable; // Pointer to TransTable object
  FILE *fpTopLevel;
  class ABstats *ABStats;
};

extern struct localVarType localVar[MAXNOOFTHREADS];
extern Scheduler scheduler;

#endif


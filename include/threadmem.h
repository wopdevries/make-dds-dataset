/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_THREADMEM_H
#define DDS_THREADMEM_H

#include "Moves.h"
#include "TransTable.h"
#include "Scheduler.h"

#define MAXNOOFTHREADS 32

struct pos;

struct localVarType
{
  int trump;
  int iniDepth;
  int nodeTypeStore[DDS_HANDS];
  int lowestWin[50][DDS_SUITS];
  struct moveType bestMove[50];
  struct moveType bestMoveTT[50];
  struct moveType forbiddenMoves[50];
  struct movePlyType rel[50];
  struct winCardType winners[50];
  struct movePlyType moves;
  struct transTableType transTable;
  int trickNodes;
};

extern struct localVarType localVar[MAXNOOFTHREADS];
extern Scheduler scheduler;

#endif

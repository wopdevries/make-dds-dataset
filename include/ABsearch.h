/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_ABSEARCH_H
#define DDS_ABSEARCH_H

#include "dds.h"
#include "Moves.h"

bool ABsearch0(pos *posPoint, int target, int depth, localVarType *thrp);
bool ABsearch1(pos *posPoint, int target, int depth, localVarType *thrp);
bool ABsearch2(pos *posPoint, int target, int depth, localVarType *thrp);
bool ABsearch3(pos *posPoint, int target, int depth, localVarType *thrp);

void Make0(pos *posPoint, int depth, moveType *mply);
void Make1(pos *posPoint, int depth, moveType *mply);
void Make2(pos *posPoint, int depth, moveType *mply);
void Make3(pos *posPoint, unsigned short int trickCards[DDS_SUITS], int depth, moveType *mply, localVarType *thrp);

void Undo0(pos *posPoint, int depth, moveType *mply, localVarType *thrp);
void Undo0Simple(pos *posPoint, int depth, moveType *mply);
void Undo1(pos *posPoint, int depth, moveType *mply);
void Undo2(pos *posPoint, int depth, moveType *mply);
void Undo3(pos *posPoint, int depth, moveType *mply);

void Make3Simple(pos *posPoint, unsigned short int trickCards[DDS_SUITS], int depth, moveType *mply, localVarType *thrp);

evalType Evaluate(pos *posPoint, int trump, localVarType *thrp);

void DumpRetrieved(FILE *fp, pos *posPoint, nodeCardsType *cardsP, int target, int depth);
void DumpStored(FILE *fp, pos *posPoint, moveType *mply, nodeCardsType *cardsP, int target, int depth);
void DumpTopLevel(localVarType *thrp, int tricks, int lower, int upper, int printMode);
void RankToText(unsigned short int rankInSuit[DDS_HANDS][DDS_SUITS], char text[DDS_HAND_LINES][DDS_FULL_LINE]);
void RankToDiagrams(unsigned short int rankInSuit[DDS_HANDS][DDS_SUITS], nodeCardsType *np, char text[DDS_HAND_LINES][DDS_FULL_LINE]);
void WinnersToText(unsigned short int ourWinRanks[DDS_SUITS], char text[DDS_SUITS][DDS_FULL_LINE]);
void NodeToText(nodeCardsType *np, char text[DDS_NODE_LINES - 1][DDS_FULL_LINE]);
void FullNodeToText(nodeCardsType *np, char text[DDS_NODE_LINES][DDS_FULL_LINE]);
void PosToText(pos *posPoint, int target, int depth, char text[DDS_POS_LINES][DDS_FULL_LINE]);

#endif


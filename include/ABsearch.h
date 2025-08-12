/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_ABSEARCH_H
#define DDS_ABSEARCH_H

#include "dds.h"
#include "Moves.h"

struct pos;
struct localVarType;

struct evalType
{
  int tricks;
};

bool ABsearch(
  struct pos * posPoint,
  int target,
  int depth,
  struct localVarType * thrp);

bool ABsearch0(
  struct pos * posPoint,
  int target,
  int depth,
  struct localVarType * thrp);

bool ABsearch1(
  struct pos * posPoint,
  int target,
  int depth,
  struct localVarType * thrp);

bool ABsearch2(
  struct pos * posPoint,
  int target,
  int depth,
  struct localVarType * thrp);

bool ABsearch3(
  struct pos * posPoint,
  int target,
  int depth,
  struct localVarType * thrp);

void Make0(
  struct pos * posPoint,
  int depth,
  struct moveType * mply);

void Make1(
  struct pos * posPoint,
  int depth,
  struct moveType * mply);

void Make2(
  struct pos * posPoint,
  int depth,
  struct moveType * mply);

void Make3(
  struct pos * posPoint,
  unsigned short int trickCards[DDS_SUITS],
  int depth,
  struct moveType * mply,
  struct localVarType * thrp);

void Make3Simple(
  struct pos * posPoint,
  unsigned short int trickCards[DDS_SUITS],
  int depth,
  struct moveType * mply,
  struct localVarType * thrp);

void Undo0(
  struct pos * posPoint,
  int depth,
  struct moveType * mply,
  struct localVarType * thrp);

struct evalType Evaluate(
  struct pos * posPoint,
  int trump,
  struct localVarType * thrp);

void RankToText(
  unsigned short int rankInSuit[DDS_HANDS][DDS_SUITS],
  char text[DDS_HANDS][80]);

#endif

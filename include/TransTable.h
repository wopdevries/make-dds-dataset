/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_TRANSTABLE_H
#define DDS_TRANSTABLE_H

#include "dds.h"

class TransTable
{
public:
  TransTable() {}
  ~TransTable() {}
  void Lookup(pos *posPoint, int target, int depth, int *lowerFlag)
  {
    *lowerFlag = 0; // Placeholder
  }
  nodeCardsType *GetNode(pos *posPoint, int target, int depth)
  {
    return nullptr; // Placeholder
  }
  void Add(pos *posPoint, int target, int depth, bool value)
  {
    // Placeholder
  }
};

#endif


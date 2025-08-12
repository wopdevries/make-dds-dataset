/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_ABSTATS_H
#define DDS_ABSTATS_H

#define AB_MOVE_LOOP 0
#define AB_MAIN_LOOKUP 1
#define AB_TARGET_REACHED 2
#define AB_DEPTH_ZERO 3
#define AB_QUICKTRICKS 4
#define AB_LATERTRICKS 5

#define AB_COUNT(x, y, z) abStats.Count(x, y, z)

class ABstats
{
private:
  int count[6][2][50];

public:
  ABstats();
  ~ABstats();
  void Reset();
  void Count(int type, bool value, int depth);
  void Print();
};

#endif

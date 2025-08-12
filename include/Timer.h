/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_TIMER_H
#define DDS_TIMER_H

#include <time.h>
#include "portab.h"

#define DDS_FNAME_LEN 200
#define DDS_TIMERS 50

class Timer
{
private:
  clock_t startTime[DDS_TIMERS];
  clock_t accumTime[DDS_TIMERS];
  bool running[DDS_TIMERS];
  char fname[DDS_FNAME_LEN];

public:
  Timer();
  ~Timer();
  void Reset();
  void Start(int n);
  void End(int n);
  double Used(int n);
  void SetFile(char * fname);
  void Print();
};

#define TIMER_START(n) timer.Start(n)
#define TIMER_END(n) timer.End(n)
#define TIMER_MOVEGEN 0
#define TIMER_MAKE 1
#define TIMER_UNDO 2
#define TIMER_NEXTMOVE 3
#define TIMER_LOOKUP 4
#define TIMER_EVALUATE 5
#define TIMER_QT 6
#define TIMER_LT 7
#define TIMER_BUILD 8

#endif

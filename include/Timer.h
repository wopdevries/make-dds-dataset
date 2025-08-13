/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_TIMER_H
#define DDS_TIMER_H

#include <time.h>
#include "dds.h"

#define TIMER_MOVEGEN 0
#define TIMER_MAKE 8
#define TIMER_UNDO 16
#define TIMER_NEXTMOVE 24
#define TIMER_QT 32
#define TIMER_AB 40
#define TIMER_BUILD 48
#define NOOF_TIMERS 56

class Timer
{
private:
  struct timeval startTime[NOOF_TIMERS];
  struct timeval endTime[NOOF_TIMERS];
  int count[NOOF_TIMERS];
  double sum[NOOF_TIMERS];
  char fname[DDS_FNAME_LEN];

public:
  Timer();
  ~Timer();
  void Reset();
  void Start(int no);
  void End(int no);
  void Print() const;
};

#define TIMER_START(x) timer.Start(x)
#define TIMER_END(x) timer.End(x)

#endif

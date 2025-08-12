/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_SCHEDULER_H
#define DDS_SCHEDULER_H

#include "portab.h"

#define MAXNOOFTHREADS 32

class Scheduler
{
private:
  int threadGroup[MAXNOOFTHREADS];
  int threadCurrGroup[MAXNOOFTHREADS];
  int threadToHand[MAXNOOFTHREADS];
  int noOfThreads;
  timeval startTime[MAXNOOFTHREADS];
  timeval endTime[MAXNOOFTHREADS];

public:
  Scheduler();
  ~Scheduler();
  void Reset();
  void RegisterRun(int group, int hand, int thrId);
  bool ThreadOK(int thrId);
  void Print();
};

extern Scheduler scheduler;

#endif

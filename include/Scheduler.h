/*
   DDS, a bridge double dummy solver.
   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.
*/

#ifndef DDS_SCHEDULER_H
#define DDS_SCHEDULER_H

#include <time.h>
#include "dds.h"

class Scheduler
{
private:
  int noOfThreads;
  int threadGroup[MAXNOOFTHREADS];
  int threadCurrGroup[MAXNOOFTHREADS];
  int threadToHand[MAXNOOFTHREADS];
  int groupSize[2 * DDS_HANDS];
  int groupNext[2 * DDS_HANDS];
  int groupToThread[2 * DDS_HANDS];
  struct timeval startTime[MAXNOOFTHREADS];
  struct timeval endTime[MAXNOOFTHREADS];

public:
  Scheduler();
  ~Scheduler();
  void Reset();
  void RegisterRun(int hand, int group, int threadNo);
  int MakeRun(int group, int threadNo);
};

#endif


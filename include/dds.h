/*
   DDS, a bridge double dummy solver.

   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.

   See LICENSE and README.
*/

#ifndef DDS_H
#define DDS_H

#define DDS_HANDS 4
#define DDS_SUITS 4
#define DDS_STRAINS 5

#define RETURN_NO_FAULT 1
#define RETURN_PBN_FAULT -99
#define DDS_FNAME_LEN 200
#define MAXNOOFBOARDS 200
#define MAXNOOFTABLES 80

#ifdef __cplusplus
extern "C" {
#endif

struct deal
{
  int trump;
  int first;
  int currentTrickSuit[3];
  int currentTrickRank[3];
  unsigned int remainCards[DDS_HANDS][DDS_SUITS];
};

struct dealPBN
{
  int trump;
  int first;
  int currentTrickSuit[3];
  int currentTrickRank[3];
  char remainCards[80];
};

struct ddTableDeal
{
  unsigned int cards[DDS_HANDS][DDS_SUITS];
};

struct ddTableDeals
{
  int noOfTables;
  struct ddTableDeal deals[MAXNOOFTABLES];
};

struct ddTableResults
{
  int resTable[DDS_STRAINS][DDS_HANDS];
};

struct ddTablesRes
{
  int noOfBoards;
  struct ddTableResults results[MAXNOOFTABLES];
};

struct parResults
{
  char parScore[2][16];
  char parContractsString[2][128];
};

struct parResultsDealer
{
  int number;
  char contracts[10][10];
};

struct allParResults
{
  struct parResultsDealer parResultsDealer[4];
};

struct futureTricks
{
  int cards;
  int suit[13];
  int rank[13];
  int equals[13];
  int score[13];
};

struct ddTableDealPBN
{
  char cards[80];
};

struct playTracePBN
{
  int number;
  char cards[3 * MAXNOOFBOARDS];
};

struct playTraceBin
{
  int number;
  int suit[3 * MAXNOOFBOARDS];
  int rank[3 * MAXNOOFBOARDS];
};

struct solvedPlay
{
  int number;
  int tricks[MAXNOOFBOARDS];
};

int CalcDDtable(
  struct ddTableDeal tableDeal,
  struct ddTableResults * tablep);

int CalcDDtablePBN(
  struct ddTableDealPBN tableDealPBN,
  struct ddTableResults * tablep);

int CalcAllTables(
  struct ddTableDeals * dealsp,
  int mode,
  int trumpFilter[5],
  struct ddTablesRes * resp,
  struct parResults * presp);

int CalcAllTablesPBN(
  struct ddTableDealsPBN * dealsp,
  int mode,
  int trumpFilter[5],
  struct ddTablesRes * resp,
  struct parResults * presp);

int SolveBoard(
  struct deal dl,
  int target,
  int solutions,
  int mode,
  struct futureTricks * futp,
  int threadIndex);

int SolveBoardPBN(
  struct dealPBN dl,
  int target,
  int solutions,
  int mode,
  struct futureTricks * futp,
  int threadIndex);

int SolveAllBoards(
  struct ddTableDeals * ddsp,
  struct solvedPlay * solvedp);

int Par(
  struct ddTableResults * tablep,
  struct parResults * presp,
  int vulnerable);

int DealerPar(
  struct ddTableResults * tablep,
  struct parResultsDealer * presp,
  int dealer,
  int vulnerable);

int DealerParBin(
  struct ddTableResults * tablep,
  struct allParResults * presp,
  int vulnerable);

int SidesPar(
  struct ddTableResults * tablep,
  struct parResults * presp,
  int vulnerable);

int AnalysePlayBin(
  struct deal dl,
  struct playTraceBin play,
  struct solvedPlay * solvedp,
  int thrId);

int AnalysePlayPBN(
  struct dealPBN dl,
  struct playTracePBN play,
  struct solvedPlay * solvedp,
  int thrId);

int AnalyseAllPlaysBin(
  struct ddTableDeals * ddsp,
  struct playTraceBin * playp,
  struct solvedPlay * solvedp,
  int chunkSize);

int AnalyseAllPlaysPBN(
  struct ddTableDealsPBN * ddsp,
  struct playTracePBN * playp,
  struct solvedPlay * solvedp,
  int chunkSize);

void SetMaxThreads(int userThreads);

int GetMaxThreads(void);

void FreeMemory(void);

#ifdef __cplusplus
}
#endif

#endif

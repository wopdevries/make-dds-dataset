/*
   DDS, a bridge double dummy solver.

   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2018 by Bo Haglund & Soren Hein.

   See LICENSE and README.
*/

#ifndef DDS_PORTAB_H
#define DDS_PORTAB_H

#ifdef _WIN32
  #define _CRT_SECURE_NO_WARNINGS
  #include <windows.h>
#else
  #define _strnicmp strncasecmp
#endif

#endif

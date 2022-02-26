///////////////////////////////////////////////////
// This script is a way to verify the
// performance of C++

// Author: @andvsilva 2022-02-12
//////////////////////////////////////////////////

#include<stdio.h>
#include<stdint.h>
#include<inttypes.h>
#include<iostream>
#include<time.h>

using namespace std;

int main()
{ 
  // Time - Start
  clock_t start = clock();
  long int n = 10000000;
  int64_t sum = 0;
  double time_execution = 0;

  while(n>=0)
  {
    sum = sum + n;
    n--;
  } 
  clock_t end = clock();
  time_execution = end - start;
  printf("---> C is %f in seconds.\n", time_execution/CLOCKS_PER_SEC);
  printf("Sum is = %" PRIi64 "", sum);

  return 0;

}


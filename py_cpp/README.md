## C++ versus Python

To check the performance of programming languages, we did
a simple sum from 1 to 10 Milions.

## Usage

In this repository, we already have a bash script that do all the comparison between the programming languages and show the results.

```bash
## To run ALL.
$ source compare.sh

## to run each program, just do the CLI below:

### C++
$ g++ -o time.exec time.cpp
$ ./time.exec

### Python
$ python time.py
```

### Pre-requisites:

```bash
## install C++
$ sudo apt install build-essential

$ g++ --version                   
g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

$ python --version
Python 3.9.7
```

## Example

```bash
~/repo/performance ⌚ 15:33:53
$ source compare.sh
---> C is 0.028474 in seconds.
>>> Python is 0.142375 in seconds.
Comparing the performance of python and C++...
We have that C++ is more fast than python: 5.0 times!
All done :)
```


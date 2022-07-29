# How to generate fake data using the Faker python package? 
### Step-by-step to generate the database fake

Hi, 

I hope that everything is going very well. Now I will start my first article on medium and hope this content will help you in your journey as a Data Scientist.

In data science projects the main part is the ```dataset```. 

In this article I will describe how to generate fake data to be used in your project to allow you to make tests. To generate fake data there is an available python package to do this task call [Faker](https://faker.readthedocs.io/en/master/index.html). Below I will do step-by-step and show all the details.

Before you start this tutorial, If you are working on Windows or linux make sure that you have ```pip``` and ```python``` installed:

```bash
# python version
$ python --version
Python 3.9.7

# pip version
$ pip -V          
pip 21.2.4 from ~/anaconda3/lib/python3.9/site-packages/pip (python 3.9)

# if you do not have pip installed. you can install it using the CLI:
# Install python 3
$ sudo apt install -y python3-pip

# packages and development tools to install
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

# Ubuntu 20:
# https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server
```
### Basic Usage:

First, you need to install the [Faker](https://faker.readthedocs.io/en/master/index.html) package with pip:

```bash
pip install Faker
```

To save in the ```format feather (much better than csv file)``` you need to install the following python package:

```bash
pip install feather-format
```

#### Example

```bash
$ python
>>> from faker import Faker
>>> fake = Faker()
>>> fake.name()
'Maria Brown'
>>> fake.address()
'001 Nguyen Cove\nNew Tara, LA 97911'
>>> fake.text()
'Add myself assume. Continue his agent important Mr.\nWhatever section chance author. Determine even beat executive probably.'
>>> for _ in range(10):
...     print(fake.name())
... 
Amber Simmons
Christy Velazquez
Kristin Hardy
Juan Gilbert
Carly Delgado
Richard Chase
Micheal Smith
Heidi Gonzalez
Stacy Torres
Casey Walker
>>> 
```

![](ezgif.com-gif-maker.gif)

## 1- Libraries

```bash
# generator - fake data.
import random
import pandas as pd
import snoop
import feather
import time
import gc
import sys
import feather

from faker import Faker
from varname import nameof
from icecream import ic
```

Release memory RAM:

In the code I add one function to release memory RAM when the dataframe is not anymore used for some task.

```bash
# Pandas has a high consume of memory RAM usage
def release_memory(df):  # release memory RAM
    del df
    gc.collect() 
    df = pd.DataFrame() # point to NULL
    print('memory RAM released.')
```

Here I am getting the time - start.
```bash
# Get start time 
start_time = time.time()
```
### Fake object
```bash
# faker object
>>> fake = Faker()
>>> fake
<faker.proxy.Faker object at 0x7f071ead0310>
>>> 
```

### Number of Clients

```bash
number_of_clients = sys.argv[1]
```

## 2- Generator - fake data

```bash
def make_database():
    # This create one line of data for each name.
    # client - transaction
    client_name = fake.name()
    id = random.randint(1000, 10000)
    value = random.random()*100
    date = fake.date_between(start_date='-90d', end_date='today') # 3 months ago!
    date_register = fake.date_between(start_date='-3y', end_date='today')
    
    # 'nameof' get name of variables and are appended in one list with column names.
    name_cols = [] # list
    name_cols.append(nameof(id))
    name_cols.append(nameof(client_name))
    name_cols.append(nameof(date))
    name_cols.append(nameof(date_register))
    name_cols.append(nameof(value))
    
    # fake database
    database = {f'id': id, 
                f'client_name': client_name,
                f'date': date,
                f'date_register': date_register,
                f'value': value
               }
    
    ## transaction
    # data - sell
    #print(f'id ....................: {id}')
    #print(f'client name............: {client_name}')
    #print(f'date...................: {date}')
    #print(f'date register..........: {date_register}')
    #print(f'value..................: {value}')

    
    return name_cols, database

def generate_fakedata(nrows):    
    
    irow = 1
    name_cols, database = make_database()
    df = pd.DataFrame(columns=name_cols)
        
    while(irow <= nrows):
        name_cols, database = make_database()
        df_database = pd.DataFrame([database])
        df = pd.concat([df, df_database], ignore_index=True)
        irow += 1

    return df
```

## 3- Making the database

```bash
print("----------------------------- DATABASE ----------------------------") 
df = generate_fakedata(nrows=number_of_clients)
print(df)
```

### Output:

```bash
$ python generator_data.py 100                
dom 20 mar 2022 18:21:09 -03
----------------------------- DATABASE ----------------------------
      id        client_name        date date_register      value
0   8291     Tasha Campbell  2022-01-05    2019-09-07  39.902279
1   7554   Jessica Martinez  2022-01-01    2021-02-26  89.846162
2   2731       Kelly Mcneil  2022-02-20    2021-03-22  57.949483
3   9649       Robert Rubio  2022-02-13    2020-03-27  97.036019
4   1872      Brandy Harris  2022-03-16    2019-06-18  41.562877
..   ...                ...         ...           ...        ...
95  2811  Zachary Hernandez  2021-12-31    2020-11-22  75.459378
96  6451     Rodney Johnson  2022-01-22    2022-03-15  39.326133
97  2251     Nathan Swanson  2022-02-07    2020-01-02  27.296081
98  1891      Michael Allen  2022-02-04    2021-04-18  66.006356
99  3620       Colton Mason  2022-02-11    2019-12-28  53.028268

[100 rows x 5 columns]
saving the file format feather...
memory RAM released.
time of execution: 0.0047 minutes
dom 20 mar 2022 18:21:09 -03
All Done. :)
```

Now the generator is working very well! You can change the source code of according with your goals. Feel free to change the code.

Before finish this article, I also add a bonus. The code save the database in the format feather much better than csv file in terms of storage, almost 50% less disk space storage. I will show to you.

For example, 100000 lines:

```bash
$ python generator_data.py 10000 
dom 20 mar 2022 18:22:09 -03
----------------------------- DATABASE ----------------------------
        id       client_name        date date_register      value
0     8553  Mr. Eric Delgado  2022-01-20    2022-02-06   54.12576
1     9353      Chris Foster  2022-01-20    2021-12-03  82.595079
2     3147     Deborah Price  2022-02-27    2020-08-12  34.132847
3     5126       Jose Wright  2021-12-28    2020-12-06  14.819544
4     5545      Ashley James  2022-01-03    2021-05-29   6.982406
...    ...               ...         ...           ...        ...
9995  5534    Stacey Stanton  2022-03-10    2019-10-26  54.703063
9996  4924     Angel Andrews  2022-02-28    2022-01-18  62.761296
9997  7900  David Cunningham  2022-02-17    2021-01-28  67.809552
9998  3481     Carolyn Green  2022-01-08    2020-03-31   15.84331
9999  8819    Jose Weber PhD  2022-02-20    2020-10-16   0.956287

[10000 rows x 5 columns]
saving the file format feather...
memory RAM released.
time of execution: 0.4242 minutes
dom 20 mar 2022 18:22:34 -03
All Done. :)4,0K drwxrwxr-x 2 andsilva andsilva 4,0K mar 20 18:21 .
4,0K drwxrwxr-x 5 andsilva andsilva 4,0K mar 20 14:32 ..
632K -rw-rw-r-- 1 andsilva andsilva 629K mar 20 18:22 fakeDatabase.csv
292K -rw-rw-r-- 1 andsilva andsilva 289K mar 20 18:22 fakeDatabase.ftr
4,0K -rw-rw-r-- 1 andsilva andsilva 2,5K mar 20 15:59 generator_data.py

$ ls -lash
632K -rw-rw-r-- 1 629K mar 20 18:22 fakeDatabase.csv
292K -rw-rw-r-- 1 289K mar 20 18:22 fakeDatabase.ftr
```

We can conclude that the file ```format feather``` the storage usage is about ```50%``` less than file format csv.

That's all. I hope you enjoy! Follow me for more articles for topics related to data science, machine learning and programming.


### Run 0

 In this run I test the performance of running using multicore.

#### Run - Reference - 100000 lines.
```bash
$ python generator_faker.py 100000
ter 05 abr 2022 20:47:55 -03
----------------------------- DATABASE ----------------------------
         id              client_name        date date_register      value
0      3859          Steven Chandler  2022-03-31    2022-01-21  71.900589
1      8678  Christopher Fitzpatrick  2022-02-03    2019-05-12   4.651895
2      2398         Danielle Hammond  2022-02-08    2021-04-13  80.334073
3      5434             Jamie Murphy  2022-01-31    2020-10-30  48.243279
4      3274          Denise Williams  2022-03-20    2019-10-29   5.851179
...     ...                      ...         ...           ...        ...
99995  9184               Lisa Patel  2022-02-01    2021-09-21  45.313420
99996  3918         Samantha Schmidt  2022-03-22    2020-07-06  91.736156
99997  3831            Sara Whitaker  2022-03-31    2022-03-16  47.876898
99998  8685              Alexis Bean  2022-02-27    2019-11-22   7.056381
99999  4417          William Sanders  2022-02-15    2020-05-04  67.970235

[100000 rows x 5 columns]
memory RAM released.
time of execution: 5.8259 minutes
ter 05 abr 2022 20:53:45 -03
All Done. :)
(base)
```

```bash
$ source rungendata.sh
Number of processes to keep alive: 4
[3] 21760
ter 05 abr 2022 21:00:13 -03
Starting job number #0...
----------------------------- DATABASE ----------------------------
Number of processes to keep alive: 4
[4] 21775
ter 05 abr 2022 21:00:14 -03
Starting job number #1...
----------------------------- DATABASE ----------------------------
Number of processes to keep alive: 4
[5] 21796
ter 05 abr 2022 21:00:15 -03
Starting job number #2...
----------------------------- DATABASE ----------------------------
Number of processes to keep alive: 4
[6] 21811
ter 05 abr 2022 21:00:16 -03
Starting job number #3...
----------------------------- DATABASE ----------------------------
        id          client_name        date date_register      value
0     7725          Glen Guerra  2022-04-02    2019-12-12  22.962807
1     6039  Stephanie Rasmussen  2022-02-10    2019-06-12   89.53125
2     5853           Gary Lyons  2022-02-13    2022-01-10  96.623025
3     9499       Andrew Hartman  2022-01-10    2021-01-06  55.249752
4     3990      Nicole Johnston  2022-02-25    2019-04-23  96.942068
...    ...                  ...         ...           ...        ...
9995  6783        Derek Jackson  2022-02-27    2021-02-12  38.520377
9996  6694        Susan Sanchez  2022-03-18    2020-08-20  45.626456
9997  1791           Beth Cohen  2022-02-04    2020-04-08  13.520932
9998  5653      Robert Gonzales  2022-03-12    2020-05-13  58.930644
9999  2874         Amanda Brown  2022-02-20    2021-02-02  62.816813

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.5192 minutes
ter 05 abr 2022 21:00:44 -03
All Done. :)
[3]    21760 done       python generator_data.py 10000 $JobNumber
        id        client_name        date date_register      value
0     8222      Nicole Turner  2022-03-17    2021-09-06  80.578954
1     3604     Leslie Jenkins  2022-01-07    2019-10-10  25.427345
2     3417      Billy Beasley  2022-01-22    2021-11-27   2.040977
3     5383      Micheal Brock  2022-02-06    2020-10-19   2.621183
4     4094        Angel Young  2022-04-03    2021-02-13  50.564286
...    ...                ...         ...           ...        ...
9995  9612       Jamie Miller  2022-01-27    2019-05-11  33.719715
9996  2338         Troy Smith  2022-01-07    2021-01-03  53.624822
9997  7444   Heather Martinez  2022-01-06    2019-06-06  65.242565
9998  2216     Madeline Chang  2022-01-09    2020-09-04   5.868639
9999  3614  Michele Hernandez  2022-03-08    2020-09-13  11.780769

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.5272 minutes
ter 05 abr 2022 21:00:46 -03
All Done. :)
[4]    21775 done       python generator_data.py 10000 $JobNumber
Number of processes to keep alive: 4
[3] 21959
ter 05 abr 2022 21:00:47 -03
        id        client_name        date date_register      value
0     3192         Kelly Soto  2022-02-18    2020-11-08  78.294761
1     3740     Karl Gutierrez  2022-04-02    2021-07-08  95.123744
2     6486      Sherri Arnold  2022-02-14    2022-02-09  35.996846
3     6794     Jeremiah Walsh  2022-02-07    2021-02-20  21.642443
4     8075          Jose Long  2022-03-06    2022-03-24  10.484655
...    ...                ...         ...           ...        ...
9995  6509   William Martinez  2022-03-21    2021-07-07  38.392668
9996  3415    Kristine Parker  2022-02-05    2020-08-10  77.099982
9997  9622   Caitlin Martinez  2022-02-10    2022-01-01  26.984343
9998  4734          Ruth Rios  2022-02-28    2021-06-30  58.373985
9999  6602  Gabrielle Johnson  2022-03-04    2020-01-30  35.186649

[10000 rows x 5 columns]
Starting job number #4...
----------------------------- DATABASE ----------------------------
memory RAM released.
time of execution: 0.5374 minutes
ter 05 abr 2022 21:00:48 -03
All Done. :)
[5]    21796 done       python generator_data.py 10000 $JobNumber
Number of processes to keep alive: 4
[4] 21978
ter 05 abr 2022 21:00:48 -03
Starting job number #5...
----------------------------- DATABASE ----------------------------
Number of processes to keep alive: 4
[5] 22000
        id      client_name        date date_register      value
0     3375    Nicholas Tran  2022-03-16    2019-10-10  12.479781
1     9973        Anna Gray  2022-03-15    2021-10-10  14.371225
2     3547    David Richard  2022-03-21    2019-08-31  99.265942
3     4777     Terry Lester  2022-03-02    2021-07-18  23.766142
4     7230    David Vaughan  2022-03-17    2020-07-14  54.086386
...    ...              ...         ...           ...        ...
9995  8361    Daniel Bowers  2022-01-12    2021-09-27  16.103485
9996  4473  Danny Castaneda  2022-01-13    2021-12-13  11.973627
9997  9107  Jessica Johnson  2022-02-10    2021-08-04  13.725691
9998  2392   Barbara Miller  2022-02-28    2021-07-01  17.852389
9999  2938  Jessica Rollins  2022-03-04    2019-07-27  10.685387

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.5442 minutes
ter 05 abr 2022 21:00:49 -03
All Done. :)
[6]  - 21811 done       python generator_data.py 10000 $JobNumber
ter 05 abr 2022 21:00:49 -03
Starting job number #6...
----------------------------- DATABASE ----------------------------
Number of processes to keep alive: 4
[6] 22019
ter 05 abr 2022 21:00:51 -03
Starting job number #7...
----------------------------- DATABASE ----------------------------
        id        client_name        date date_register      value
0     6265   Alicia Davenport  2022-03-26    2019-12-05   14.18479
1     3293     Isaiah Jenkins  2022-02-05    2021-03-01  73.454561
2     7061      Jasmine Smith  2022-02-02    2021-06-26  80.883036
3     8635        Robert Ware  2022-01-07    2020-04-10  81.691932
4     4910    Levi Barnett MD  2022-01-20    2020-06-07  17.200236
...    ...                ...         ...           ...        ...
9995  1518  Christopher Hardy  2022-01-16    2019-06-25  31.117378
9996  3316          Sarah Lee  2022-01-12    2021-08-26   26.23733
9997  9782  Nicholas Mcdaniel  2022-01-22    2020-12-16  44.446551
9998  2373   Danielle Ballard  2022-01-21    2021-09-30  21.258418
9999  5308  Clayton Hicks DVM  2022-02-06    2021-12-26  80.654115

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.5201 minutes
ter 05 abr 2022 21:01:19 -03
All Done. :)
[3]    21959 done       python generator_data.py 10000 $JobNumber
        id         client_name        date date_register      value
0     9168        Jeffrey Wong  2022-03-12    2021-08-18  86.262011
1     9577  Brittany Patterson  2022-01-21    2022-03-03   8.669195
2     3265      Robert Johnson  2022-02-18    2021-01-12    79.3052
3     7514     Frank Robertson  2022-02-12    2019-06-13  13.457695
4     9545      Angela Wheeler  2022-02-23    2021-10-30   3.296825
...    ...                 ...         ...           ...        ...
9995  1806      Brian Anderson  2022-01-14    2019-12-05  18.625031
9996  6617        Nancy Rogers  2022-02-27    2019-11-09  95.656853
9997  9849       Theresa Perez  2022-03-14    2022-03-31  87.338459
9998  7276     Kelsey Robinson  2022-02-06    2021-09-01  22.368764
9999  7623        Sandra Moore  2022-03-24    2020-04-28  72.461119

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.5221 minutes
ter 05 abr 2022 21:01:20 -03
All Done. :)
[4]    21978 done       python generator_data.py 10000 $JobNumber
        id     client_name        date date_register      value
0     8016  Anthony Morris  2022-02-08    2020-10-19  66.938432
1     4757   Leslie Cooper  2022-01-10    2020-08-28  48.534041
2     7916    Erica Lawson  2022-01-22    2020-10-26  46.960768
3     7041   Cynthia Jones  2022-01-19    2019-09-01    5.09263
4     7190    Douglas Cook  2022-01-20    2019-05-05  40.372664
...    ...             ...         ...           ...        ...
9995  6777     Lisa Hughes  2022-01-22    2019-09-29   5.216448
9996  4789   Micheal Frost  2022-02-27    2021-11-27  68.650756
9997  2981     James Brown  2022-04-02    2021-04-23  77.790853
9998  2893      Anna Perez  2022-03-14    2022-03-31   83.25658
9999  8616      John Hardy  2022-02-23    2020-11-14  76.049026

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.515 minutes
ter 05 abr 2022 21:01:20 -03
All Done. :)
[5]  - 22000 done       python generator_data.py 10000 $JobNumber
Number of processes to keep alive: 4
[3] 22170
ter 05 abr 2022 21:01:22 -03
Starting job number #8...
----------------------------- DATABASE ----------------------------
Number of processes to keep alive: 4
[4] 22186
        id          client_name        date date_register      value
0     1455       Stacy Williams  2022-04-03    2019-05-25   90.92088
1     9831         John Schmidt  2022-04-03    2021-07-24  71.823283
2     4211       James Peterson  2022-01-09    2020-03-08   47.15568
3     4158       Louis Ewing II  2022-03-29    2020-04-09   54.78143
4     2664         Mark Sanchez  2022-01-23    2019-06-18  85.646491
...    ...                  ...         ...           ...        ...
9995  4877       Michelle Vance  2022-03-20    2020-07-13  74.600947
9996  6332  Christopher Gregory  2022-03-08    2022-04-01   4.730215
9997  9261     Franklin Sanders  2022-03-28    2020-01-07  81.344963
9998  6249            Neil Cole  2022-02-05    2020-10-14  79.744809
9999  2466         Philip Smith  2022-03-28    2020-05-04  73.509695

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.526 minutes
ter 05 abr 2022 21:01:22 -03
All Done. :)
[6]  - 22019 done       python generator_data.py 10000 $JobNumber
ter 05 abr 2022 21:01:23 -03
Starting job number #9...
----------------------------- DATABASE ----------------------------
Number of processes to keep alive: 4
[5] 22211
ter 05 abr 2022 21:01:24 -03
Starting job number #10...
----------------------------- DATABASE ----------------------------
waiting until the last process finished...
waiting until the last process finished...
        id       client_name        date date_register      value
0     4484      Curtis Walsh  2022-03-11    2019-06-29  69.487448
1     8207        Gary Braun  2022-01-16    2020-10-11  41.724758
2     3915  Barbara Franklin  2022-03-14    2019-12-17  37.481957
3     5783     Jason Krueger  2022-02-10    2020-12-17  15.026336
4     1894         Marc Clay  2022-01-06    2021-12-18   3.758856
...    ...               ...         ...           ...        ...
9995  2742   Kathryn Jackson  2022-02-15    2020-10-25  93.863406
9996  8748    Ashley Coleman  2022-03-11    2021-10-31  72.372238
9997  8243    Rachel Sanchez  2022-03-29    2021-06-21  92.298247
9998  6602     Kimberly Ward  2022-02-20    2019-07-31  43.032824
9999  5276    Vincent Wright  2022-03-24    2021-05-26   24.38684

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.456 minutes
ter 05 abr 2022 21:01:49 -03
All Done. :)
[3]    22170 done       python generator_data.py 10000 $JobNumber
        id       client_name        date date_register      value
0     2802      Joseph Allen  2022-01-20    2019-12-07   9.034519
1     9337    Barbara Jacobs  2022-03-28    2020-02-06  45.799438
2     8302  Anthony Lawrence  2022-01-14    2019-06-08  12.851088
3     8011        Randy Ruiz  2022-01-06    2020-06-10  11.884906
4     8982     Karen Cameron  2022-02-17    2021-12-19  23.794182
...    ...               ...         ...           ...        ...
9995  8481   Timothy Carlson  2022-02-09    2019-06-29  41.475157
9996  3748      Sara Osborne  2022-03-10    2020-11-24   5.557425
9997  8398       Howard Hill  2022-01-12    2020-09-27   8.201378
9998  5472        Kelly Dyer  2022-03-21    2022-02-18  69.393603
9999  9338   Shelby Robinson  2022-01-19    2020-01-23  54.182112

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.4564 minutes
ter 05 abr 2022 21:01:50 -03
All Done. :)
[4]  - 22186 done       python generator_data.py 10000 $JobNumber
        id       client_name        date date_register      value
0     5532      Amanda Evans  2022-03-22    2019-08-02  30.353866
1     6084     Samuel Rivera  2022-01-18    2021-10-30   88.61284
2     8339    Johnathan Bush  2022-02-15    2022-02-23  22.130152
3     8662     William David  2022-03-12    2022-03-23  80.169212
4     8739  Stephanie Cooper  2022-02-06    2020-08-10  93.302379
...    ...               ...         ...           ...        ...
9995  5190        Sandy King  2022-01-29    2021-11-27  28.400841
9996  2517        David Hall  2022-04-01    2019-07-10  69.592634
9997  5300     Shelly Rivera  2022-03-02    2021-10-08  34.643616
9998  4197        Don Parker  2022-02-11    2022-01-16  95.053137
9999  4859     Maria Esparza  2022-03-22    2021-02-28  12.725396

[10000 rows x 5 columns]
memory RAM released.
time of execution: 0.4643 minutes
ter 05 abr 2022 21:01:51 -03
All Done. :)
[5]  + 22211 done       python generator_data.py 10000 $JobNumber
waiting until the last process finished...
merging files...
saving the file format feather...
files merged successfully.
1 minutes and 42 seconds elapsed for Script Execution.
All Done!
(base) 
```

## Resources

- [Faker’s documentation](https://faker.readthedocs.io/en/master/index.html)
- [Faker - Github](https://github.com/joke2k/faker)
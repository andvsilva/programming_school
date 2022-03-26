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


## Resources

- [Faker’s documentation](https://faker.readthedocs.io/en/master/index.html)
- [Faker - Github](https://github.com/joke2k/faker)
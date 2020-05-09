## Phyton-SS
Demo code of external sorting and searching using Python

### Code Requirements
The code is in Python 3.4

### Description
Here, there are three cases that we want to solve:

1. Sorting a million of data 
2. Sorting bigger data (~7 billion data)
3. Searching in a million of data


#### Case 1
A textfile that contains the age (integer) of each people in a city, 
assuming there are 10 million people in that city.
The format of the file is simple, each row represents age of a person.
This is the contents of **age.txt**:

```Text
23
51
35
...
```

We want to sort this data into the same textfile format (output file **age_sorted.txt**) that takes the file **age.txt** as input. 
Here, we only use Python built-in library to sort and create the output file.

#### Case 2
Case 2 is pretty similar to Case 1, but there are some differences. 
The textfile data is now bigger. **age.txt** now contains the age of the whole world (~7 billion people).
Also we only have "*shitty*" computer on hand with 1 GB of RAM.

From calculation, the textfile of ~7 billion integer data will take ~28 GB of memory space
(assuming it's 32 bit integer, 4 byte each integer, so it is 7 billion x 4 byte). 
The problem arises when we only have 1 GB of RAM, our RAM can not hold the data to sort it since it's 28 GB.

The Python code here demonstrates how to sort the big data even with low RAM size. 
We use classic devide and conquer method.
What we do here is store/split the big data into some chunk files, 
the size of each chunk file is lower than our RAM size of course, name it `chunk_memory`, 
each chunk file also contains sorted data. 
When we finish splitting the data, we merge it into one file (doing comparation in RAM), 
the buffer memory size also doesn't exceed the `chunk_memory`, 
so if we want the total buffer memory remains the same as `chunk_memory`, 
the buffer memory size must be `chunk_memory` devided by total of created chunks.

The name of script file to sort the data is **`SortingBigFile.py`**.
The main function to do sort in the file is **`sort_as_chunk()`**, it takes four arguments,
the input filename (which is **age.txt**), memory of chunk, flag to clean up the chunk files, and format of splited chunk files.
The script also provides random generator **age.txt** data to demonstrate it.
This script can handle Case 1 and Case 2 as well.
The file **`SortingBigFile.py`** depends on two files, **`memory_chunk_module.py`** and **`generator_random_data.py`**,
both of the files use Python build-in library.

The method above has a price, when we use chunk data stored in hard-disk memory (which is slower than RAM), 
the sorting process will take some time. It will be slower when the chunk memory is low (many chunk files). But there are some methods to optimize it, 
we can use multithreaded process for each chunk file and/or use GPU to make the process of sorting faster.

#### Case 3
In Case 3, we have list of a million blacklisted name and phone number in a textfile, each line is one word (name), followed by space,
then the phone number. The example of **blacklist.txt**:

```Text
Andi 1341441
Melisa 8565467
Aslam 2908345
...
```

Assuming we want to create API for this case.
We have to write two functions, **`initalize(blacklist)`** it takes string input which is the blacklist we have, called when the API is starting, 
and **`check_blacklist(name, phone_number)`**, this function takes two arguments and return Boolean value whether the name with the phone number is in blacklist or not. 

The name of script file to solve Case 3 is **`BlackListAPI.py`**.
When the script starts, it will call `initialize()` function, and then do check the name and phone number.
We do it using sorted chunk files as we do it for Case 1 and Case 2 to reduce RAM usage (in function `initialize()`), but instead of merging it into single sorted file, 
we do binary search for each chunk file for the name and phone number (in function `check_blacklist()`).
Because binary search's time complexity is O(lg *n*) even in worst case scenario, it will reduce the latency for the API call. 


### Script To Execute
Script to execute for each Case:

* **`SortingBigFile.py`** for Case 1 and Case 2.
* **`BlackListAPI.py`** for Case 3.


import random

# Generate random data into a txt file, the file contains integer data (assuming 32 bit, each 4 byte)
# so total size of file is : SIZE = total_random_data * 4 byte 
def create_file(filename, total_random_data, limit_bottom, limit_upper):
    random_file = open(filename, "w")

    for i in range(total_random_data):
        line = str(random.randint(limit_bottom, limit_upper)) + "\n"
        random_file.write(line)
    random_file.close()

    print("generating data: success")
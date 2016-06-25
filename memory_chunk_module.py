import math
import os

def get_parsed_memory(memory):
    # kilobyte
    if memory[-1].upper() == 'K':       
        return int(memory[:-1]) * 1024
    # megabyte
    elif memory[-1].upper() == 'M':     
        return int(memory[:-1]) * 1024 * 1024
    # gigabyte
    elif memory[-1].upper() == 'G':     
        return int(memory[:-1]) * 1024 * 1024 * 1024
    # byte
    else: 
        return int(memory)


def get_total_chunk(filename, chunk_memory):
    return int(math.ceil((os.path.getsize(filename) / chunk_memory)))


def cleanup_chunk_file(chunk_filenames):
    for file in chunk_filenames:
        os.remove(file)

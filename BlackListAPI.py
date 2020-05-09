import bisect
import memory_chunk_module as mcm


def initialize(filename):
    file_content = open(filename, "r")

    for i in range(total_chunk):
        lines = file_content.readlines(chunk_memory)
        lines.sort()
        file = open(blacklist_temp_format.format(i), "w")
        file.write(''.join(lines))
        chunk_filenames.append(blacklist_temp_format.format(i))
        file.close()
        

def check_blacklist(name, phone_number):
    is_blacklisted = False
    check_data = [name, phone_number]

    for i in range(total_chunk):
        file = open(blacklist_temp_format.format(i), "r")
        lines = [line.split() for line in file.readlines()]
        item_point = bisect.bisect(lines, check_data) # binary search for each chunk file
        if check_data in lines[item_point-1 : item_point]:
            is_blacklisted = True
            file.close()
            break

    return is_blacklisted


# Global variables
chunk_memory = mcm.get_parsed_memory("1k")
chunk_filenames = []
blacklist = "blacklist.txt"
blacklist_temp_format = 'blacklist_{0}.txt'
total_chunk = mcm.get_total_chunk(blacklist, chunk_memory)


if __name__ == "__main__":
    initialize(blacklist)

    # Demo
    print(check_blacklist("Siska", "712454"))
    print(check_blacklist("Melisa", "8565467"))  
    print(check_blacklist("Jokho", "081235"))

    print()
    mcm.cleanup_chunk_file(chunk_filenames)

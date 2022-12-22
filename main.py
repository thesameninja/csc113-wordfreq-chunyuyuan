import string
import multiprocessing
import time

filepath = "./book.txt" 
out_filepath = "./output.txt"
#removes the punctuations in the text using built in python string class
def remove_punctuations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line
#removes numbers from the text
def remove_numbers(line):
    line = ''.join((x for x in line if not x.isdigit()))
    return line

def ordered_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key],key))
        sorted_values = sorted(sorted_values)

    sorted_values = sorted_values[::-1]
    return sorted_values

def process_line(line, word_count, lock):
    line = remove_punctuations(line)
    line = remove_numbers(line)
    words = line.split()

    # Acquire the lock
    lock.acquire()
    try:
        for word in words:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
    finally:
        # Release the lock
        lock.release()

def measure_time(num_processes):
    # Create a manager to create a shared memory space
    manager = multiprocessing.Manager()

    # Create a shared dictionary using the manager
    word_count = manager.dict()

    # Create a lock to synchronize access to the shared dictionary
    lock = manager.Lock()

    # Record the start time
    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool(num_processes) as pool:
        # Open the input file in read mode
        with open(filepath, 'r') as fi:
            # Process the lines in the file in parallel using the worker processes
            pool.starmap(process_line, [(line, word_count, lock) for line in fi])

    # Record the end time
    end_time = time.time()

    # Sort the word count dictionary by frequency
    sorted_word_count = ordered_dict_by_freq(word_count)

    # Write the sorted word count dictionary to the output file
    with open(out_filepath, 'w') as fo:
        for item in sorted_word_count:
            fo.write("{:<30}{:>8}\n".format(item[1], item[0]))

    #Return the time taken to execute the script
    return end_time - start_time

if __name__ == '__main__':
    # Measure the time taken to execute the script using 1 process
    time_1_process = measure_time(1)
    print("Time taken with 1 processes: {:.2f} seconds".format(time_1_process))

    # Measure the time taken to execute the script using 2 processes
    time_2_processes = measure_time(2)
    print("Time taken with 2 processes: {:.2f} seconds".format(time_2_processes))

    # Measure the time taken to execute the script using 3 processes
    time_3_processes = measure_time(3)
    print("Time taken with 3 processes: {:.2f} seconds".format(time_3_processes))

    # Measure the time taken to execute the script using 4 processes
    time_4_processes = measure_time(4)
    print("Time taken with 4 processes: {:.2f} seconds".format(time_4_processes))

     # Measure the time taken to execute the script using 5 processes
    time_5_processes = measure_time(5)
    print("Time taken with 5 processes: {:.2f} seconds".format(time_5_processes))

     # Measure the time taken to execute the script using 5 processes
    time_6_processes = measure_time(6)
    print("Time taken with 6 processes: {:.2f} seconds".format(time_6_processes))

     # Measure the time taken to execute the script using 7 processes
    time_7_processes = measure_time(7)
    print("Time taken with 7 processes: {:.2f} seconds".format(time_7_processes))

    # Measure the time taken to execute the script using 8 processes
    time_8_processes = measure_time(8)
    print("Time taken with 8 processes: {:.2f} seconds".format(time_8_processes))

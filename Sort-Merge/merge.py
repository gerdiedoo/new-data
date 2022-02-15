import array, tempfile, heapq, random

"""
 Solution to sort large file containing many 32-bit integers
 See original Guido's solution based on Python3.0
 http://neopythonic.blogspot.com.au/2008/10/sorting-million-32-bit-integers-in-2mb.html

 The idea is to read part of the input file into memory, sort them and write sorted result to 
 a temporary file. Finally merge these temp files to one single output file.
 Use read in chunks and write in batch for time and memory efficiency
 Here only use a file with 1000 integers for demonstration
"""

def gen_file(num):
    """
    Generate a file for sort

    The content stored is some internal representation depending on the machine
    not readable text content in file. See official doc about array:
    https://docs.python.org/2/library/array.html

    @param num -- the number of integers in file
    """
    # Each item size is 4 bytes for typecode 'i'. Check it using ar.itemsize 
    ar = array.array('i')
    f = open('large_int_file', 'w')
    #batch_size = num / 10
    for i in xrange(num):
        ar.append(random.randint(1, num))
        if len(ar) >= 100: # batch write
            ar.tofile(f)
            del ar[:]
    f.close()

def read_in_chunks(f, size):
    """
    Create a generator for reading file data in chunks

    This is particularly memory efficient for large file reading
    since it doesn't pull the data into memory all at once.
    Also take care of when we finish consuming the file data,
    easy to use for other code by simply iterating on it. 
    See the use in 'tempfile_gen' and 'sort_large_int_file' functions

    @param f    -- file handler
    @param size -- int size for the number of bytes we read each time
    """
    while True:
        data = f.read(size)
        if not data:
            break
        yield data

def tempfile_gen(t):
    """
    Create a generator to be used in merge phase

    @param t -- temporary file handler
    """
    t.seek(0)
    ints = array.array('i')
    for data in read_in_chunks(t, 400):
        # fromstring accepts a series of bytes read from sorted temp file
        ints.fromstring(data)
    for each in ints:
        yield each

def merge_sortedfiles(iters):
    """
    Merge each sorted temp file to one output file

    @params iters -- a list of temp file generator
    """
    # Write text content to output file to be readable
    output = open('output.txt', 'w')
    ar = array.array('i')
    for x in heapq.merge(*iters):
        ar.append(x)
        if len(ar) >= 50: # write once when extracting 50 ints in order
            ws = ','.join(map(str, ar))
            #print '-' * 20
            output.write(ws)
            output.write('\n')

            del ar[:] # clear the array buffer for next series of integers
    if ar:
        ws = ','.join(map(str, ar))
        output.write(ws)

def sort_large_int_file():
    """
    Main logic to sort large file
    """
    f = open('large_int_file', 'r')
    ar = array.array('i')
    iters = []
    # Read 800 bytes each time, that is 200 integers
    # Each temp file has the size of 800 bytes
    for data in read_in_chunks(f, 800):
        # Also can use ar.fromfile(f, n) n is the number of ints we read
        # But fromfile will raise error if less than n integers available
        # fromstring (byte string) is flexible provided the chunk size is multiple of the item size

        ar.fromstring(data)
        t = tempfile.TemporaryFile()
        sorted_ar = array.array('i', sorted(ar))
        sorted_ar.tofile(t)

        iters.append( tempfile_gen(t) )
        del ar[:]  # clear the array buffer to read next chunk

    merge_sortedfiles(iters)
    f.close()

if __name__ == "__main__":
    #gen_file(1000)

    sort_large_int_file()

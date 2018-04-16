import multiprocessing as mp # processes
import random # pseudo random numbers
import string # collection of string constants

"""
Process, Queue
"""

random.seed(123)

output = mp.Queue()

# puts a random string into the queue
def rand_string(length, pos,  output):
    rand_str = "".join(random.choice(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.digits)
                  for i in range(length))
    output.put((pos, rand_str))

# create processes
processes = [mp.Process(target=rand_string, args=(5, x, output)) for x in range(4)]

# start
for p in processes:
    p.start()

# wait for process to end
for p in processes:
    p.join()

# sort results in reverse id order
results = [output.get() for p in processes]
results.sort(key=lambda x:x[0], reverse=True)
print(results)


"""
Pool - apply, map, apply_async, map_async
"""

def cube(x):
    return x**3

pool = mp.Pool(processes=4)

# synchronous - block until all workers finished
results = [pool.apply(cube, args=(x,)) for x in range(1, 7)]

# asynchronous - apply_async returns a list of futures
results = [pool.apply_async(cube, (x,)) for x in range(1, 7)]
output = [p.get() for p in results]

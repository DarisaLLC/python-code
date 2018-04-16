import random 

def get_data():
    return random.sample(range(10), 3)

# first send(None) initializes variables and enters while loop 
def consumer():
    rsum = 0.0 # use name "rsum" so we don't hide the sum() name
    items_seen = 0.0
    while True:
        l = yield # receive data and print updated running average, then return None to all send() calls
        items_seen += len(l)
        rsum += sum(l) 
        print("running average: {}".format(rsum/items_seen))

# does not accept data via send()
# simple use next() to print running average
# note that None is returned for each next() call
def producer(consumer):
    consumer.send(None)
    while True:
        l = get_data()
        print("produced: {}".format(l))
        consumer.send(l)
        # first next() call intializes consumer and yields first None (printing first average) 
        # subsequent next() calls continue returning None (printing averages)
        yield None 

print(__name__)

if __name__ == "__main__":
    c = consumer()
    p = producer(c)
    for i in range(10):
        p.__next__()

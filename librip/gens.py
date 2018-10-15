import random


def field(items, *args):
    for l in items:
        if len(args) > 1:
            for x in args:
                if x in l.keys:
                    if l[x] is not None:
                        yield l[x]
        elif len(args) == 1:
            for x in args:
                if x in l.keys():
                    if l[x] is not None:
                        yield l[x]
                        
                        
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield (random.randrange(begin, end + 1))

query_string = "?name=Bob&age=99&day=Wed"

def make_list(query):
    pairs = query_string[1:].split('&') # first step
    print(pairs)
    for i in range(len(pairs)):
        pairs[i] = tuple(pairs[i].split('=')) # second step, remove = and convert to tuple
    return pairs


print(make_list(query_string))


#    s[s.find(' ') + 1:]     start +1 after space.


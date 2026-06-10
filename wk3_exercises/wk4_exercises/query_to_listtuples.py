query_string = "?name=Bob&age=99&day=Wed"

def make_list(string):
    pairs = string[1:].split('&') # first step
    print(pairs)
    pairs = [pair.split('=') for pair in pairs]
    print(pairs)
        #pairs[i] = tuple(pairs[i].split('='))
    return pairs


print(make_list(query_string))


#    s[s.find(' ') + 1:]     start +1 after space.


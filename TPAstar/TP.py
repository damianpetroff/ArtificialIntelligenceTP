

'''0'''
def h0(n):
    return 0

'''la distance entre n et B sur l'axe x'''
def h1(n):
    return 0

'''la distance entre n et B sur l'axe y'''
def h2(n):
    return 0

'''la distance à vold d'oiseau entre n et B'''
def h3(n):
    return 0

'''la distance de Manhattan entre n et B'''
def h4(n):
    return 0

def solve(v1, v2, h):
    return 0

d_positions = {}
d_connections = {}


# DEBUG
def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print(k)
                dumpclean(v)
            else:
                print('%s : %s' % (k, v))
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print(v)
    else:
        print(obj)

# END DEBUG

if __name__ == "__main__":
    import re
    with open("data/positions.txt", "r") as file:
        for position in file.readlines():
            p = re.sub('\n', '', position).split(' ')
            d_positions[p[0]]=(p[1],p[2])
    dumpclean(d_positions)

    with open("data/connections.txt", "r") as file:
        for connection in file.readlines():
            c = re.sub('\n', '', connection).split(' ')
            d_connections[(c[0],c[1])]=c[2]
    dumpclean(d_connections)

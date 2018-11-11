
cities = []

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = {}
        self.parent = None
        self.fn = 0
        self.gn = 0
        self.hn = None

    def __str__(self):
        return f"{self.name} ({self.x},{self.y}), {len(self.neighbors)} neighbors"

    def addNeighbor(self, city, weight):
        self.neighbors[city] = weight

    def dumpNeighbors(self):
        for k,v in self.neighbors.items():
            print(f"neighbor:{k}, weight:{v}")

def readFiles():
    import re
    #Read positions file
    with open("data/positions.txt", "r") as file:
        for position in file.readlines():
            p = re.sub('\n', '', position).split(' ')
            cities.append(City(p[0], int(p[1]), int(p[2])))

    #Read connections file
    with open("data/connections.txt", "r") as file:
        for connection in file.readlines():
            c = re.sub('\n', '', connection).split(' ')
            getCityFromName(c[0]).addNeighbor(getCityFromName(c[1]), int(c[2]))
            getCityFromName(c[1]).addNeighbor(getCityFromName(c[0]), int(c[2]))

def getCityFromName(name):
    for city in cities:
        if city.name == name:
            return city
    return 0

def getCityFromInput(s):
    city = None
    st = "\nEnter "+s+" city : "
    while(city not in cities):
        cityName = input(st).capitalize()
        city = getCityFromName(cityName)
    return city

def AStar(initialCity, destinationCity, h):
    history = []
    currentCity = None
    frontiere = [initialCity]
    initialCity.gn = 0

    while len(frontiere) > 0 :
        frontiere = sorted(frontiere, key=lambda city: city.fn)
        currentCity = frontiere.pop(0)

        if currentCity == destinationCity:
            return (getPath(currentCity), len(history), currentCity.gn)

        history.append(currentCity)

        for city, weigth in currentCity.neighbors.items():
            if city not in history:
                gn = weigth + currentCity.gn
                hn = h(city, destinationCity)
                fn = gn + hn
                if city.hn is None:
                    city.hn = hn

                if city not in frontiere:
                    frontiere.append(city)
                elif gn >= city.gn:
                    continue

                city.parent = currentCity
                city.gn = gn
                city.fn = fn
    return (None, len(history), 0)

def getPath(city):
    path = [city]
    currentCity = city.parent
    while currentCity is not None:
        path.append(currentCity)
        currentCity = currentCity.parent
    path.reverse()
    return path

def pathToString(path):
    stringPath = path[0].name
    for city in path[1::]:
        stringPath += " -> " + city.name
    return stringPath

# Heuristiques
def h0(n, B):
    '''0'''
    return 0
def h1(n, B):
    '''la distance entre n et B sur l'axe x'''
    return abs(n.x - B.x)
def h2(n, B):
    '''la distance entre n et B sur l'axe y'''
    return abs(n.y - B.y)
def h3(n, B):
    '''la distance à vol d'oiseau entre n et B'''
    return (pow(h1(n,B), 2) + pow(h2(n,B), 2)) ** 0.5
def h4(n, B):
    '''la distance de Manhattan entre n et B'''
    return h1(n, B)+h2(n, B)

if __name__ == "__main__":
    import sys
    heuristiques = [h0, h1, h2, h3, h4]
    readFiles()

    #Initial City
    if len(sys.argv) > 1:
        initialCityName = sys.argv[1].capitalize()
        initialCity = getCityFromName(initialCityName)
    else:
        initialCity = getCityFromInput("initial")
    print(f"Initial city city set to {initialCity.name} ({initialCity.x},{initialCity.y})")

    #Destination City
    if len(sys.argv) > 2:
        destinationCityName = sys.argv[2].capitalize()
        destinationCity = getCityFromName(destinationCityName)
    else:
        destinationCity = getCityFromInput("destination")
    print(f"Destination city set to {destinationCity.name} ({destinationCity.x},{destinationCity.y})")

    #A
    i=0
    for hi in heuristiques:
        print("\nHeuristic : ", i)
        path = AStar(initialCity, destinationCity, hi)
        print("Path :", pathToString(path[0]))
        print("Number of visited cities :", path[1])
        print("Path weight :", path[2])
        i+=1

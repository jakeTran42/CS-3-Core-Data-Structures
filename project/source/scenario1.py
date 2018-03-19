import strings

def read_routes(path):
    routeDict = {}
    for line in open(path, 'r'):
        line = line.split(',')
        line[1] = line[1].strip()
        routeDict[line[0]] = line[1]
    return routeDict

def find_cost(allRoutesCost, phoneNumber):
    # print('\n',allRoutesCost)
    bestPrice = 0
    for k, v in allRoutesCost.items():
        v = float(v)
        if strings.contains(phoneNumber, k):
            if bestPrice == 0:
                bestPrice = v
            elif v < bestPrice:
                bestPrice = v
    return str(bestPrice)

def write_cost(phoneNumber, price):
    with open('route-price-1.txt', 'w') as file:
        file.write(phoneNumber + ' --- ' + price)

if __name__ == '__main__':
    allRoutes = read_routes('../data/route-costs-4.txt')
    phoneNumbers = '+15124156620'
    best_price = find_cost(allRoutes, phoneNumbers)
    write_cost(phoneNumbers, best_price)

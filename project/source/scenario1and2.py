import strings
import time

def read_routes(routePath):
    routeDict = {}
    for line in open(routePath, 'r'):
        line = line.split(',')
        line[1] = line[1].strip()
        routeDict[line[0]] = line[1]
    return routeDict

def read_numbers(numberPath):
    openNumList = open(numberPath, 'r')
    numList = openNumList.read().splitlines()
    return numList



def find_cost(allRoutesCost, phoneNumber):
    # print('\n',allRoutesCost)
    bestPrice = '0'
    currentKeyLen = 0
    for k, v in allRoutesCost.items():
        # v = float(v)
        if phoneNumber.startswith(k):
        # if k in phoneNumber:
            # if bestPrice == 0:
            #     bestPrice = v
            if len(k) > currentKeyLen:
                currentKeyLen = len(k)
                bestPrice = v
    return bestPrice

def write_cost(phoneNumber, price, N, write):
    with open('route-price-{}.txt'.format(N), '{}'.format(write)) as file:
        file.write(phoneNumber + ' --- $' + price + '\n')

def singleNumber(routes, phoneNumber):
    start_time = time.time()
    allRoutes = read_routes(routes)
    best_price = find_cost(allRoutes, phoneNumber)
    write_cost(phoneNumber, best_price, 1, 'w')
    end_time = time.time()
    print("Running time:", end_time - start_time)

def multipleNums(routes, numPath):
    start_time = time.time()
    allRoutes = read_routes(routes)
    all_nums = read_numbers(numPath)
    for num in all_nums:
        best_price = find_cost(allRoutes, num)
        write_cost(num, best_price, 2, 'a')
    end_time = time.time()
    print("Running time:", end_time - start_time)


if __name__ == '__main__':
    singleNumber('../data/route-costs-10000000.txt', '+14152345678')
    # multipleNums('../data/route-costs-106000.txt', '../data/phone-numbers-1000.txt')

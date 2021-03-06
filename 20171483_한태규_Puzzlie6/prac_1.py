#Programming for the Puzzled -- Srini Devadas
#Find the Fake
#Given a collection of coins, one of which is fake and is slightly heavier
#find the counterfeit using a minimum number of weighings.

#The procedure splits coin pile into 3 groups
def splitCoins(coinsList):
    length = len(coinsList)
    print(length)
    group1 = coinsList[0:length//3]
    group2 = coinsList[length//3:length//3*2]
    group3 = coinsList[length//3*2:length]
    return group1, group2, group3
    
#This procedure compares the weight of 2 groups like a balance
def compare(groupA, groupB):
    if sum(groupA) > sum(groupB):
        result = 'left'
    elif sum(groupB) > sum(groupA):
        result = 'right'
    elif sum(groupB) == sum(groupA): #Could just be an else
        result = 'equal'
    return result

#This procedure finds the fake coin group, knowing that the
#fake coin is heavier
def findFakeGroup(group1, group2, group3):
    result1and2 = compare(group1, group2)
    
    if result1and2 == 'left':
        fakeGroup = group1
        status = 'left' # prac_1 추가
    elif result1and2 == 'right':
        fakeGroup = group2
        status = 'right' # prac_1 추가
    elif result1and2 == 'equal': #Could just be an else
        fakeGroup = group3
        status = 'equal' # prac_1 추가

        
    return fakeGroup, status
    

#This procedure iteratively keeps dividing the pile into 3 smaller piles and
#using the balance to choose one of the smaller piles until the fake coin is found
def CoinComparison(coinsList):
    counter = 0
    #Make a copy of coinsList
    currList = coinsList[:]
    while len(currList) > 1:
        group1, group2, group3 = splitCoins(currList)
        currList, status = findFakeGroup(group1, group2, group3)
        counter += 1

        # prac_1 추가
        if len(currList) == 1 and status == "equal":
            print("코인의 무게가 전부 동일합니다.")
            print("가짜 코인이 없습니다.")

    #We are down to one coin in the pile so we found the fake
    fake = currList[0]

        
    print ('The fake coin is coin', coinsList.index(fake) + 1, 'in the original list')
    print ('Number of weighings:', counter)

    
#Pretend that you actually can't see the values in coinsList!
coinsList2 = [10, 10, 10, 10, 10, 10, 11, 10, 10]

coinsList = [10, 10, 10, 10, 10, 10, 11, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10]

noFakeList = [10, 10, 10,    10, 10, 10,     10, 10, 10,


             10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10]

##coinComparison(coinsList2)
CoinComparison(noFakeList)


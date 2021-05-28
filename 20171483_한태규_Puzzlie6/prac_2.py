#Programming for the Puzzled -- Srini Devadas
#Find the Fake
#Given a collection of coins, one of which is fake and is slightly heavier
#find the counterfeit using a minimum number of weighings.

#The procedure splits coin pile into 3 groups
def splitCoins(coinsList):
    length = len(coinsList)
    group1 = coinsList[0:length//3]
    group2 = coinsList[length//3:length//3*2]
    group3 = coinsList[length//3*2:length]
    return group1, group2, group3

## prac_2 추가
def findFakeGroupAndType(group1, group2, group3):

    group1_sum = sum(group1)
    group2_sum = sum(group2)
    group3_sum = sum(group3)

    if group1_sum == group2_sum:
        another_number = group3_sum - group1_sum
    elif group1_sum == group3_sum:
        another_number = group2_sum - group1_sum
    elif group2_sum == group3_sum: #Could just be an else
        another_number = group1_sum - group2_sum
    return another_number

## prac_2 추가
def findFakeGroupLighter(group1, group2, group3):

    if sum(group1) < sum(group2):
        fakeGroup = group1
    elif sum(group2) < sum(group1):
        fakeGroup = group2
    elif sum(group2) == sum(group1): #Could just be an else
        fakeGroup = group3
        
    return fakeGroup

## prac_2 추가
def findFakeGroupHeavier(group1, group2, group3):

    if sum(group1) > sum(group2):
        fakeGroup = group1
    elif sum(group2) > sum(group1):
        fakeGroup = group2
    elif sum(group2) == sum(group1): #Could just be an else
        fakeGroup = group3

    return fakeGroup

#This procedure iteratively keeps dividing the pile into 3 smaller piles and
#using the balance to choose one of the smaller piles until the fake coin is found
def CoinComparisonGeneral(coinsList):
    counter = 0
    #Make a copy of coinsList
    currList = coinsList[:]
    find_type = None ## prac_2 추가
    while len(currList) > 1:
        group1, group2, group3 = splitCoins(currList)

        ## prac_2 추가
        if not find_type :
            find_type = findFakeGroupAndType(group1, group2, group3)
            print(find_type)
            counter += 2

        ## prac_2 추가
        if find_type > 0:
            fake_coin_status = "무거운"
            currList = findFakeGroupHeavier(group1, group2, group3)

        ## prac_2 추가
        if find_type < 0:
            fake_coin_status = "가벼운"
            currList = findFakeGroupLighter(group1, group2, group3)

        counter += 1

        # prac_1 추가
        if find_type == 0:
            print("코인의 무게가 전부 동일합니다.")
            print("가짜 코인이 없습니다.")
            print('Number of weighings:', counter)
            return

    #We are down to one coin in the pile so we found the fake
    fake = currList[0]

    print('가짜 동전의 상태 > {}'.format(fake_coin_status))
    print('Number of weighings:', counter)
    print('The fake coin is coin', coinsList.index(fake) + 1, 'in the original list')

    
#Pretend that you actually can't see the values in coinsList!
coinsList = [10, 10, 10,     10, 10, 10,       10, 10, 10,

             10, 10, 10, 10, 10, 10, 10, 10, 10,

             10, 10, 10, 10, 10, 10, 9, 10, 10]

##coinComparison(coinsList2)
CoinComparisonGeneral(coinsList)


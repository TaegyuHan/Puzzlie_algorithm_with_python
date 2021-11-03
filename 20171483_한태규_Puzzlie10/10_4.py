
def dinnerCheck(invited, dislikePairs):
    good = True
    for j in dislikePairs:
        if j[0] in invited and j[1] in invited:
            good = False
    return good

def largestSol(chosen, elts, dPairs, Sol):
    if len(elts) == 0:
        if Sol == [] or len(chosen) > len(Sol):
            Sol = chosen
        return Sol

    if dinnerCheck(chosen + [elts[0]], dPairs):
        Sol = largestSol(chosen + [elts[0]], elts[1:], dPairs, Sol)

    return largestSol(chosen, elts[1:], dPairs, Sol)

def InviteDinner(guestList, dislikePairs):
    Sol = largestSol([], guestList, dislikePairs, [])
    print(f"Optimum solution: {Sol}")

if __name__ == '__main__':
    dislikePairs = [['Alice', 'Bob'], ['Bob', 'Eve']]
    guestList = ["Alice", "Bob", "Cleo", "Don", "Eve"]
    InviteDinner(guestList, dislikePairs)
# this is a function straight from the textbook. I am copying this code to try to memorize and look back on when necessary

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

# Secret Santa Picker
import random
import pandas as pd

nameDictionary = {}
i = 0

while(input != "End"):
    santa = input('Enter name of Participant: (enter "End" to exit to results)\n')
    if santa == "End":
        break
    pgiftee = input('If known, which Participant did this Santa buy for last year?\n')
    partner = input('Enter the name of Participant this Particiant should not get as their Giftee.\n')
    giftee = ""
    nameDictionary[i] = santa, pgiftee, partner, giftee
    i += 1

df = pd.DataFrame(nameDictionary)
df.index['Santa', 'Previous Giftee', 'Partner/Limit', 'Giftee']
df1 = pd.DataFrame.transpose(df)
options = df1['Santa'].tolist()
j = 0

for ind in range(0, len(df1.index)):
    giftee = df1['Santa'].sample(1, replace = False, ignore_index = True).values[0]
    gifteeConditions, conditionsInd = conditionCheck(df1, giftee, options, j)
    gifteeUnique, uniqueInd = uniqueCheck(df1, gifteeConditions, options, j)
    if gifteeConditions == gifteeUnique:
        giftee = gifteeUnique
    else:
    
    df1['Giftee'][ind] = giftee
    options.remove(giftee)
    j += 1

print(df1)

def conditionCheck(nameDataFrame, tempGiftee, options, ind):
    conditionsIndicator = False
    while conditionsIndicator == False:
        if (tempGiftee == nameDataFrame['Santa'][ind]) | (tempGiftee == nameDataFrame['Previous Giftee']) | (tempGiftee == nameDataFrame['Partner/Limit'][ind]):
            tempGiftee = nameDataFrame['Santa'].sample(1, replace = False, ignore_index = True).values[0]
            print("Condition Check Fail: " + tempGiftee)
            continue
        else:
            conditionsIndicator = True
            giftee = tempGiftee
            print("Condition Check Success: " + giftee)
            break
    return [giftee, conditionsIndicator]

def uniqueCheck(nameDataFrame, tempGiftee, options, ind):
    uniqueIndicator = False
    while uniqueIndicator == False:
        if tempGiftee not in options:
            tempGiftee = df1['Santa'].sample(1, replace = False, ignore_index = True).values[0]
            print("Unique Check Fail: " + tempGiftee)
            continue
        else:
            uniqueIndicator = True
            giftee = tempGiftee
            print("Unique Check Success: " + giftee)
            continue
    return [giftee, uniqueIndicator]


#drink hashmap with key being drink name and tuple as list
drinkPrices = {"cappuccino": [5.50, 0], "plain": [4.00, 0], "frappe": [10.00, 0], "milkshake": [8.00, 0], "latte": [5.00, 0] }


#hashmap that has the name of the person as key and a list as value
#list contains the drink name they drink and the total amount they have paid
pairs = {"Bob": ["cappuccino", 0], "Jeremy": ["plain", 0], "Linda": ["frappe", 0], "Bella": ["milkshake", 0], "Carol": ["latte", 0]}


#running total of how much has been paid in all time. start at 100 just for example
totalSum = 100


#total for how much was paid on this current trip
currentSum = 0


#calculate what % this drink was of the current sum and update it in the dictionary
def drinkPercentage(drinkPrices, currentSum):
    for drink in drinkPrices.items():
        percentage = drink[1][0] / currentSum
        drink[1][1] = percentage


#function to calculate who buys this time        
def whoPays(drinkPrices, pairs, currentSum):
    #loop to get total sum of this coffee run
    for person in pairs:        
        #add the drink price to the sum
        currentSum += drinkPrices.get(pairs.get(person)[0])[0] 
    
    global totalSum 
    totalSum += currentSum

    #call drinkPercentage fn to calculate %s
    drinkPercentage(drinkPrices, currentSum) 
    
    #variable to track who has the biggest difference in percentage paid vs percentage their coffee takes up of sum
    biggestDifferenceKey = None 
    #variable to keep track of the biggest percentage numerically
    biggestDifference = float('-inf')
    
    #now loop through each person 
    for person in pairs.items(): 
        #calculate what % has each person paid of the total amount so far
        percentagePaid = person[1][1] / totalSum 
        differenceInPercentages = drinkPrices.get(person[1][0])[1] - percentagePaid
        #calculate the diff between the person's percentage and the coffee's percentage and
        #compare it to the max difference
        #update if the difference is the biggest so far
        if (differenceInPercentages) > biggestDifference: 
            biggestDifference = differenceInPercentages
            biggestDifferenceKey = person 
    
    #make sure to update the person who is paying's percentage paid
    pairs[biggestDifferenceKey[0]][1] += currentSum
    
    #return person
    return biggestDifferenceKey[0] 

print("The person who pays this time is " + whoPays(drinkPrices, pairs, currentSum))
    
        
        

# Submission For Bertram Capital: Who Buys Coffee

## How To Run Code
There are 2 data structures and 1 global variable that can be updated and tested. Those are the **drinkPrices** dictionary, the **pairs** dictionary, and the **totalSum** variable. You can update the prices of the drinks, the amount a person has previously paid, what drink they buy, how many people, etc.. You can also update how much has already been spent. 

Then all you need to do is run the code in the terminal. You can use a for loop to see how the person who is paying changes as the total sum/the amount they have paid has changed. I have included a commented out for loop at the bottom for convenience. I have also included a print function so you can see how much each person has paid after the loop ends.

I have also included comments for nearly every line of code to help explain their purpose/rational

## Pre-entered Data
I have pre-entered data to demonstrate the layout of my data structures and to make it easier to run the code. Please feel free to follow that format for either dictionary

## My thought process
Since each drink is a different price, it wouldn't be fair to make every person take turns paying. Therefore, I decided to make the payment choice based off percentages. First, I calculated the percentage each individual drink was over the cost of all the drinks. (So a $4 drink is 25% if all the drinks together cost $20). Then I calculated how much each person has paid % wise of the total amount (if someone only spent $40 out of $320 then they only spent 1/8 of the total cost). The difference between those the % a person has actually paid vs what they should have paid according to their drink is then calculated. Whomever has the highest difference has to pay. For instance, if Joe has only paid 30% of the total cost but his drink is 50% of all the drink costs, then he is likely going to pay next. 

## Thoughts on how to extend this code & assumptions
Using a backend server and database would be an extension to this code as it would enable the variables to have their changes stored. Right now the dictionary always returns to the written in numbers, but a database would be able to store changes to those values and a server could return them long term. 

In addition, this code assumes people order the same thing every single time and that drink prices are static. If people change their orders or drink prices fluctuate, that would require additional variables/data structures and functions to keep track of what they ordered last. That is why I would recommend a backend server/database so you can update those drink prices/people's orders. 

In the case where two people have tied for having the biggest difference, by my code (as I set > rather than >= biggestDifference), the first person in the dictionary will be the one to pay.
# python program to print even words 
string = "we are all violent men " # In this example 'we' word has 2 letters and 
                              # ramain words are have odd no. of letters 



count = string.split(' ')

for i in count:
    if len(i)%2==0:
        print(i, end="")
# to print words greater than k

k = 3
for i in count:
    if len(i)>k:
        print("\n", i)


# python program to print even words 
string = "we are violent men" # In this example 'we' word has 2 letters and 
                              # ramain words are have odd no. of letters 

k = 3

count = string.split(' ')

for i in count:
    if len(i)%2==0:
        print(i, end=" ")

for i in count:
    if len(i)>k:
        print("\n",i, end=' ' )


        
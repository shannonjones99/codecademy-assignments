import numpy as np

## Question 1
# answer b.	(6,4)

## Question 2

a = np.array([
    [12, 7, 19, 3],
    [5, 14, 8, 22],
    [9, 1, 16, 11],
    [10, 11, 2, 0]
])

print(a[ :4, -2: ])
# answer d.	a[ :4 , -2: ]

## Question 3
print(np.arange(1,15,3).reshape(1, 5) )
# answer a.	[[ 1, 4, 7, 10, 13]]

## Question 4
def plus(n):
    if type(n)!= int and n <= 2:
        return "n is not a integer greater than 2"
    
    zeros = np.zeros((n, n))
    zeros[:, n//2] = 1 # column ones
    zeros[n//2, :] = 1 # rows ones
    return zeros

print(plus(9))

## Question 5
weights = 175 - np.arange(5*7)/5
weekly_weights = weights.reshape(5,7)
weekend_weights = weekly_weights[:5,-2:]
average_weekend_weights = weekend_weights.mean(axis=1)
print(weekend_weights,average_weekend_weights )

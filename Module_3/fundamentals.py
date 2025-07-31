dates = [1982,1980,1973]
N = len(dates)
print(N)

for i in range(N):
    print(dates[i]) 

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

for i in range(-5,6):
    print(i)    

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for gender in Genres:
    print (gender)    


PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
Ratings = PlayListRatings[i]
while i < len(PlayListRatings) and Ratings >= 6:
    print(Ratings)
    i = i + 1
    Ratings = PlayListRatings[i]
    # i+=1

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while i < len(squares) and squares[i] == 'orange':
    print(squares[i]) 
    new_squares.append(squares[i])
    i+=1
    print(new_squares)
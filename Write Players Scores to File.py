# Write Players Scores to File
'''
The Springfork Amateur Golf Club has a tournament every weekend. The club
president has asked you to write a program that will read each player's name
and score as keyboard input, and then save these as records in a file named
golf.txt.
First, the program should ask the user for the number of players. Then, it
should ask the user for each name and score individually.
The file golf.txt should be structured so that there is a line with the player's
name, followed by their score on the next line.
Here is an example:
Emily
30
Mike
20
Jonathan
23
'''

file = open('golf.txt', 'w')
players = int(input("Enter number of players:"))

for i in range (players):
    player = input("Enter name of player number " + str(i+1) + ":")
    file.write(player + "\n")
    score = input("Enter score of player number " + str(i+1) + ":")
    file.write(score + "\n")
file.close()




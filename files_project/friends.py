#ask the user for a list of three friends 
#for each friend, we'll tell the user whether they are nearby
#for each nearby firend, we'll save their name to 'nearby_friends.txt'

#hint readline()

friends = input('Enter three friends names, separeted by commas (no spaces, please):').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()] #check if the name were in the file

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
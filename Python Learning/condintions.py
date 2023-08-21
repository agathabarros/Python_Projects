friends = ["Rolf", "Bob", "Jen", "Anne"]
guests = ["jose", "Bob", "Michael", "jen", "Anne"]

friends_lower = set([f.lower() for f in friends])
#guests_lower = set([g.lower() for g in guests])

#print(friends_lower.intersection(guests_lower))

present_friends = [
    name.title() 
    for name in guests 
    if name.lower() in friends_lower
]

print(present_friends)
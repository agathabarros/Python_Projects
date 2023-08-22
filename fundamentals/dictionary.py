friends = ["Rafinha", "Raysa", "Dudu", "Duda", "Yuri", "Arthur", "Breno", "Dani"]
time_since_seen = [3, 7, 15, 11, 9, 10, 5, 2]

long_timers = {
    friends[i] : time_since_seen[i]
    for i in  range(len(friends))
if time_since_seen[i] > 10
}
print(long_timers)
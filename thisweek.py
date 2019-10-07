# more strings and text

X = "there are xd types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

print(X)
print(y)

print("I said: %r.:" % X)
print("I also said : '%s' ")

hilarious = True
jokeEvaluation = "isn't that joke so funny?! %r"

print(jokeEvaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w+e)

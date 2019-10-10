# more strings and text

X = "there are %d types of people." % 10
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

# more printing fun
print("mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everyone that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

# But wait! There's more:
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# why do i use %r instead of %s it the above example?

days = "mon tue wed thu fri sat sun"
months = "Jan\nFeb\nMar\naApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months ", months)

print("""
There's something going on here.
with the three double-qoutes.
we'll be able to type as much as we like.
even 4 lines if we want.
""")

# escape seq             what it does?
# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \{name}
# \r
# \t
# \uxxxx
# \uxxxxxxxx
# \v
# \ooo
# \xhh

print('apple\torange')
print('apple\norange')
print('apple\rorange')
print('apple\vorange')
print('apple\000orange')
print('apple\aorange')
print('apple\borange')
print('apple\forange')
print('apple\\orange')
print('apple\'orange')
print('apple\"orange')

# what does the following code do?
#   while True:
#       for i in ["/", "-", "|", "\\", "|"]:
#           print("%s\r" % i, end='')

# can you use ''' instead of """ ? YES

age = input("how\000old are you?")
height = input("how tall are you?")
print("so, you are %r old and %r tall." % (age, height))
eye = input("what's your eye color?")
hair = input("what color is your hair?")
print("so, your eye color is %r and your hair is %r." % (eye, hair))
food = input("what's your favorite food")
color = input("what's your favorite color")
print("so your favorite food is %r an your favorite color is %s." % (food, color))

name = input('his name was?')
age = input('he was')
hair = input('he had dark')
eye = input ('and light.')
shoes = input('He always had on,')
food = input('He was always eating')

print('There was a boy and his name was %r, he was %r years old.' % (name, age))
print('He had dark %r hair and light %r eyes.' % (hair, eye))
print('He always had on a pair of %r on, and love eating %r.' % (shoes, food))

































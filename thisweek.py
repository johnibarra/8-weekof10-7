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

# escape sequence















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






























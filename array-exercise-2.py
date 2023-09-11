# You have a list of your favourite marvel super heros.

heros: list[str] = ["spider man", "thor", "hulk", "iron man", "captain america"]

# Using this find out,

# Length of the list

print(len(heros))

# Add 'black panther' at the end of this list

heros.append("blank panther")
print(heros)

# You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'

heros.remove("blank panther")
heros.insert(3, "blank panther")
print(heros)

# Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

heros[1:3] = ["doctor strange"]
print(heros)

# Sort the heros list in alphabetical order (Hint. 
# Use dir() functions to list down all functions available in list)

heros.sort()
print(heros)


"""

Implement the function likes which takes an array containing the names of people
that like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

"""

def likes(names):
    s = "like this"
    if len(names) == 0:
        s = "no one likes this"
    elif len(names) == 1:
        s = f"{names[0]} likes this"  
    elif len(names) == 2:
        s = f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        s = f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        s = f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    return s

print(likes(["Alex", "Jacob", "Mark", "Max"]))
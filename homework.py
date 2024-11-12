names = ["Aaron", "Chethana", "Bengisu", "Rashika", "Ratika", "Shashi", "Trevor", "Pragathi", "Josephine", "Ayla", "Charlotte"]


def linearsearching(n):
    for i in names:
        if i == n:
            return n
    return ("not found")

print(linearsearching("Ratik"))
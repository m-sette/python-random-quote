import random


def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    for i in range(3):
        rnd = random.randint(0, last)
        print(i, quotes[rnd].rstrip())


if __name__ == "__main__":
    primary()

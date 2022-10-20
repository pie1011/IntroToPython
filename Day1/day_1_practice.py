movies = ["Inception", "Tenet", "Interstellar", "Memento"]

for i in movies:
    print(i)

for i, val in enumerate(movies):
    print(f"{i}: {val}")

for i in range(1, 10):
    print(i)


def check(one):
    print(one)
    return

check(1)
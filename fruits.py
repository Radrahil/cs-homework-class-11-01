def fruit(name):
    k = 2
    for i in range(0, 3):
        for j in range(0, k):
            print(end=" ")
        k -= 1

        for j in range(0, i + 1):
            print(name + " ", end="")
        print("\r")


fruit("#")
fruit("$")
fruit("&")

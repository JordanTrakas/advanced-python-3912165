# Example file for Advanced Python by Joe Marini
import itertools

# define a list of days in English, French, and German
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
daysGm = ["Son", "Mon", "Dien", "Mit", "Don", "Fre"]

# The implementation below is more verbose and complex than it needs to be
# for d in range(len(days)):
#     print(d+1, days[d])

# the enumerate function
# for i, d in enumerate(days, start=1):
#     print(i, d)

# use zip to combine sequences
# for d in zip(daysFr, daysFr, daysGm):
#     print(d)

# use enumerate and zip together
# for i, d in enumerate(zip(days, daysFr, daysGm)):
#     print(i+1, d[0], "=", d[1], "in French", "=", d[2], "in German")

# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"

# for i in itertools.zip_longest(seq1, seq2, seq3):
#     print(i)

result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="-")
print("Result:")
for item in result:
    print(item)

lears= ["diamonds", "clubs ", "hearts", "spades"]
cards= [i for i in range(2,11)]
y= ["A"] +cards + ["J", "Q", "K"]
def deck(lear, cards):
    for k in lear:
        for i in cards:
            yield(i , k)
try:
    while True:
        print(next(deck(lears,y)))
except StopIteration:
    print("Всі карти виведено")
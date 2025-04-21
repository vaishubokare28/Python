def count_up_to(n):
    i=1
    while i<=n:
        yield i
        i+=1

counter=count_up_to(3)

print(next(counter))
print(next(counter))
print(next(counter))

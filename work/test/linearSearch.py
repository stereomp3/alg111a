import fp


def linearSearch(a, x):
    n = len(a)
    # ri = -1
    # fp.each(range(0,n), lambda i:
    #     i if x==a[i] else None
    # )
    return fp.each(range(0,n), lambda i:
        print('linearSearch(a, 6)=' + i) if x==a[i] else None
    )

a = [3,7,2,6,8,4]
print('a=', a)
print('linearSearch(a, 6)=', linearSearch(a, 6))


import timeit

def multiply():
    for i in range(1000000, 1000016):
        pow(i, i)
        print('okay')

R = 10
N = 1

t = timeit.Timer(multiply)
duration = t.repeat(repeat=R, number=N)

print(f"Time to complete({N} times repeated x{R} ): {round(min(duration), 2)}")

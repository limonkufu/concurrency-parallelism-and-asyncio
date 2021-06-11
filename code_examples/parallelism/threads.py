import concurrent.futures
import timeit

def multiply():
    pow_list = [i for i in range(1000000, 1000016)]


    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(pow, i, i) for i in pow_list]

    for f in concurrent.futures.as_completed(futures):
        print('okay')


if __name__ == "__main__":

    print("Starting...")
    
    R = 10
    N = 1

    t = timeit.Timer(multiply)
    duration = t.repeat(repeat=R, number=N)

    print(f"Time to complete({N} times repeated x{R} ): {round(min(duration), 2)}")
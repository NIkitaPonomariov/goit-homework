import time
from multiprocessing import Pool, cpu_count

def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    return [factorize_number(number) for number in numbers]

def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(factorize_number, numbers)
    return result

if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)

    start_time = time.time()
    result = factorize(*numbers)
    end_time = time.time()
    print(f"Synchronous result: {result}")
    print(f"Synchronous time: {end_time - start_time} seconds")

    start_time = time.time()
    result = factorize_parallel(*numbers)
    end_time = time.time()
    print(f"Parallel result: {result}")
    print(f"Parallel time: {end_time - start_time} seconds")

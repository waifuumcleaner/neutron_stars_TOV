import timeit
import gc

def warm_up(method, *args, runs=10):
    for _ in range(runs):
        method(*args)

def time_test(method, *args, runs=200):
    """
    Measures the average execution time of a given method over multiple runs.
    """
    # Disable garbage collection for accurate timing
    gc.disable()

    # Warm up the method to avoid initialization overhead
    warm_up(method, *args)

    # Measure execution time using timeit for precision
    wrapped_method = lambda: method(*args)
    times = timeit.repeat(wrapped_method, repeat=runs, number=1)

    # Re-enable garbage collection after timing
    gc.enable()

    average_time = sum(times) / len(times)
    return average_time * 1000  # Return time in milliseconds




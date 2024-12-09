import math
import time
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count

logging.basicConfig(
    filename="integration.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


def integrate_part(f, start, end, n_iter):
    acc = 0
    step = (end - start) / n_iter
    for i in range(n_iter):
        acc += f(start + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    span = (b - a) / n_jobs
    part_iter = n_iter // n_jobs
    futures = []

    start = time.time()
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start_point = a + i * span
            end_point = start_point + span
            logging.info(f"Starting job for range [{start_point}, {end_point}]")
            futures.append(
                executor.submit(integrate_part, f, start_point, end_point, part_iter)
            )

        result = sum(future.result() for future in futures)
    end = time.time()
    logging.info(f"Integration complete. Time: {end - start} seconds")
    return result, end - start


def integrate_with_process(f, a, b, *, n_jobs=1, n_iter=10000000):
    span = (b - a) / n_jobs
    part_iter = n_iter // n_jobs
    futures = []

    start = time.time()
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start_point = a + i * span
            end_point = start_point + span
            logging.info(f"Starting process for range [{start_point}, {end_point}]")
            futures.append(
                executor.submit(integrate_part, f, start_point, end_point, part_iter)
            )

        result = sum(future.result() for future in futures)
    end = time.time()
    logging.info(f"Integration with processes complete. Time: {end - start} seconds")
    return result, end - start


if __name__ == "__main__":
    a = 0
    b = math.pi / 2
    cpu_count_num = cpu_count()

    with open("results.txt", "w") as f:
        for n_jobs in range(1, cpu_count_num * 2 + 1):
            result_thread, time_thread = integrate(math.cos, a, b, n_jobs=n_jobs)
            result_process, time_process = integrate_with_process(
                math.cos, a, b, n_jobs=n_jobs
            )

            f.write(f"jobs: {n_jobs}\n")
            f.write(
                f"ThreadPoolExecutor: time = {time_thread:.4f} seconds, result = {result_thread}\n"
            )
            f.write(
                f"ProcessPoolExecutor: time = {time_process:.4f} seconds, result = {result_process}\n\n"
            )

import multiprocessing
import queue
import time
import codecs
from datetime import datetime

def log(message):
    return f"[{datetime.now()}] {message}"

def logger(log_queue):
    with open("interaction_log.txt", "a") as logfile:
        while True:
            try:
                message = log_queue.get(block=True)
                logfile.write(message + "\n")
                logfile.flush()
                print(message)
            except queue.Empty:
                continue

def process_a(to_b_queue, from_main_queue, log_queue):
    while True:
        try:
            message = from_main_queue.get(block=True, timeout=1)
            log_queue.put(log(f"Process A: Received message: {message}"))
            message_lower = message.lower()
            log_queue.put(log(f"Process A: Result message: {message_lower}"))
            time.sleep(5)
            to_b_queue.put(message_lower)
        except queue.Empty:
            continue

def process_b(to_main_queue, from_a_queue, log_queue):
    while True:
        try:
            message = from_a_queue.get(block=True, timeout=1)
            log_queue.put(log(f"Process B: Received message: {message}"))
            rot13_message = codecs.encode(message, 'rot_13')
            log_queue.put(log(f"Process B: Result message: {rot13_message}"))
            to_main_queue.put(rot13_message)
        except queue.Empty:
            continue

def main():
    from_main_queue = multiprocessing.Queue()
    to_b_queue = multiprocessing.Queue()
    back_to_main_queue = multiprocessing.Queue()
    log_queue = multiprocessing.Queue()

    logger_process = multiprocessing.Process(target=logger, args=(log_queue,))
    logger_process.start()

    p_a = multiprocessing.Process(target=process_a, args=(to_b_queue, from_main_queue, log_queue))
    p_b = multiprocessing.Process(target=process_b, args=(back_to_main_queue, to_b_queue, log_queue))

    p_a.start()
    p_b.start()

    try:
        while True:
            input_message = input("Enter a message (or 'quit' to exit): ")

            if input_message == 'quit':
                break

            from_main_queue.put(input_message)

            try:
                log_queue.put(log(f"Main Process: Received message: {input_message}"))
                response = back_to_main_queue.get(block=True, timeout=6)
                log_queue.put(log(f"Main Process: Received coded message: {response}"))
            except queue.Empty:
                log_queue.put("[Error] Timeout waiting for response from process B.")

    finally:
        p_a.terminate()
        p_b.terminate()
        logger_process.terminate()

if __name__ == "__main__":
    main()

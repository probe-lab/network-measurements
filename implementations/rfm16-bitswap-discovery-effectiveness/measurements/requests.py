#!/usr/bin/python

import threading, subprocess, os, signal, time
from functools import partial

ipfs = "./ipfs"
filename = "cids/cids.txt"
n_threads = 5


class Requester(threading.Thread):
    def __init__(self, i, lock, file):
        threading.Thread.__init__(self)
        self.threadID = i
        self.lock = lock
        self.file = file
        self.alive = True

    def run(self):
        while t.alive:
            # acquire lock to avoid race of the file
            lock.acquire()
            # read one cid
            line = file.readline()[:-1]
            # release lock
            lock.release()

            # break when we reach the end of the file
            if len(line) == 0:
                lock.acquire()
                t.alive = False
                lock.release()
                break

            # use ipfs cli to request the cid
            process = subprocess.Popen(
                [ipfs, "get", line], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            # process should be over, but just to make sure that we don't open too many threads
            c = 0
            # 90 seconds time out while the process is not over
            while process.poll() is None and c < 900 and self.alive:
                c += 1
                time.sleep(0.1)

            # avoid race in stdout
            lock.acquire()
            if process.poll() is None:
                # if process not over yet, kill it
                process.terminate()
                print("terminated", line)
            lock.release()


def sigterm_handler(signum, frame, threads):
    print("exiting gracefully")
    for t in threads:
        t.alive = False
    time.sleep(1)
    exit(1)


if __name__ == "__main__":

    # open cids file
    file = open(filename, "r")
    # create lock
    lock = threading.Lock()

    threads = []
    for i in range(n_threads):
        threads.append(Requester(i, lock, file))

    sigterm_handler = partial(sigterm_handler, threads=threads)
    signal.signal(signal.SIGTERM, sigterm_handler)

    for t in threads:
        t.start()

    time.sleep(10)

    # Wait for all threads to complete
    done = False
    while not done:
        time.sleep(1)
        done = True
        for t in threads:
            done = done and not t.alive

    print("All done, closing file")

    file.close()


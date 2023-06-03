import threading

class ReadWriteLock:
    def __init__(self):
        self.mutex = threading.Lock()
        self.read_cv = threading.Condition(self.mutex)
        self.write_cv = threading.Condition(self.mutex)
        self.readers = 0
        self.writers = 0

    def acquire_read(self):
        with self.mutex:
            while self.writers > 0:
                self.read_cv.wait()
            self.readers += 1

    def release_read(self):
        with self.mutex:
            self.readers -= 1
            if self.readers == 0:
                self.write_cv.notify()

    def acquire_write(self):
        with self.mutex:
            while self.readers > 0 or self.writers > 0:
                self.write_cv.wait()
            self.writers += 1

    def release_write(self):
        with self.mutex:
            self.writers -= 1
            self.read_cv.notify_all()
            self.write_cv.notify()


# Create a ReadWriteLock object
rwlock = ReadWriteLock()

# Define a shared resource
shared_resource = []

# Define a reader function
def reader():
    rwlock.acquire_read()
    print(f"Reader {threading.get_ident()} acquired the read lock.")
    print(f"Reader {threading.get_ident()} read the shared resource: {shared_resource}")
    rwlock.release_read()

# Define a writer function
def writer():
    rwlock.acquire_write()
    print(f"Writer {threading.get_ident()} acquired the write lock.")
    shared_resource.append(threading.get_ident())
    print(f"Writer {threading.get_ident()} wrote to the shared resource: {shared_resource}")
    rwlock.release_write()

# Create some threads to read from the shared resource
readers = []
for i in range(5):
    t = threading.Thread(target=reader)
    readers.append(t)
    t.start()

# Create some threads to write to the shared resource
writers = []
for i in range(2):
    t = threading.Thread(target=writer)
    writers.append(t)
    t.start()

# Wait for all the threads to finish
for t in readers + writers:
    t.join()
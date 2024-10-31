import threading

class FileAppenderSingleton:
    _instance = None
    _lock = threading.Lock()  

    def __new__(cls, file_path="test.txt"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(FileAppenderSingleton, cls).__new__(cls)
                    cls._instance.file_path = file_path
        return cls._instance

    def append_to_file(self, text):
        with open(self.file_path, "a") as file:
            file.write(text + "\n")


def append_text(text):
    file_appender = FileAppenderSingleton() 
    file_appender.append_to_file(text)


if __name__ == "__main__":
    
    thread1 = threading.Thread(target=append_text, args=("Hello from Thread 1",))
    thread2 = threading.Thread(target=append_text, args=("Hello from Thread 2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Text appended to test.txt using a Singleton instance.")


# adv: single instance obj and also is global... dis: so many ways which to follow based oncases
# used thread level 
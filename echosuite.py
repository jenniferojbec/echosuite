import os
import subprocess
import time
import threading
from typing import List

class EchoSuite:
    def __init__(self):
        self.background_tasks = []
        self.foreground_task = None
        self.is_running = True

    def add_background_task(self, command: List[str]):
        self.background_tasks.append(command)

    def set_foreground_task(self, command: List[str]):
        self.foreground_task = command

    def run_task(self, command: List[str]):
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {command}: {e}")

    def run_foreground_task(self):
        if self.foreground_task:
            print(f"Running foreground task: {self.foreground_task}")
            self.run_task(self.foreground_task)

    def run_background_tasks(self):
        while self.is_running:
            for task in self.background_tasks:
                print(f"Running background task: {task}")
                self.run_task(task)
                time.sleep(5)  # Sleep for 5 seconds before switching tasks

    def start(self):
        background_thread = threading.Thread(target=self.run_background_tasks)
        background_thread.start()
        try:
            while self.is_running:
                self.run_foreground_task()
                time.sleep(30)  # Switch to foreground task every 30 seconds
        except KeyboardInterrupt:
            print("Shutting down EchoSuite...")
            self.is_running = False
            background_thread.join()

if __name__ == "__main__":
    echo_suite = EchoSuite()
    echo_suite.add_background_task(["notepad.exe"])
    echo_suite.add_background_task(["calc.exe"])
    echo_suite.set_foreground_task(["mspaint.exe"])
    echo_suite.start()
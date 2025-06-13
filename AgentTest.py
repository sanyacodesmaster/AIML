import os
import time

class DataProcessor:
    def __init__(self, secret_key):
        # TODO: Securely handle secret keys later
        self.secret_key = secret_key

    def run_heavy_computation(self):
        # Inefficient busy wait — performance issue
        start_time = time.time()
        while time.time() - start_time < 5:
            pass  # busy wait for 5 seconds instead of sleep

    def execute_command(self, user_input):
        # SECURITY ISSUE: executing user input directly
        os.system(user_input)

    def process_data(self, data):
        """
        FIXME: This function is slow and unoptimized
        Processes data in a naive way
        """
        result = []
        for item in data:
            # Simulate some processing
            result.append(item * 2)
        return result

def main():
    processor = DataProcessor("hardcoded-secret-key-1234")  # Hardcoded secret (security issue)
    processor.run_heavy_computation()
    processor.execute_command("ls -l")  # Unsafe command execution
    processed = processor.process_data([1, 2, 3, 4])
    print(processed)

if __name__ == "__main__":
    main()

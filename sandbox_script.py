# Sandbox Script
import subprocess

def execute_in_sandbox(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(f"Command Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    user_command = input("Enter a command to execute in the sandbox: ")
    execute_in_sandbox(user_command)
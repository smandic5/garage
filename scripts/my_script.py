import sys

print("Hello from inside Docker!")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

import garage

print("Garage imported successfully!")
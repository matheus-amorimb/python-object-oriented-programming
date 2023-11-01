import sys
import os

# Add the root directory of your project to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.BankAccount import BankAccount

# Rest of your main.py script

print('funcionando')
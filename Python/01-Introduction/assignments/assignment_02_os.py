import os

# Using relative path based on the script location
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

print('Exists:', os.path.exists(path))

if os.path.exists(path):
    print('Contents:', os.listdir(path))


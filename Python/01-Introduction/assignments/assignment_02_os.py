import os

path = r"D:\AI-LLM-Engineer\Python\01-Introduction"

print("Path:", path)
print("Exists:", os.path.exists(path))

if os.path.exists(path):
    print(os.listdir(path))
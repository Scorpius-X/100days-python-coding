#learning about python exceptions

try:
    file = open("file1.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["aws"])
except FileNotFoundError:
    file = open("./100days-python-coding/Day30/file1.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")

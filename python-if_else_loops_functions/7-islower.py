 #!/usr/bin/python3

def islower(c):
    """
    Returns True if c is a lowercase character, False otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')

print(islower("a"))  
print(islower("H"))  
print(islower("3"))  
print(islower("g"))

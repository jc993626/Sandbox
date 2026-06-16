"""Video exercise."""

def is_adult(age):
    return age >= 18 # returns boolean   T/F

print(f"got {is_adult(18)}, expected True")
print(f"got {is_adult(17)}, expected False")
# Question 1: Mutable and Immutable Objects

# mutable object: list
marks = [70, 80, 90]

print("Original list:", marks)

marks[0] = 75

print("Modified list:", marks)


#  immutable object: string
name = "Python"

print("\nOriginal string:", name)

name = "J" + name[1:]

print("New string:", name)


# Rewrite the code so that modifying values does not change numbers.


numbers = [1, 2, 3]
values = numbers.copy()

values.append(4)

print(numbers)  #[1,2,3]
print(values) # [1,2,3,4]



# Rewrite the code so that modifying values does not change numbers.

def update_list(items):
    new_items = items.copy()
    new_items.append(100)
    return new_items

scores = [50, 60, 70]
new_score=update_list(scores)
print(scores)
print(new_score)



# Question 5: Memory Management and Garbage Collection

name_list=["tehdi", "yousuf", "muhammed"]

new_name_list=name_list

del name_list
print(new_name_list)
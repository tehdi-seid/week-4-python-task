
**Question 1.**
=> A mutable object can be changed after it has been created.

For example list, dict, set etc....

=> An immutable object cannot be changed after it has been created.
For example touples, strng,  int etc...


**Question 2**.

What is the output?

True
False
True

Explain the difference between is and ==.

is => it checks weather the two variables are referencing the same object or not 

= => it checks the value inside the variables

Why do a and c have the same values but different identities?

=> that is because of they are referencing different object

**Question 3**

Predict the output.

 ```bash

 [1, 2, 3, 4]
 
 ```


Explain why modifying values also affects numbers.

=> because they are referencing the same object

Rewrite the code so that modifying values does not change numbers.

**Question 4**

```bash

[50, 60, 70, 100]

```

**Explain why the original list changes after the function call.**

The function receives a reference to the original list. Calling items.append(100) changes the shared list.
**Question 5**

Python manages objects in memory and tracks references to them.
The statement del numbers removes the name numbers; it does not necessarily destroy the object. If another variable still refers to the object, that object remains accessible.

When an object is no longer reachable, Python can reclaim its memory. CPython uses reference counting and a cyclic garbage collector to handle unreachable reference cycles.


**mini project**

**Why does modifying a shared reference affect the original list?**
=> that is because of they are refferencing the same object and modifying one affects the other too

**Why does modifying the copied list not affect the original list?**

cause the copied list is referencing another object it created it own object but it contains the copy of the original
**What is the difference between equality and identity in Python?**

=> Equality checks the values inside the objects 

=> but Identity checks their reference
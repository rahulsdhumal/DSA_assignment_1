# Q4. Write a program to print the first non-repeated character from a string?

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return f"First non-repeated character is : {c}"
  return f"Either all characters are repeating or string is empty"
str1=input("Enter a string : ")
print(first_non_repeating_character(str1))
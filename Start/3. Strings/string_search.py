# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."
temp_str = sample_text.lower()

# Using find() to find the first occurrence of a substring
# print("First occurrence of 'the': index", temp_str.find('the'))

# Example with optional start and end parameters
# print("First occurrence of 'the': index", sample_text.find('the', 5, 15))
# print("First occurrence of 'the': index", sample_text.find('the', 5, 40))


# Using index() to find the first occurrence of a substring (raises ValueError if not found)
# print("First occurrence of 'fox': index", temp_str.index('fox'))
# try:
#     print("First occurrence of 'fax': index", temp_str.index('fax'))
# except ValueError:
#     print("Not found")

# The 'in' operator can be used for Boolean testing:
# print('Fox' in sample_text)

# Using rfind() to find the last occurrence of a substring
print("Last occurrence of 'the'", sample_text.rfind('the'))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print("Last occurrence of 'jump'", sample_text.rindex('jump'))

# The replace() function will find content in the string and replace it
result = sample_text.replace('lazy', 'tired')
print(result)
temp_str_1 = temp_str
result_2 = temp_str_1.replace('The', 'THE')
print(result_2)
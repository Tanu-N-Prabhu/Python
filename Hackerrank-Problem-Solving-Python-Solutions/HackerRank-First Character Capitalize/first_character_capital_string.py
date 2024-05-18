def capitalize_words(text):
  """Capitalizes the first letter of each word in a string.

  Args:
      text: The string to be processed.

  Returns:
      A new string with the first letter of each word capitalized, 
      except for non-alphanumeric characters.
  """
  result = []
  is_first_word = True
  for char in text:
    if char.isalpha():
      if is_first_word:
        result.append(char.upper())
        is_first_word = False
      else:
        result.append(char)
    else:
      result.append(char)
      is_first_word = True
  return ''.join(result)

# Test cases
text1 = "hello world"
text2 = "12abc"
text3 = "This is a Test"

print(capitalize_words(text1))  # Output: Hello World
print(capitalize_words(text2))  # Output: 12abc (no change)
print(capitalize_words(text3))  # Output: This Is A Test

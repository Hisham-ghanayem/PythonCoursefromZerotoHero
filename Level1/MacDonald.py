def cap_sentence(mystring):
  name_list = list(mystring)
  modified_name_list = []

  for index, char in enumerate(name_list):
    if index == 0 or index == 3: # Check for the first (index 0) and fourth (index 3) positions
      modified_name_list.append(char.capitalize()) # Capitalize and add to the new list
    else:
      modified_name_list.append(char) # Add the character as is

  # Join the modified characters back into a string
  result_string = "".join(modified_name_list)
  return result_string
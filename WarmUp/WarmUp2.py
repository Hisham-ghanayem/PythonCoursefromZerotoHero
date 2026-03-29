#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
#def animal_crackers(text):
    #pass
# Check
#animal_crackers('Levelheaded Llama')
# Check
#animal_crackers('Crazy Kangaroo')

def animal_crackers(text):

  list_string = text.split()
  if list_string [0][0] == list_string [1][0]:
    return True
  else:
    return False
#Rules for def:
#If the key is in the dictionary, add the value to the list stored by that key.
#If the key is not in the dictionary, add the value to the list by the key 2∗key.
#If there is no key 2∗key, add the key 2∗key to the dictionary
# and match it with the list from the passed element [value].
def update_dictionary(d, key, value):
  if key in d:
    d.setdefault(key,[]).append(value)
  if key not in d and 2*key in d:
    d.setdefault(2*key,[]).append(value)
  if key not in d and 2*key not in d:
    d.update({2 * key : [value]})
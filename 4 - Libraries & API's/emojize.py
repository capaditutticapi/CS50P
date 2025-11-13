from emoji import emojize
text = input(("Input: "))
converted = emojize(text,language="en")
converted = emojize(converted,language="alias")
print("Output: ", converted)

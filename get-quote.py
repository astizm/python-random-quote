def quote():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  #f.write("\nAll things are difficult before they are easy")
  f.close()

 
  for a_quote in quotes:
   print(a_quote, end='')

if __name__== "__main__":
  quote()

try:
   fd = open("testfile2", "w")
   fd.write("This is my mathematics file!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fd.close()
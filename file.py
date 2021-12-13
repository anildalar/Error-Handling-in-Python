

filename = input("Please enter the filename ")
filename = filename+'.txt'

try:
  f = open(filename)
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")




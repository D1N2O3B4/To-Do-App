from urllib.request import urlretrieve

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

urlretrieve(url1,"./Created/read1.txt")
urlretrieve(url2,"./Created/read2.txt")
urlretrieve(url3,"./Created/read3.txt")

def header_split(obj):
  return obj.strip().split(",")

def to_list(obj):
  new_values = []
  for i in obj.strip().split(","):
    if i[::-1] != "":
      new_values.append(i)
    else:
      new_values.append(0.0)
  return new_values
    

def group(objects):
  total = []

  a = [object for object in objects if objects[0] == object]
  b = [object for object in objects if objects[1] == object]  
  c = [object for object in objects if objects[2] == object]
  d = [object for object in objects if objects[3] == object]
  total.append(a)
  total.append(b)
  total.append(c)
  total.append(d)
  return total
  


dicty = {}
total = []
with open("./Created/read1.txt","r") as f:
  fil = f.readlines()
  headers = header_split(fil[0])
  values = fil[1:]

  for value in values:
    set_list = to_list(value)
    # print(set_list)
    total.append(group(set_list))
print(total)

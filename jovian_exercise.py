from urllib.request import urlretrieve

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

urlretrieve(url1,"./Created/read1.txt")
urlretrieve(url2,"./Created/read2.txt")
urlretrieve(url3,"./Created/read3.txt")





def header_split(obj):
  return obj.strip().split(",")

def values_split(obj):
  value_list = []
  for i in obj.strip().split(","):

    try:
        value_list.append(float(i))
    except ValueError:
        value_list.append(0.0)
    return value_list

final = []
with open("./Created/read.txt","r") as r:
    p = r.readlines()
headers = p[0]
arranged_headers = split_headers(headers)
values = p[1:]

for i in values:
    arranged_values = split_values(i)
    end = dictyfy(arranged_values,arranged_headers)
    final.append(end)
print(final)

def read_csv_columnar(path):
  with open(path,"r") as f:
    read_f = f.readlines()
    headers = read_f[0]
    values = read_f[1:]
    ultimate = {}
    good_vals = values_split(values)
    good_headers = header_split(headers)
    print(good_headers)
    print(good_vals)

    # for i in good_headers:
    #   ultimate[i] = 

read_csv_columnar("./Created/read1.txt")


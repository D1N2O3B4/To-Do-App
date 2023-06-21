import numpy as np
# from urllib.request import urlretrieve

# url_1 = "https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images/download?datasetVersionNumber=1"

# urlretrieve(url_1,"./Created/url.txt")#retireves only web content not files

a = [19,23,34]
b = [90,15,12]

a = np.array(a)
b = np.array(b)

print(a)
print(b)

print(np.matmul(a,b))
print(a @ b)

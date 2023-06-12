from urllib.request import urlretrieve

url_1 = "https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images/download?datasetVersionNumber=1"

urlretrieve(url_1,"./Created/url.txt")#retireves only web content not files

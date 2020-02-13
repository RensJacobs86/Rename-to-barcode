import pandas as pd
import os

print("processing...")

path = os.getcwd()

for x in os.listdir(path):
    if x[-3:] == "csv":
        data = pd.read_csv(filepath_or_buffer=path + "\\" + x)
    elif x[-4:] == "xlsx":
        data = pd.read_excel(path + "\\" + x)

catalog = [x for x in data[data.columns[0]]]
upc = [str(x) for x in data[data.columns[1]]]
new_upc = []

# om barcodes 13 cijfers te geven
for x in upc:
    if len(x) == 12:
        new_upc.append("0" + x)
    elif len(x) == 11:
        new_upc.append("00" + x)
    else:
        new_upc.append(x)

for x in os.listdir(path):
    if x[-4:] == "jpeg":
        os.rename(os.path.join(path, x), os.path.join(path, x[:-4] + "jpg"))

for index, plaatje in enumerate(catalog):
    for cover in os.listdir(path):
        if cover[:-4] == plaatje:
            os.rename(os.path.join(path, cover), os.path.join(path, new_upc[index] + ".jpg"))

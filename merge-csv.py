import pandas as pd
from pathlib import Path

#-----ścieżka do plików-----
path = str(Path(__file__).parent.absolute()) #jeśli pliki w tym samym folderze co skrypt
#path = ""  #jeśli nie,, podajemy ścieżke do plików

filename1 = path + "\\file1.csv"
filename2 = path + "\\file2.csv"
filename_res = "result.csv"


#-----wczytaj dane--------
print("reading data...")

data1 = pd.read_csv(filename1)
data2 = pd.read_csv(filename2)


#-------mergowanie-------
print("merging...")

join_type = "inner"

#jeśli klucz ta sama nazwa
key = "ID"
out = pd.merge(data1, data2, on=key, how=join_type)

#jeśli inna nazwa kluczy
# key1 = "ID"
# key2 = "ID2"
# out = pd.merge(data1, data2, left_on = key1, right_on=key2, how=join_type)


#-------zapis do wynikowego csv-----------
print("writing to file...")

out.to_csv(filename_res, index=False)

print("file saved")

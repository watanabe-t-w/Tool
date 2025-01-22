import sys
import csv

args = sys.argv

if len(args) != 2:
    print("Usage: python convert.py filename.csv")
    exit()

output = []
with open(args[1], encoding="shift_jis") as f:
    reader = csv.reader(f)
    for row in reader:
        output.append({
            "code": row[2],
            "pref": row[6],
            "addr": row[7] + row[8].replace("以下に掲載がない場合", "").split("（")[0]
        })

f = open("zipcode.js", "w", encoding="utf-8")
f.write("const zipcode = ")
f.write(str(output))
f.close()

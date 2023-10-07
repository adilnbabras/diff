import os
import sys

G = '\033[92m'  # green
R = '\033[91m'  # red
W = '\033[0m'   # white

result = os.popen(f"diff -u {sys.argv[1]} {sys.argv[2]} | tee ./blahblah.txt").read()

with open("./blahblah.txt", "r") as txt_file:
  result_3 = txt_file.readlines()
txt_file.close()

os.popen("rm -r ./blahblah.txt")

for i in result_3:
    if i.startswith('-'):
        print(R + i + W)
    elif i.startswith('+'):
       print(G + i + W)
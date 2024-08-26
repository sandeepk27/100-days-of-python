# Day 73 of code!
# Write your code here.

import os

files = os.listdir("clutteredFolder")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
    i = i + 1
    
    
#from PyPDF2 import PdfWriter
# import os

# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()
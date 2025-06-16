import os
import time

director = "studio"

if not os.path.exists(f"{director}"):
    os.mkdir(f"{director}")
    print(f" Now {director} is created")

read= os.access(f"{director}", os.R_OK)
write= os.access(f"{director}", os.W_OK)
exicute = os.access(f"{director}", os.X_OK)

print(f"Sleep Time Start")



print(f" The {director} Current Permission is {read} {write} {exicute}")   #drwxr-xr-x

time.sleep(120)

print(f"Sleep Time Stop")

change_read= os.chmod(f"{director}", 0o400)

print(f"The {director} now update perrmisson is {change_read} {write} {exicute} ")  #dr--------



    
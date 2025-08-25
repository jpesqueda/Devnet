devices=[]
# file=open("devices.txt","r")
# for item in file:
#    item=item.strip()
#    devices.append(item)
# file.close()
# print(devices)



file = open("devices.txt", "a")
while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()

print(devices)

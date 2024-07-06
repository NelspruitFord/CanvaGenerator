import csv

lookup = []

while True:
    temp = input("Stock number to search: ")
    if temp == "":
        break
    lookup.append(temp)

fields = ["Stock Number", "Vehicle Code", "Make", "Model", "Specification", "VIN", "Registration Date", "Odometer", "Colour", "Internet Price", "Fuel Type", "Transmission"]

carsToLoad = []

with open(r"C:\Users\KewanSeymour\OneDrive - PRODUKTA MOTORS\Documents\Daily Stock Recon\Pinnacle Stock Export\PinnacleStockExport.csv") as fileObject:
    readerObject = csv.DictReader(fileObject)

    for row in readerObject:
        if row['Stock Number'] in lookup:
           
            car = {k:v for k,v in row.items() if k in fields}
            carsToLoad.append(car)

for i in carsToLoad:
    i["Registration Date"] = i["Registration Date"][-4:]
            
with open(r"C:\Users\KewanSeymour\OneDrive - PRODUKTA MOTORS\Documents\Code\Details Generator\detailsToLoad.csv", "w") as fileObject:
    
    writer = csv.DictWriter(fileObject, fieldnames=fields)
    writer.writeheader()
    writer.writerows(carsToLoad)

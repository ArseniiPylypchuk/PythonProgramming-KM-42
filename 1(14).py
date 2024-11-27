import csv

with open("Enya.csv", "w") as musician:
    info_about_fav_songs =["song", "year"]
    writer= csv.DictWriter(musician, fieldnames=info_about_fav_songs)
    writer.writeheader()
    writer.writerow({"song" : "Carribean Blue ", "year" : 1991})
    writer.writerow({"song":'Orinoco Flow', "year": '1988'})
    writer.writerow({"song":'Only If', "year":'1997'})
    writer.writerow({"song": 'Only time',"year":'2000'})
    writer.writerow({"song" :'Boadicea', "year":'1987'})
with open("Enya.csv" , newline='') as musicians:
    reader = csv.DictReader(musicians)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print("\n")
    for row in reader:
        print(row['song'], row['year'])
monthslist = ["January","February","March","April","May","June","July","August","September","October","November","December"]
while True:
    date = input("Date: ")
    if "/" in date:
        datesplit= date.split(sep = "/") 
        if len(datesplit) == 3:
            pass 
        else:
            continue 

        try:
            month = int(datesplit[0])
            day = int(datesplit[1])
            year = int(datesplit[2])
            if not (0 < month < 13 and 0 < day < 32 and year > 0):
                raise ValueError
        except ValueError:
            continue 

        print(f"{year:04}-{month:02}-{day:02}")       
        break

    elif "," in date:
        date = date.replace("," , "") 
        datesplit = date.split(sep = " ")
        if len(datesplit) == 3:
            pass
        else:
            continue 

        month = datesplit[0]
        try:
            monthsdict = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
            month = monthsdict[month]
        except KeyError:
            continue 

        try:
            day = int(datesplit[1])
            year = int(datesplit[2])
            if not (0 < day < 32 and 0 < year):
                raise ValueError
        except ValueError:
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    else:
        continue 

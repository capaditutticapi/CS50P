import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if time := re.search(r"(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)", s):
      
        hour1 = int(time.group(1))
        mins1 = time.group(2)
        ampm1 = time.group(3)
        hour2 = int(time.group(4))
        mins2 = time.group(5)
        ampm2 = time.group(6)

        if ampm1 == "PM" and hour1 != 12:
            hour1 = hour1+12
        if ampm2 == "PM" and hour2 != 12:
            hour2 = hour2+12
        if mins1 == None:
            mins1 = ":00"
        if mins2 == None:
            mins2 = ":00"
        #  edge 12 cases: 12 AM = 00:00 and adding 0 prefix to single digit hours
        if hour1 == 12 and ampm1 == "AM":
            hour1 = "00"
        elif int(hour1) < 10:
            hour1 = f"0{hour1}"
        if hour2 == 12 and ampm2 == "AM":
            hour2 = "00"
        elif int(hour2) < 10:
            hour2 = f"0{hour2}"

        return f"{hour1}{mins1} to {hour2}{mins2}"
    else:
        raise ValueError



if __name__ == "__main__":
    main()

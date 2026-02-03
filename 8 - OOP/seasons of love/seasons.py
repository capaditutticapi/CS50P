from datetime import date, datetime, timedelta
import sys
import inflect

def main():
    dob = input("Date of Birth: ")
    formatted_dob = verify(dob)
    minutes_transcurred = difference(formatted_dob)
    english_minutes = convert_to_english(minutes_transcurred).capitalize()
    print(f"{english_minutes} minutes")

#verify date is entered in correct format
def verify(date):
    try:
        formatted_dob = datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid Date")
    return formatted_dob

#calculate minutes from dob to today
def difference(dob):
    diff = date.today() - dob.date()
    return diff.days*24*60

#convert numbers to english using inflect module
def convert_to_english(mins):
    p = inflect.engine()
    mins_str = p.number_to_words(mins)
    mins_str = mins_str.replace("and ", "")
    return mins_str


if __name__ == "__main__":
    main()



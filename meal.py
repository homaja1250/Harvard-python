def main():
    #Get time from user
    answer = input("What time is it? ")
    #Call the convert function
    time = convert(answer)
    #Breakfast between 7:00 and 8:00
    if time >= 7 and time <=8:
        print("breakfast time")
    #lunch between 12:00 and 13:00
    if time >= 12 and time <=13:
        print("lunch time")
    #Dinner between 18:00 and 19:00
    if time>= 18 and time <= 19:
        print("dinner time")

def convert(time):
    #Get hour and minute
    hours,minutes = time.split(":")
    #convert time into float number
    new_minute = float(minutes)/60
    #return the result to main function
    return float(hours)+new_minute
if __name__ =="__main__":
    main()



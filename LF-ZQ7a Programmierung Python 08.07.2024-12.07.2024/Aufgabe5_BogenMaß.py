import math
#take user input
def umwandeln(radian):
    # calculate the whole degree
    degrees = math.degrees(radian)
    whole_degrees = math.floor(math.degrees(radian))
    decimal_part = degrees - whole_degrees

    # calculate the minutes
    minutes = int(decimal_part * 60)
    decimal_part_minutes = decimal_part * 60 - minutes
    #calculate the seconds
    seconds = int(decimal_part_minutes * 60)
    
    return whole_degrees, minutes, seconds


radians = int(input("Enter the radians to convert to degrees: \n"))

degrees, minutes, seconds = umwandeln(radians)

print(f"{degrees}° {minutes}' {seconds}\"")




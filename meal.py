def convert(time):
    hours, minutes =time.split(':')
    return hours + minutes / 60

def main():
    time = input("Enter the time in 24-hour format (e.g., 07:30): ")
    converted_time = convert(time)

    if 6 <= converted_time < 9:
        print("It's breakfast time!")
    if 12 <= converted_time < 14:
        print("It's lunch time!")
    if 18 <= converted_time < 20:
        print("It's dinner time!")
    
if __name__ == "__main__":
    main()
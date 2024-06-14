# Function to calculate area of Rectangle or Square
def calculate_area(width, length):
    if width == length:
        return "This is a Square!"
    else:
        return width * length

# Main method is here
if __name__ == '__main__':
    try:
        # Taking user input for width and length
        width = float(input("Enter the width: "))
        length = float(input("Enter the height: "))

        # Check for negative values
        if width < 0 or length < 0:
            print("Please enter positive numbers for width and length.")
        else:
            # Calling the function to calculate area
            area = calculate_area(width, length)

            if width == length:
                print(area)
            else:
                print(f'Area of Rectangle is: {area}')
    except ValueError:
        print("Please enter valid numbers for width and length.")


# Function to calculate area of Rectangle or Square
def calculate_area(width , length):

    if width == length:


        return "This is a Square!"
    
    else:

        return width*length



#Main method is here

if __name__ =='__main__':

# Taking user input for width and length
    width=float(input("Enter the width: "))
    length=float(input("Enter the heigth: "))


# Calling the function to calculate area
    area=calculate_area(width,length)

    if width == length:

        print(area)
    else:

        print(f'Area of Rectangle is: {area}')
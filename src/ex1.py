from ValidationException import ValidationException

def validate_file(file_path):
    non_integer_mileages = []
    with open(file_path, 'r') as file:
        next(file) 
        for line in file:
            car_id, mileage = line.strip().split(',')
            try:
                mileage_float = float(mileage.strip())
                if not mileage_float.is_integer():
                    non_integer_mileages.append(mileage_float)
            except ValueError:
                print(mileage)
    return non_integer_mileages


def ex1():
    try:
        non_integer_mileages = validate_file("./files/input.txt")
        for mileage in non_integer_mileages:
            print("Invalid mileage: " + str(mileage))
    except ValidationException as ve:
        print(ve)

ex1()


"""
# 2nd method
def validate_file(file_name):
    file1 = open(file_name, 'r')
    for count, line in enumerate(file1):
    if count !=0:
        line_values = line.split(',')
    # if the second value is number -> throw exception
        try:
            int(line_values[1])
        except:
            raise validationException(f"Invalid Mileage: {line_values[1]}")
        
    file1.close()



def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)

ex1()

 """
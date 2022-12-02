# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculatebmi(weight, height):
    #weight = float(input("Enter your weight (in kg): "))
    #height = float(input("Enter your height (in cm): "))
    bmi = round(weight/(height * height),2)
    print("Your BMI is : " + str(bmi))
    if bmi <18.5 :
        #print("You are underweight")
        return -1
    elif bmi >=18.5 and bmi <=24.9:
        #print("Your weight is moderate")
        return 0
    else:
        #print("You are overweight")
        return 1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculatebmi(92, 1.81)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

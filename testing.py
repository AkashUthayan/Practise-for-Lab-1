import main as bmi


def testbmi():
    height = 1.7
    weight = 70
    result = bmi.calculatebmi(height,weight)
    assert (result == -1)



if __name__ == '__main__':
    testbmi()

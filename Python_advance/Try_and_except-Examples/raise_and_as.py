def test(inp):
    if inp == 0:
        raise NameError("QQ")
    elif inp == 1:
        raise ValueError("TAT")
    elif inp == 2:
        raise TypeError("XD")
    elif inp == 48763:
        raise Exception("Too Fast!")
    else:
        raise Exception("other")
try:
    inp = int(input("Enter a number: "))
    test(inp)
except NameError as e:
    print("NameError:", e)
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)
except Exception as e:
    print("Other Error:", e)
else:
    print("No error")
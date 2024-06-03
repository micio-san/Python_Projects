#madlibs

def checkValidity(type):
     value = input(type)
     if value=="":
        print("No empty values!")
        checkValidity(type)
     elif value.isdigit():
        print("No numeric vals!")
        checkValidity(type)
     else:
        return value


adjective= checkValidity("Adj: ")
verb= checkValidity("Verb: ");
thing= checkValidity("Thing: ")

finishedstring = f"My life is {adjective} and I {verb} my {thing}"
print(finishedstring)




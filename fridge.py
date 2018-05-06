while True:
    door = raw_input("is the door (c)losed or (o)pen ")
    if door == "o":
        time = int(raw_input("how long has the door been open "))
        if time > 180:
            for i in range(10):
                print("{} beep".format(i))
        else:
            print("dont keep me open for to long!")
    elif door == "c":
        print("so your not hungry")
    else:
        print("technical difficulties")

counter = 0
reset = 0
while True:
    if reset == 3:
        Q = (input("do you want to start again? type 'yes' or 'no' "))
        if Q == "yes":
            reset = 0
            continue
        else:
            print("have a pleasant day.")
            print("you have run the code ", counter)
            break
    else:
        BoxOrCircle = input("what is the shape? ")
        if BoxOrCircle == "e" or BoxOrCircle == "E":
            print("thanks for playing")
            print("you have played", counter, "times")
            break
        elif BoxOrCircle == "c" or BoxOrCircle == "b":
            width = int(input("enter the width: "))
            length = int(input("enter the length: "))
            height = int(input("enter the height: "))
            volume = (width * length * height)
            surface_area = (2 * (height * width)) + (2 * (height * length)) + (2 * (width * length))
            print(volume)
            print(surface_area)
            counter += 1
            reset += 1
        else:
            print("enter either 'c' or 'b': ")

mylist=["osama","ahmed","khlid"]

while True:
    print("hi my name is travis ")
    name=input("what is you name ?:")

    if name in mylist:
        print("hi {}".format(name))

        remove=input("would you like to be removed from the sysytem (y/n)?:").strip().lower()

        if remove =="y":
            mylist.remove(name)
            print("sorry to c you go")
            print(mylist)

        elif remove =="n":
            print("thank you for syting with us ")
            print(mylist)


    else:
        print("hummm id ont think i know you {}".format(name))
        addme=input("would you like to be added to the sysyme (y/n)?:").strip().lower()

        if addme =="y":
            mylist.append(name)

        elif addme =="n":
                print("ok cy later ")
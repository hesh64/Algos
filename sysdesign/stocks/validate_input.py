def validate(price):
    if len(price) == 0:
        return False

    if price[0] != '-' and price[0] != '+':
        return False

    decimal = False

    for i in range(1, len(price)):
        if price[i] == '.' and decimal == False:
            decimal = True
        elif price[i] == '.' and decimal == True:
            return False

        if '0' <= price[i] <= '9':
            continue
        elif price[i] != '.':
            return False
    return True


def main():
    input = '+40.325'
    print(validate(input))
    print("Is the price valid -1.1.1? ", validate("-1.1.1"))
    print("Is the price valid -222? ", validate("-222"))
    print("Is the price valid ++22? ", validate("++22"))
    print("Is the price valid 10.1? ", validate("10.1"))
    print("Is the price valid +22.22.? ", validate("22.22."))
    print("Is the price valid .100? ", validate(".100"))


main()

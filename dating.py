#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Nov. 5, 2022
# random number guessing game with try catch


def main():
    # variables
    good_looking = input("Are you really good looking? (y/n): ")
    rich = input("Are you rich? (y/n): ")
    is_good_looking = False
    is_rich = False
    yesNo = ["y", "Y", "n", "N"]

    # valid input is entered
    if good_looking in yesNo and rich in yesNo:
        # if user is good looking
        if good_looking == "y" or good_looking == "Y":
            is_good_looking = True

        # if user is rich
        if rich == "y" or rich == "Y":
            is_rich = True

        # checks if user can date grandchild
        if is_rich or is_good_looking:
            print("You can date our grandchild :)")

        else:
            print("YOU CANNOT DATE OUR GRANDCHILD!")

    else:
        print("Please enter either y or n.")

    print("Thank you for using this program!")


if __name__ == "__main__":
    main()

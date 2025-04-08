#
###############################################################
#  ____                           ____       __  __           #
#|  _ \ _ __ _____      _____   / ___|___  / _|/ _| ___  ___  #
#| | | | '__/ _ \ \ /\ / / __| | |   / _ \| |_| |_ / _ \/ _ \ #
#| |_| | | |  __/\ V  V /\__ \ | |__| (_) |  _|  _|  __/  __/ #
#|____/|_|  \___| \_/\_/ |___/  \____\___/|_| |_|  \___|\___| #
#                stratuslabs@outlook.com                      #
###############################################################



#importing and headder text
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Drews Coffee")
print(ascii_banner)
print ("Hi Welcome to Drews Coffee ! ")

menu = " Americano, Latte, Cappucino, Iced Frappuccino"

# Start of the coffee Shop script

name = input ("Can i take your name please \n \n")

#Adding the coffee shop bouncer, nobody allowed called Joker Penguin or Loki allowed in the shop
# First use of operators shown as "or" "and" including greater than / less than integer values #
#Nested If statements below

if name == "Joker".lower() or name == "Penguin".lower() or name == "Loki".lower():
    evil_status = input (" Are you Evil " +name + "?" + "\n")
    deeds = int(input("How many good deeds have you done today ? \n"))
    if evil_status == "yes" and deeds < 4:
        print (" You are BANNED please leave the Shop.")
        exit()
    else:
        print ( "Hi " + name + " Come on in ! \n")

#User input is not case sensitive due to the .lower()

print ( "\n Hi " + name + " Check out our Menu \n" + menu + "\n" )
selection = input ("What can i get you ? \n")

if selection.lower() == "Americano".lower():
    price = 1
elif selection.lower() == "Latte".lower():
    price = 4
elif selection.lower() == "Cappucino".lower():
    price = 3
elif selection.lower() == "Iced Frappuccino".lower():
    price = 5
else:
    selection = input ("We dont have that here sorry!, Choose off this Menu please \n" + menu + "\n")
    price = 0

amount = input( "How many " + selection + "'s would you like ? \n")
print ("Great choice! " + selection )

total = price * int(amount)

# can do it like this too and reference the absolute - absolutetotal = str(total)

everything = input ( " Brilliant! is that everything ? \n")

if everything == "yes":
    print ( "That will cost you £ " + str(total))
    exit()
else:
    selection2 = input (" What else can i get you ? \n " + menu + "\n")
    amount2 = input ("\n How many " + selection2 + "'s would like?")

#Calculation of additonal orders 

absolutesure = input ("Are you absolutely sure now ?, so it's a \n" + selection + " and a " + selection2 + " \n")

total2 = price * int(amount2) 

endtotal = int(total) + int(total2)


if absolutesure == "yes":
    print ( "That will cost you £ " + str(endtotal) + " Thank You " + name)
else:
    print (" GET OUT OF MY SHOP ")
    exit()


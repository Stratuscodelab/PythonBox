'''
:'######:::::'###::::'##::::'##:'########::'####:'##::: ##::'######:::
'##... ##:::'## ##::: ###::'###: ##.... ##:. ##:: ###:: ##:'##... ##::
 ##:::..:::'##:. ##:: ####'####: ##:::: ##:: ##:: ####: ##: ##:::..:::
 ##:::::::'##:::. ##: ## ### ##: ########::: ##:: ## ## ##: ##::'####:
 ##::::::: #########: ##. #: ##: ##.....:::: ##:: ##. ####: ##::: ##::
 ##::: ##: ##.... ##: ##:.:: ##: ##::::::::: ##:: ##:. ###: ##::: ##::
. ######:: ##:::: ##: ##:::: ##: ##::::::::'####: ##::. ##:. ######:::
:......:::..:::::..::..:::::..::..:::::::::....::..::::..:::......::::
                    stratuslabs@outlook.com
'''

import pyfiglet
  
result = pyfiglet.figlet_format("Camping", font = "banner3-D" )
print(result)

#Variable list of all camping stuff to take 

#camping_stuff = "Tent, knife, Rapberry PI, Hexi Cooker, Bag, Mobile, Portable Charger, Food, Flask, Water, Sleeping Bag"
#The list is indexed and will stay the same number so you can reference it at a later date.
#if you want to reference backwards use [-1] neat little hack
supplies = ["Tent", "knife", "Hexi Cooker", "Bag", "Mobile", "Portable Charger", "Food", "Flask", "Water", "Sleeping Bag"]

#Print the data Class 
#print(type(camping_list))

#This list shows a String, Float, Integer and a Boolean 
camp_site = [ "Crystal Lake", 23.3, 404, True ]

me = supplies[2]
print (me)

#Methods, this demonstrates methods used in Python.
#append - you can only add one item to the supplies list

#supplies.append("Toilet Paper")

#extend - you can add multiple items to your supplies list.

#supplies.extend(["Toilet paper", "Chocolate"])

#You can do the same thing with addition as we explained in the Drews Coffee Script
# supplies = supplies + [ "Toilet Paper", "Chocolate"]

#Inserting an item to a particular place within the list you can use insert

supplies.insert(-2, "Chocolate")

#####################
#Clear - if you want to clear the list you can type 
#supplies.clear() 
#This will clear the list, its used in a scenario when you want to program something and then come back to fill in a list.

#Removing an item from the list can be done 

supplies.remove("Chocolate")

#Another method called pop can be used to remove particular items, when you remove an item the index will change. 

supplies.pop(0)

#If you wanted to see what was pop'ed you can print it through terminal via the following command. 

print("This was just deleted: " + supplies.pop(0))


print (supplies)
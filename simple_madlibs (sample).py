#string concatenation practice lets put strings togther LOL
#lets make a string that says "sub to ____"

youtuber = "Pewdiepie" #some string 

#a few ways to do this
#print("sub to " + youtuber) #first way includes putting the string "sub to" then a "+" to conncatenate (add) the value of youtuber
#print("sub to {}".format(youtuber)) #puts value of youtuber into {}
#print(f"sub to {youtuber}") #this is the cleanest way to show this


adj = input("Adjective: ") #input means that when you run the code it will ask you to put a response in it
adj2 = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
madlib = f"Coding is so {adj}! It makes me feel {adj2}! It makes me super stoked because \
I love to {verb1}. Stay real like always and {verb2}!"

print(madlib)
import random
l=["r","p","s"]
while True:
	#take input from user
	u=input("enter your choice,press enter to discontinue")
	#to exit
	if u=='n':
		print("game over")
		exit()
	#input from computer
	c=random.choice(l)
	print ("computer chooses",c)

	#compare the user and the computer choice
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")

	if u==c:
		print("tie")
	elif u=="p" and c=="r":
		print("u wins")

	if u==c:
		print("tie")
	elif u=="s" and c=="r":
		print("comp wins")

	if u==c:
		print("tie")
	elif u=="r" and c=="s":
		print("u wins")

	if u==c:
		print("tie")
	elif u=="p" and c=="s":
		print("comp wins")

	if u==c:
		print("tie")
	elif u=="s" and c=="p":
		print("u wins")



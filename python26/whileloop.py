mind=50
guess=0
while guess!=mind:
	guess=int(input("guess any number  "))
	if guess==mind:
		print("wow correct")
	elif guess>mind:
		print("your enter high value")
	elif guess<mind:
		print("enter your low value")

# Created by Ibrahim Elsakka on 4/13/2017

import time

print "You start your computer and can boot into one of two options:"
print "1. Windows 7"
print "2. Ubuntu"
boot_choice = raw_input("> ")

if boot_choice == "1":
	print "You boot into Windows 7."
	print "You are now presented with a few choices:"
	print "1. Launch Steam"
	print "2. Launch Google Chrome"
	steam_or_chrome = raw_input("> ")

	if steam_or_chrome == "1":
		print "You launch Steam."
		print "You see your library of games. What are you going to play?"
		game_choice = raw_input("> ")
		print "Nice! You spend your evening playing %s" % game_choice
	elif steam_or_chrome == "2":
		print "You open Chrome."
		print "Everyone knows you can only go on YouTube or Netflix on the internet."
		print "1. Netflix"
		print "2. YouTube"
		netflix_or_youtube = raw_input("> ")
		if netflix_or_youtube == "1":
			print "You spend your evening on Netflix watching videos. Nice!"
		elif netflix_or_youtube == "2":
			print "You spend your evening on Youtube watching videos. Nice!"
		else:
			print "Someone doesn't know how to follow directions."

elif boot_choice == "2":
	print "You boot into Ubuntu."
	print "You have no games on Ubuntu so you're forced to do work."
	time.sleep(3.0)
	print "Just kidding, you still go on Netflix and spend your evening watching videos."

else:
	print "You go outside and see some sun."
	time.sleep(1.0)
	print "You get skin cancer and die."
	time.sleep(1.0)
	print "Shoulda put on sunscreen."
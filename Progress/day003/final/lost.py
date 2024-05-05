import time

print("_"*200)

print("The man get lost in space and time, in a planet that is not eart h. an uncknown planet.")
time.sleep(3)
print("He forgot his name, and all his memories. after waking up, he finds out that a weird creature was watching and waiting for him to wakeup.")
time.sleep(1)
print( "who are you? -  the man asks.")
time.sleep(2)
print("I am Opticus. i know that you have forgotten everything, including your memories. I didn’t see any brain activity in you brain after I scanned it. I’ll call you Krypton.")
time.sleep(2)
print("There are people on earth watching us, they’re gonna give us instructions of what to do to get back home. Since You’re tired, I’ll be your guide. from now on, we’ll be interacting with the humans on the other side, telling them what we have as choices:")
time.sleep(1)
print("to Humans:")
time.sleep(1)
choice = input("were inside of a cave, it is raining heavily outside, and I see a dark tunnel that we do not know where it leads us, what to do? (type o for 'outside' and t for 'tunel')").lower()
time.sleep(1)

if choice == 't':
    choice2 = input("(after being ided by a misterious light at the end of the tunel...) The light Guided us. we walked untill outside, but there are Two stones: a big one, and a small one. one of them needs to be moved so we can exit the cave. which one we move?(type s 's' for small and 'b' for big.)").lower()
    if choice2 == 's':
        time.sleep(2)
        print("After the door is open, they see a rocket, and an allert tells them: Run over, You can escape now.")
        time.sleep(2)
        print("Inside the rocket, the assistant says: Congratulations, you’ve made it. We are on our way to earth…")
        time.sleep(1)
        print("congratulations, You Won!!!")
    else:
        print("The big stone destroyed the cave with the man inside, and they died...\nYou lost...")
else:
    print("The man and the creature went outside and were struck by lightning, and died...\nYou lost...")



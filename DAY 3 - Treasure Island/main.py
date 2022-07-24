chest = """MMMMMMMMMMMMMMMMMMMMMMMMMMWx' .'xWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWXk:':oo:':kXWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMO, .o0KXKd' ,OMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWK0NMNxc',lkko,,cxXMN0KWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKo..c0WMWKc....cKWMW0c..oKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNo..:c..cKMMNxllxNMMKc..c:..oNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNk:.',.;xXMMMMMMMMMMXx;.,,.:kNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWO:,xNMMMMMMMMMMMMMMNx,:OWMMMMMMMMMMMMMMMMM
MMMMWOdoooookXNNNWWWNNNNN0xooooood0NNNNXXNNNNNKkooooodOWMMMM
MMMMO'.:ccc,..,;;ck0x:,;,..;cccc:..,;;;;;;;;;,..,cccc.'OMMMM
MMMMx.:0OkKd..:c:clolc:c;..kXXXXO,.,cc::c::cc:..oKkOK:.xMMMM
MMMMx.:0xd0d..clllllllll:..kXXXXO,.;lllllllllc..o0dx0l'kMMMM
MMMMx.:000Xd. ........... .kXXXXO, ........... .oK00X00NMMMM
MMMMx.:0xo0d..:::::::::;'..okOOOd. ';:::::::::..o0odKxoKMMMM
MMMMx.;O00Ko..cllllll:'.'.',;;;;,'''.':llllllc..l0000:.xMMMM
MMNx'..,;;;'...'''''.. ;O00OdlldO0KO: .''''''...';;;;..'xNMM
MM0'.oxxdoxdollllllll,.cKXO;.''.;OXKc.'lllllllloxxodxxo.'0MM
MM0''kK0doOkc;;;;;;,,. :KXk,.''.,kXKc .,;,,;,,,ckOod0KO,'0MM
MM0,.:lllllllcccccccc' :KXXO;. ;OXXKc.'cccccccccllllllc.,0MM
MMWO; .;:::' ......... 'xKXKkookKXKx' ......... ':::;. ;OWMM
MMMMx.:00OKo..llllllll,..,,,,,,,,,,..,llllllll..oKO00:.xMMMM
MMMM0ld0xo0d..:cccccccc:;,'''''''',:clccccccc:..o0ox0:.xMMMM
MMMMN00KKKXd. ....................,ll;........ .oKKKK:.xMMMM
MMMMk,c0xo0d..ccccccccccccccccccccloollccccccc..o0ox0:.xMMMM
MMMMx.:0K0Ko..lollooollollollllllollllollloool..oK0KK:.xMMMM
MMNk,..;:::' ..''''''''.'.''..''.'.'''''.'''... ';::;..;kNMM
MM0'.coooloollclllllllloooloolloolloolllllllllllooloool.,0MM
MM0''kK0dlOkc;;;;;;;;;:x0oo0kllk0oo0kc,,;;;;;,;ckOod0Kk,'0MM
MM0'.lddooddlcccllcllclodoodoooodooddlcclllcllllddooddl.'0MM
MMXc. .......   .....    ..  . .... ..    . ..... .... .cXMM                                                                                   
"""

print("You just landed on an island!\n")
print("You are looking for a treasure chest. You got the map from a sneaky lookin fella name Squidgy Roger.\nCan you find it and not perish?\n")
step_1 = input("You disembarked your ship and is now on a beach with your crew. What do you do? \n1) Go into the deep part of the island? \n2) Go around the coast? \n3) Go up the cliff you see there?\n->")
step_1.strip()
if step_1 == "1":
    step_2 = input("You got deep into the tropical woods. You hear a noise. Do you investigate?\n1) Yes 2) No\n")
    step_2.strip()
    if step_2 == "1":
        step_3 = input("It seems like someone is already diggin up!!! \nThe Squidgy Roger sold the map to multiple people! Quick, what do you do?\n1) Do nothing?\n2) Prepare to fight and launch a suprise attack?\n3) Announce yourself and confront them?\n->")
        step_3.strip()
        if step_3 == "1":
            print("Really? Well, you did nothing. They got away with the treasure. -_-\n When you come back to your ship you are faced with mutiny because you have no money and is killed\n")
        elif step_3 == "2":
            print("You order your men to sneak around.\nAfter everyone is in place you aim your pistol and shoot at someone looking the toughest.\nThe fight started!\n")
            print("It was tough. But you won!!!All you crew are now dead, but so is the enemy. No idea who is gonna carry the treasure chest tho.")
            print(chest)
        elif step_3 == "3":
            step_4 = input("They got really suprised for a second, but then quickly regained composure and prepared for a fight'\nThey are not losing all those golden dublons\nWhat do you do? 1) Retreat for now to think up a plan? 2) Attack?\n->")
            step_4.strip()
            if step_4 == "1":
                step_5 = input("You step back and run away.\nThey laugh at your crew running and get back to digging.\nIt seems like you ran not into the direction of your ship and ended up on the other side of the island.\n"
                               "But what is that? Is that a ship?!\nIt seems to be theirs."
                               "\nWhat do you do? \n1) Sneak onto the ship and prepare an ambush\n2) Stay outside and attack them on their return\nThey are gonna be immobile because of the heavy treasure and tired, right?")
                step_5.strip()
                if step_5 == "1":
                    print("There was just one guard and you quickly dispose of him and get into the ship\nAfter half an hour you hear footsteps and laughter\nThe other crew is here\nRight when they were getting onto the deck, unsuspecting you attacked\n"
                          "You overpowered a suprised enemy and got the treasure! And a cool new ship, that you don't know what to do with, as a boonus! ")
                    print(chest)
                elif step_5 == "2":
                    print("They, obviously, saw you. Dropped the treasure and faced your attack.\n...\nSeems like you are not the smartest captain\nYou perished.\n")
            elif step_4 == "2":
                print("There were more of them and they had to time to prepare. Your crew were wiped out.\nYou got captured and will probably be sold to slavery or your family will have to pay ransom to get you out.\n")
    elif step_2 == "2":
        print("You diverted from the noise and searched around without finding anything\nYou got to that part of the island way later\nTo you dismay you found a dugout - smbd got the treasure.\nWhen you come back to your ship you are faced with mutiny because you have no money and is killed\n")
elif step_1 == "2":
    print("You just wasted time on the beach. Good job -_-\nTreasure was found by someone else!")
elif step_1 == "3":
    print("You ended up on top of the cliff. Exhausted. But hey, at least you got a good workout and\n...You got a great view of an unfamiliar crew boarding their ship with what seemed to be an exact treasure chest you were looking for\nYour crew notices that too.\nYou are kicked off the cliff shortly after.")

print("THE END")
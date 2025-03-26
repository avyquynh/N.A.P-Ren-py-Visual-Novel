# The script of the game goes in this file.
default sai_meet1 = 0 
default aled_meet1 = 0 
default xela_meet1 = 0
default maria_meet1 = 0
default andres_meet1 = 0

default chosen_menu_choices = []
default chosen_menu_choices1 = []
default clue_pathway = 0
default dining_clue = 0 
default maria_clue = 0
default memory_clue = 0

default question_continue = 0
default question_continue1 = 0

default photo1_unlocked = 0

image photo1 = "images/inv/inv_photo_1.png"
label photo1:
    window hide
    show photo1
    pause
    return
image inv_photo1 = "images/inv/inventory_photo1.png"
label inv_photo1:
    window hide
    show inv_photo1
    pause
    return
image inv_popup1 = "images/popup/popup1.png"
label inv_popup1:
    window hide
    show inv_popup1
    pause
    return

label start:

    scene black screen with fade
    user "..."
    scene path day with fade
    scene black screen with fade
    scene path day

    user "What the..."
    user "Where am I?" 

    show maria smiling
    with moveinleft
    maria "Hey there!"
    user "Oh, hi?"
    show maria talking 
    maria "The name's Maria! What's yours?"
    show maria neutral 
    jump day1
    
    return

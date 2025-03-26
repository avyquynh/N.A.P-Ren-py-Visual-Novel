
label day2:
    scene black screen with fade
    scene yncabin day with fade
    yn "Damn I'm exhausted."
    yn "I wonder what's on today's agenda."
    menu choice_5:
        "Meet Up With the Others":
            jump meetup_1
label meetup_1:
    scene bonfire day with fade
    show maria talking at left 
    show zichen neutral at right
    maria "Hey [name]! You're up early!"
    show maria neutral
    yn "Yeah, gotta get exploring..."
    show maria talking
    maria "We'll be here if you need anything, right Zichen?"
    show maria neutral
    show zichen thinking
    zi "I got no where else to be."
    show zichen neutral
    show maria talking
    maria "So where are you headed to first?"
    show maria neutral
    menu choice_6:
        "Sai's Cabin":
            $ sai_meet1 = sai_meet1 + 1
            jump sai1
        "Xela's Cabin" if xela_meet1 > 0:
            jump xela1
        "Stay and Chat":
            $ maria_meet1 = maria_meet1 + 1
            jump maria1
label sai1:
    scene saicabin with fade
    show sai neutral
    yn "Morning Sai, can we talk?"
    show sai wink 
    sai "Of course! What's up?"
    yn "I just want to get a feel of the situation."
    show sai talking
    sai "Well go on n' shoot!"
    show sai neutral
    menu sai_questions2:
        set chosen_menu_choices1
        "Do you remember anything from your first day?":
            $ question_continue1 = question_continue1 + 1
            $ dining_clue = dining_clue + 1
            show sai thinking
            sai "Not at all, it's been a long while now."
            show shand
            sai "I remember being really afraid at first but I'm not sure why."
            show sai talking
            sai "It's great here! I mean just check the commisary!" 
            show sai neutral 
            hide shand
            jump sai_questions2
        "What do you know about the boundary?":
            $ question_continue1 = question_continue1 + 1
            $ andres_meet1 = andres_meet1 + 1
            show sai thinking
            sai "I actually don't know much about it."
            show sai talking
            sai "You'd have to ask Andres." 
            show sai neutral
            yn "Who?"
            show sai thinking
            sai "Oh you haven't met him yet! He's a unique one."
            show sai talking
            sai "I'd ask Maria where to find him, she seems to know everything haha!"
            show sai neutral
            jump sai_questions2
        "{color=#b80909}I think I know everything I need to know for now.{/color}" if question_continue1 >= 1:
            jump continue2
label continue2: 
    show sai talking
    sai "Well where are you headed next?"
    show sai neutral
    menu explore_2:
        "Go to the Commisary" if dining_clue == 1:
            jump location1
        "Find Andres" if andres_meet1 >= 1:
            jump location2
        "Find Maria and Zichen":
            jump location3
label location1:
    $ clue_pathway = clue_pathway + 1
    $ dining_clue = dining_clue + 1
    scene dining day with fade
    yn "I wonder why Sai said this place was so great..."
    yn "Well either way I'm starving."
    if xela_meet1 == 0:
        show xela talking
        user "Someone's a hungry hippo."
        show xela neutral
        yn "Hey, not cool man."
        show xela talking
        user "Haha, my bad."
        show xela neutral
        yn "Who are you anyways?"
        show xela thinking
        show xhand
        xela "Oh right, we haven't met, the name is Xela."
        xela "I'm the fifth resident."
        hide xhand
        show xela neutral
        yn "Nice to meet you, I'm [name]."
        show xela talking
        xela "Oh I know, talk of the town you are."
        show xela neutral
        yn "What?"
        show xela talking
        xela "I'm only joking, seven of us does not make a town."
        show xela neutral
        yn "Wait seven."
    else:
        show xela talking
        with hpunch
        xela "Me too man."
        show xela neutral
        yn "Shoot! Do you ever not try to scare people?"
        show xela talking
        xela "Nah it's in my blood."
        show xela neutral
        yn "Terrible excuse."
        show xela thinking
        show xhand
        xela "It's not actually on purpose. All I do is wander around with my notebook."
        hide xhand
        xela "It's not exactly my fault you six scare easily."
        show xela neutral
        yn "Wait, six."
        yn "Xela there's seven of us here."
    show xela thinking
    xela "Uh yeah. What, did you forget how to count?"
    show xela neutral
    yn "No, Xela this is the eighth day of camp."
    show xela thinking
    xela "..."
    xela "Oh shit..."
    show xela neutral
    yn "So there's probably someone new already."
    show xela thinking
    xela "Nah no way. I would've sensed their vibes."
    show xela neutral
    yn "Are you being serious? I can never tell."
    show xela thinking
    xela "I'm kidding. But if they already arrived they're probably with Maria right now."
    show xela neutral
    yn "What? Why? Is Maria the informant for newbies?"
    show xela thinking
    xela "No, she's the first resident."
    $ memory_clue = memory_clue + 1
    show xela neutral
    yn "First? Are you sure?"
    show xela thinking
    xela "... I am not..."
    show xela neutral
    yn "I thought Sai was."
    show xela thinking
    xela "I thought Maria was."
    show xela neutral
    yn "..."
    xela "..."
    yn "Could one of them just have gotten mixed up?"
    show xela talking
    xela "Probably, we're all losing our minds out here."
    show xela neutral

label location2:
    scene ynpath day
    yn "Sai said Maria knew everything, but I don't want to bother her just yet."
    yn "At the very least Andres has got to be near the cabins."
    show aled neutral
    with moveinleft
    show aled talking
    if aled_meet1 == 0:
        $ aled_meet1 = aled_meet1 + 1
        user "Hey, you must be the new face I've heard about."
        show aled neutral
        yn "Yeah, are you Andres?"
        show aled thinking
        aled "Andres? No, the name is Aled. Nice to meet you."
        show aled talking
        aled "Looks like you haven't been around much if you haven't met me or Andres yet."
        show aled neutral
        yn "Unfortunately..."
        show aled talking
        aled "Why are you looking for him anyways?"
        show aled neutral
        yn "Sai told me to meet him to learn more about this place."
        show aled thinking
        aled "Oh so you met Sai already."
        aled "Seems I can look forward to whatever you discover Sherlock."
        show aled neutral
        yn "Sherlock?"
        show aled talking
        aled "Oh my bad, do you prefer Detective Conan? Nancy Drew? Any member of Mystery Inc.?"
        show aled neutral
        yn "No, you just caught me off guard. Also the name is [name]."
        show aled thinking
        aled "Good to know."
        show aled neutral
        yn "Anyways, do you know where I can find Andres?"
    else:
        show aled talking
        aled "Looks like you're already out and about."
        show aled neutral
        yn "Hey Aled!"
        yn "Yeah, I'm looking for someone named Andres."
        show aled talking
        aled "Ah out and about being a detective huh?"
        show aled neutral
        yn "Something like that, do you know where I can find him?"
    show aled thinking
    aled "Oh, Andres is probably somewhere near the bonfire."
    show aled talking
    aled "That boy loves his pictures."
    show aled neutral
    yn "Pictures?"
    show aled thinking
    aled "Yeah, it seems he was a photographer before all this."
    aled "At the very least, he had his camera with him before he got here."
    show aled neutral
    yn "Sounds like his memory is pretty in-tact."
    show aled talking
    aled "Maybe, I mean I think we all remember our passions."
    show aled neutral
    yn "Wait our passions?"
    show aled talking
    aled "Well not exactly passions, but everyone seems to remember something from before we arrived here."
    show aled neutral
    if aled_meet1 > 0: 
        yn "I see you've also done some detective work."
        show aled talking
        aled "Yeah, I ran into Andres last night near my cabin."
        aled "He was just looking through his camera lens, he wasn't taking any pictures though."
        show aled neutral
    yn "I see... thanks Aled."
    show aled talking
    aled "Of course, I'll be off then. Good luck with Andres."
    aled "He can get immersed in his own world quite a bit."
    show aled neutral
    hide aled neutral 
    with moveoutleft
    yn "Looks like the bonfire is my next destination."
    scene black screen
    scene bonfire day
    with fade

    $ andres_meet1 = andres_meet1 + 1
    show andres thinking
    user "Hm..."
    yn "Hey! Are you Andres?"
    user "..."
    yn "Hello?"
    user "..."
    yn "HELLOOO!!!"
    show andres talking
    with hpunch
    user "Huh!"
    user "Oh, sorry were you talking to me?"
    show andres neutral
    yn "Yeah, you're Andres right?"
    show andres talking
    andres "Yes, that's me, who are you?"
    show andres neutral
    yn "Oh my name is [name], the latest resident."
    show andres talking
    andres "So you're the seventh. Looks like the eighth will probably show up later today then."
    andres "Why were you looking for me?"
    show andres neutral
    yn "Sai. She said you could help me out."
    show andres thinking
    andres "Uh, I don't know what she told you but I doubt I can help you."
    andres "For one, I hardly talk to the others."
    show andres neutral
    yn "Oh yeah, Aled mentioned something about you being a photographer?"
    show andres talking
    andres "Hm, yeah it seems I was."
    andres "Enough about my un-remembered past though, why did Sai think I could help you?"
    show andres neutral
    yn "She said you'd know more about the boundary surrounding this place."
    show andres talking
    andres "The boundary..."
    andres "Okay I'm starting to get why she sent you to me."
    andres "Here, take a look at this."
    show andres neutral
    
    call photo1
    hide photo1
    $ photo1_unlocked = photo1_unlocked + 1

    yn "What's this?"
    show andres talking
    andres "A photo?"
    show andres neutral
    yn "That's not what I meant."
    yn "It's just a picture of the forest floor."
    show andres talking
    andres "It's a picture of the boundary."
    andres "You can see a line that divides the campsite and the forest beyond it."
    show andres thinking
    andres "I've poking around and looking for things I can take pictures of for evidence."
    show andres talking
    andres "Sadly, I have a limited amount of camera film, so I've taken very few photos."
    show andres neutral
    yn "How much film do you have left?"
    show andres thinking
    andres "Mmm, just enough for ten pictures."
    show andres neutral
    yn "We should help each other out."
    show andres talking
    andres "How so?"
    show andres neutral
    yn "I'm collecting information about this place, and you're taking pictures right?"
    show andres thinking
    andres "Yeah. So what, you want to share information with me so I share my pictures with you?"
    show andres neutral
    yn "Exactly. It'd be a good way for us to get to the bottom of this situation."
    yn "Also it lets us retain our memories."
    show andres talking
    andres "Alright, I get it. You can take that photo then."
    andres "As a sign of our partnership."
    call inv_popup1
    hide inv_popup1
    andres "Meet me here in the future if you need me."
    show andres neutral
    yn "Perfect."
    hide andres neutral 
    with moveoutleft
    yn "(Where to next?)"
    jump explore_2
label location3: 
    scene cabin day
    show maria neutral at left
    show zichen neutral at right
    maria "Hey Welcome back!"

label bedroom1:
    scene yncabin night
    menu inventory_check:
        "Look in Inventory":
            show inventory_screen
            if photo1_unlocked == 1:
                call inv_photo1
                hide inv_photo1
                hide inventory_screen
            jump inventory_check
        "Go to Bed":
            yn "Time to hit the hay."
            jump day3







return

label day1:
    $ name = renpy.input("Enter Name:\n", length=10)
    $ name = name.strip()

    yn "My name is [name]."
    
    menu choice_1:
        "I'm not sure what's going on...":
            show maria thinking
            maria "Mmm, so you don't know either."
            yn "Either?"
            maria "It's okay."
            jump continue_1
        "Do you know where we are Maria?":
            $ clue_pathway = clue_pathway + 1
            show maria talking
            maria "Not at all, we all showed up one-by-one."
            yn "What? All?"
            show maria thinking
            maria "We're not sure why we all ended up here."
            show maria neutral
            yn "So you dont know what this place is?"
            jump continue_1
label continue_1:
    show maria talking 
    show mhand
    maria "None of us really know, we just call it \"The Camp\"."

    yn "\"None of you know\"? So how many of us are there?"
    hide mhand
    show maria neutral at left

    show zichen thinking at right
    with moveinright
    zi "Hm... maybe around seven so far? Including you of course."
    yn "What the? Who are you?"
    show zichen neutral 
    zi "Zichen, third resident of The Camp."
    yn "Right, nice to meet you."

    show maria talking 
    show mhand at left
    maria "We should talk more in our cabin."
    maria "It's getting late!"
    hide mhand
    show maria neutral

    show zichen thinking
    zi "Maria's right. Follow us, uhh..."
    yn "It's [name]."
    show zichen talking
    zi "Alright. I'll lead the way."
    show zichen neutral 

    scene cabin day 
    with fade

    show zichen talking
    zi "As you can see, the cabins are all relatively close together."
    zi "There's probably only a few meters in-between each."
    zi "So if you need anything, the rest of us can help."
    show zichen neutral
    yn "Sounds good."
    show zichen thinking 
    zi "This is basically what all the cabins look like. One bunk and a shelf."
    zi "Me and Maria will show you yours tonight."

    show zichen neutral
    yn "Oh wait speaking of Maria, where is sh-"
    show zichen neutral at right
    show maria smiling at left
    with moveinleft
    with hpunch
    maria "Hey!"
    show maria neutral
    yn "Woah!"
    show maria talking
    maria "Sorry!!! I had to check in with the others."
    show mhand at left
    maria "Y'know, let them know about the newest arrival!"
    maria "We'll introduce you at the bonfire tonight!"
    show maria neutral 
    hide mhand

    show zichen talking at right
    zi "It would serve you well to get to know them."
    zi "Even if they're a little strange."
    show zichen neutral 
    show maria talking
    maria "It'll be tons of fun! We'll lead the way for you don't worry."
    show maria neutral
    yn "Thanks..."
    show maria thinking 
    maria "What's wrong?"
    show maria neutral
    yn "Nothing, just a little unnerved. I'm not sure how you both are so calm."
    yn "How long have you guys been here? At this camp I mean."
    show maria thinking
    maria "..."
    maria "Hard to say really. I'm not sure..."
    show maria neutral
    zi "..."
    show zichen talking 
    zi "Well save your questions for the rest of the group tonight."
    show zichen thinking
    zi "Not that you'll get much clarity or any answers"
    zi "After all, we're in the same boat here."
    show maria smiling
    maria "We should head out soon, I'll lead the way!"
    show zichen neutral 
    show maria neutral
    
    scene bonfire night
    with fade

    show zichen neutral at right
    show maria smiling at left
    
    maria "Welcome to the bonfire!" 
    maria "It was pretty hard to find don't you think?"
    show maria neutral
    menu sarcasm1:
        "It was right infront of the cabins...":
            show maria thinking
            maria "Awh man, you're no fun [name]"
            show maria neutral
            jump sai_sector1
        "Super hard to find, impossible even.":
            $ maria_clue = maria_clue + 1
            show maria smiling
            maria "Haha! Thanks [name], you're a fun one."
            show maria thinking
            maria "Be careful when you come here alone."
            maria "It'd be bad if you got hurt."
            show maria neutral
            yn "(?)"
            jump sai_sector1         
label sai_sector1:
    show zichen talking
    zi "Hm, Let's introduce you to the others [name]"
    show zichen thinking
    show maria talking
    maria "We should approach Sai first, she might be able to help you."
    show maria neutral
    zi "Right, she's been here the longest."
    show zichen neutral
    yn "Yeah, I'm down for that."
    show maria smiling
    maria "She over by her cabin, follow us!"

    hide maria neutral
    with moveoutleft
    hide zichen neutral 
    with moveoutleft

    if maria_clue > 0:
        yn "(What was that all about?)"

    scene path night
    with fade

    show maria neutral at left
    show zichen neutral
    show sai neutral at right

    yn "You guys are quick."
    show maria smiling
    maria "Yeah, come meet Sai!"
    show maria neutral
    show zichen talking
    zi "We'll let you guys talk, me and Maria are heading back to our cabin."
    show zichen neutral
    hide maria neutral
    with moveoutleft
    hide zichen neutral
    with moveoutleft
    scene path night
    show sai talking 

    sai "Hey there! So you're [name]?"
    show sai neutral
    yn "Yeahh, nice to meet you, Sai right?"

    show sai wink
    sai "You got it [name]!"

    show sai talking
    sai "Those two are awfully close, I wonder if this is a summer camp romance~"
    show sai neutral

    yn "Who? Maria and Zichen?"
    show sai talking
    show shand
    sai "Who else! Those lovebirds are always with each other."
    sai "Anyways!"
    hide shand
    sai "If you have any questions [name] just ask me."
    sai "I am the first resident after all!"

    show sai neutral

    menu sai_questions:
        set chosen_menu_choices
        "Has anyone tried leaving?":
            $ question_continue = question_continue + 1
            show sai thinking
            sai "No, there's a boundary that prevents us from doing that."
            yn "A physical boundary? Cuz I don't see one."
            show shand
            sai "Not sure..."
            hide shand
            show sai talking
            sai "I wouldn't want to leave even if I could though..."
            show sai neutral
            yn "..."
            jump sai_questions
        "How long have you been here?":
            $ question_continue = question_continue + 1
            show sai thinking
            sai "About eight days."
            show sai neutral
            yn "(So she knows how long)"
            jump sai_questions
        "Is there anything you can tell me about the situation?":
            $ question_continue = question_continue + 1
            $ memory_clue = memory_clue + 1
            show sai thinking
            sai "Mmm, it's pretty peaceful."
            show sai talking 
            sai "Honestly, I don't wanna go back to wherever I came from."
            show sai neutral
            yn "\"Wherever\" you came from?"
            show sai talking
            sai "Huh?"
            show sai neutral
            yn "(Does she not remember?)"
            jump sai_questions
        "{color=#b80909}I think I know everything I need to know for now.{/color}" if question_continue >= 1:
            jump no_questions
label no_questions: 
    show sai talking
    sai "Hope I could help you out [name]!"
    show sai wink
    sai "Well, if you ever need me, I'll be in my cabin, it's by the bonfire."
    show shand
    sai "You can't miss it!"
    hide shand

    yn "Alright thanks Sai."

    show sai talking
    sai "You know it [name]! See ya!"

    hide sai neutral 
    with moveoutright
    yn "..."    
    yn "I'm exhausted, I should find Maria."

    scene cabin night
    with fade
    show maria smiling
    maria "Hey [name]! How was Sai?"
    yn "She seems a little..."
    yn "Nevermind, she seemed cool."
    maria "Ready to go to your cabin?"
    show maria neutral
   

    menu choice_2:
        set chosen_menu_choices
        "I'm ready to go.":
            show maria neutral
            jump return_choice_2
        "I'm going to go explore real quick":
            show maria talking
            maria "Alright, just return to my cabin when you're done!"
            jump explore_1
label explore_1:
    hide maria talking
    yn "(Where should I go first?)"
    menu explore1:
        "The Bonfire":
            jump bonfire_1
        "(Mmmm, I changed my mind.)":
            jump return_choice_2
label bonfire_1:
    scene bonfire night
    $ aled_meet1 = aled_meet1 + 1
    yn "(There's six others total, I've met three, so three to go.)"
    yn "... I wonder where everyone could be..."
    yn "Oh, hey, someone's over there."
    yn "Hey!"
    show aled neutral 
    with moveinright
    show aled talking
    user "My, hello there, you're a fresh face around here huh."
    show aled neutral
    yn "Yeah, how about you?"
    show aled talking
    aled "I'm Aled, the sixth resident"
    alec "Since you're the newest, I showed up right before you."
    show aled neutral
    yn "The name's [name]."
    yn "So I'm guessing you don't know much either then..."
    show aled thinking
    aled "No, I haven't gathered much sadly."
    show aled talking
    aled "Try asking Xela though, she got here before me."
    show aled neutral
    yn "Who?"
    show aled talking
    aled "Dark clothes, looks goth, emo, stuff along that vein."
    aled "She's around the area, you just have to look."
    aled "She's also a tad elusive."
    show aled neutral
    yn "What do you mean?"
    show aled thinking
    aled "You're going to have to experience her presence yourself..."
    show aled talking
    aled "I won't be sticking around for it, it's quite late."
    aled "I'll see you around new kid!"
    show aled neutral
    
    hide aled neutral
    with moveoutleft

    $ xela_meet1 = xela_meet1 + 1
    yn "..."
    yn "Where am I going to find \"Xela\"?"
    show xela neutral
    with hpunch
    show xela talking
    user "Yo, you lookin' for me?"
    show xela neutral
    yn "WTF!"
    show xela talking
    show xhand
    user "LOL, my bad dude."
    show xela neutral
    yn "Right... well nice to meet you, the name's [name]."
    show xela talking
    xela "Mmm... well as you already know, I'm Xela."
    xela "Fifth resident."
    show xela neutral
    hide xhand
    yn "Nice to meet you, I need to know more about this place, can you help?"
    if memory_clue > 0:
        yn "This place is messing with everyone's heads."
        show xela talking
        xela "Yeah, mine too..." 
        show xela neutral
    yn "Aled told me to fnd you, he didn't have much information himself..."
    show xela talking
    xela "Oh, well this tid-bit I know might be useful to you then."
    show xela neutral
    yn "What?"
    show xela talking
    xela "Everyone at camp showed up here with everything they had on them."
    show xela neutral
    yn "Meaning...?"
    show xela talking
    xela "We may not have our phones, or memories, BUT, everything else we were carrying the day we were taken came with us."
    xela "When I showed up here I had a journal with me."
    show xela thinking
    xela "I was probably in school or something before I was basically kidnapped" 
    xela "Y'know, if you pay enough attention, you'll see things that can lead you to the truth."
    show xela neutral
    yn "What?"
    if memory_clue > 0:
        show xela thinking
        xela "What? Are you losing your memory already lol."
        show xela neutral
        yn "No you're just being cryptic..."
        show xela thinking
    xela "Just stay observant or you'll end up like Sai."
    xela "She's almost a lost cause."
    show xela neutral
    yn "Lost cause?"
    show xela talking
    xela "She can't remember anything. Luckily I've been jotting my memories down in my notebook."
    show xela thinking
    show xhand
    xela "But I'm sure I'll eventually lose all my memories too..."
    hide xhand
    show xela talking
    xela "Anyways, I'm going to bed, find me tomorrow if you need to."
    yn "Alright, I will." 
    hide xela talking with moveoutright
    yn "..."
    yn "I should find Maria if I want to get to my cabin."
    
    menu choice_3:
        "Go to Maria's Cabin":
            scene cabin night with fade
            jump return_choice_2 

    return
label return_choice_2:
    scene cabin night
    show maria smiling
    maria "Alright! Let's get going!"
    scene ynpath night with fade
    show maria smiling
    maria "So this is where you'll be staying."
    maria "Sai is nearby so if you need anything, just walk down the path to her cabin."
    show maria talking
    maria "I'll be going, see you tomorrow morning [name]!"
    hide maria talking with moveoutleft
    menu choice_4:
        "Go Inside":
            scene yncabin night
            jump bedroom
label bedroom:
    yn "I can finally relax."
    yn "Time for bed..."
    scene black screen
    jump day2  
return
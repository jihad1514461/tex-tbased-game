import random
def riddles():
    l=[
    ['Voiceless it cries, wingless flutters, toothless bites, mouthless mutters. What is it?', 'The wind',"jihad","jihad"],
    ["\n I am often in the air, but never take flight,\n I can be a source of warmth, or a reason for fright.\n Some say I am a blessing, others call me a curse,\n What am I that can be both tame and fierce?","Fire","jihad"],
    ['What starts with an E, ends with an E, but only contains one letter?', 'An envelope',"jihad","jihad"],
    ['What has four legs in the morning, two legs in the afternoon, and three legs in the evening?', 'A human being (crawls on all fours as a baby, walks on two legs as an adult, and uses a cane in old age)',"jihad","jihad"],
    ['What has a face and hands but no arms or legs?', 'A clock',"jihad","jihad"],
    ['What is black when you buy it, red when you use it, and gray when you throw it away?', 'Charcoal',"jihad","jihad"],
    ['What can you catch but not throw?', 'A cold',"jihad","jihad"],
    ["What has a heart that doesn't beat, a mouth that doesn't eat, and a brain that doesn't think?", 'A jar',"jihad","jihad"],
    ['I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?', 'A pencil lead',"jihad","jihad"],
    ['What is as big as an elephant, but weighs nothing?', 'Its shadow',"jihad","jihad"],
    ["\n I am always in front of you, but never behind,\n I can be a friend or foe, but never unkind.\n I am as bright as the sun, but never in the sky,\n What am I that can always catch your eye?","Reflection","jihad"],
    ["I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but I need water to survive. What am I?", 'A tree',"jihad","jihad"],
    ["What has a heart that doesn't beat, a mouth that doesn't speak, and can make even the bravest man weak?", 'Fear',"jihad","jihad"],
    ["I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", 'Fire',"jihad","jihad"],
    ['What can you see in the dark, but disappears in the light?', 'Shadows',"jihad","jihad"],
    ['What has a head and a tail, but no body?', 'A coin',"jihad","jihad"],
    ['What is as light as a feather, but even the strongest man cannot hold it for long?', 'Breath',"jihad","jihad"],
    ['What has a bed but never sleeps, a mouth but never eats, and runs but never walks?', 'A river',"jihad","jihad"],
    ['What has a tongue but cannot speak, eyes but cannot see, and a soul but cannot die?', 'A shoe',"jihad","jihad"],
    ['I am always in front of you, but can never be seen. What am I?', 'The future',"jihad","jihad"],
    ["\n I am small and round, but can be as heavy as lead,\n I can be a source of comfort, or a cause for dread.\n Some say I am a symbol of love, others see me as a curse,\n What am I that can be both good and worse?","Heart","jihad"],
    ['I am not alive, but I can die if I fall in the water. What am I?', 'A leaf',"jihad","jihad"],
    ['I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?', 'Fire',"jihad","jihad"],
    ["I have a heart that doesn't beat, an eye that doesn't see, and a mouth that doesn't speak. What am I?", 'A skull',"jihad","jihad"],
    ["What is it that when you see it, you feel like screaming, but it's not alive?", 'A ghost',"jihad","jihad"],
    ['What can run but never walks, has a mouth but never talks, has a bed but never sleeps, and has a head but never weeps?', 'A river',"jihad","jihad"],
    ["What is always in front of you but can't be seen?", 'The future',"jihad","jihad"],
    ['What has a face and two hands, but no arms or legs?', 'A clock',"jihad","jihad"],
    ['What has a neck but no head, two arms but no hands?', 'A shirt',"jihad","jihad"],
    ['What has a mouth, but cannot eat; moves, but has no legs; and has a bank, but cannot put money in it?', 'A river',"jihad","jihad"],
    ['What goes through cities and fields, but never moves?', 'A road',"jihad","jihad"],
    ["What has a heart that doesn't beat?", 'An artichoke',"jihad","jihad"],
    ['The more you take, the more you leave behind. What am I?', 'Footsteps',"jihad","jihad"],
    ['I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost every human being. What am I?', 'A pencil lea',"jihad","jihad"],
    ['It belongs to you, but other people use it more than you do. What is it?', 'Your name',"jihad","jihad"],
    ['What is it that no man ever saw, which never was, but always will be?', 'Tomorrow',"jihad","jihad"],
    ['What can you break, even if you never pick it up or touch it?', 'A promise',"jihad","jihad"],
    ["I am an escape from reality,\n A place where you can be free.\n You can fly or you can swim,\n Do impossible things on a whim.\n Sometimes I'm good, sometimes I'm bad,\n I can leave you happy or feeling sad.\n I'm something you can't touch or hold,\n But in your mind, I can unfold.\n What am I that comes when you sleep,\n A world of wonder, yours to keep?","a dream","jihad"],
    ["\n I am always around, but never seen or heard,\n In the light I am invisible, in the darkness I am blurred.\n I am not alive, but without me you can't live,\n What am I that is always there to give?","Air","jihad"],
    ["\n I am made of water, but if you touch me I will die,\n I can be a source of joy, or a reason to cry.\n Some say I am a treasure, others think I'm just a whim,\n What am I that's so ephemeral and dim?","Bubble","jihad"],
    ["\n I am not alive, yet I can die,\n I can be strong or gentle, but never lie.\n Some say I am a mystery, others find me plain,\n What am I that can bring joy or pain?","Wind","jihad"],
    ["\n I am always busy, but never seem to tire,\n I am often in a hurry, but I never perspire.\n I can take you places, but never leave the ground,\n What am I that can always be found?","Imagination","jihad"],
    ["\n I am something that's full, yet can never overflow,\n I am like a river, but without the flow.\n Some say I am a gift, others see me as a curse,\n What am I that can be both better and worse?","Memory","jihad"],
    ["\n I am small and fragile, but can be very strong,\n I am often in a group, but sometimes I don't belong.\n Some say I am a joy, others call me a pain,\n What am I that can be both sunshine and rain?","Flower","jihad"],
    ["\n I am always moving, but never seem to go far,\n I am often in a hurry, but I never leave a scar.\n I can be a source of light, or a reason for fear,\n What am I that can be both far and near?","Shadow","jihad"],
    ["I am a window to the world, but without any glass,\n I can take you to distant lands, and bring you back in a flash.\n I am often found in books, but never on a shelf,\n What am I that can be both an adventure and a delve?","Imagination","jihad"]
    ]
    #print(len(l))
    c=0
    d=9
    f=0
    for i in range(5):
        a = random.randint(c,d)
        c = d
        d += 9
        b=l[a]
        print(b[0])
        input_str =" ".join( input("answer: ").split()).lower().replace(".", "")
        
        if input_str in b[1].lower() or input_str in b[2].lower():
            print("right answer")
            f+=1
        else:
            print("wrong answer")
    return f
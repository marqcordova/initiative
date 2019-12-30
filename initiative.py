from tkinter import * 
import pprint
import random
master = Tk() 

length= 10

#dictionary for holding all important varaibles
d={}
for x in range(0,length):
        d["combatant{0}".format(x)]={"Name": "",
                                      "Bonus": 0,
                                      "Initiative": 0,
                                      "Range_d4": 0,
                                      "Cantrip_d6": 0,                                      
                                      "Finesse_d6": 0,                                     
                                      "Melee_d8": 0,
                                      "Move_d6": 0,
                                      "Spell_d10": 0,
                                      "Other_d6": 0}

order = ["","Name","Bonus","Move_d6","Range_d4","Finesse_d6","Cantrip_d6","Melee_d8","Spell_d10","Other_d6","Adv--None--Dis"]

def copy_box():        
    master.clipboard_clear()
    master.clipboard_append(textbox.get(1.0,'end'))
    print(textbox.get(1.0,'end'))

def Roll():
    textbox.delete(1.0,END)
    for i in range(0,length):
        d['combatant'+str(i)]['Name'] = names[i].get()
        if bonus[i].get().strip().isnumeric():
            d['combatant'+str(i)]['Bonus'] = round((int(bonus[i].get().strip())/2)+0.1) #add 0.1 so rounding is reliable
        d['combatant'+str(i)]['Melee_d8'] = melees_d8[i].get()
        d['combatant'+str(i)]['Move_d6'] = move_d6[i].get()
        d['combatant'+str(i)]['Range_d4'] = range_d4[i].get()
        d['combatant'+str(i)]['Finesse_d6'] = finesse_d6[i].get()
        d['combatant'+str(i)]['Spell_d10'] = spell_d10[i].get()
        d['combatant'+str(i)]['Cantrip_d6'] = cantrip_d6[i].get()
        d['combatant'+str(i)]['Other_d6'] = other_d6[i].get()
        d['combatant'+str(i)]['Advantage'] = advantage[i].get()
    #pprint.pprint(d)
    output = []   
    for i in range(0,length):
        
        keys = ['Range_d4', 'Cantrip_d6', 'Finesse_d6','Melee_d8', 'Move_d6','Spell_d10','Other_d6']
        if sum([d['combatant'+str(i)].get(key) for key in keys]) > 0:
            name = (d['combatant'+str(i)]["Name"])
            dice =[]
            actions = []
            if d['combatant'+str(i)]['Range_d4'] == 1:
                dice.append(4)
                actions.append('Range_d4')
            if d['combatant'+str(i)]['Cantrip_d6'] == 1:
                dice.append(6) 
                actions.append('Cantrip_d6')
            if d['combatant'+str(i)]['Finesse_d6'] == 1:
                dice.append(6) 
                actions.append('Finesse_d6')
            if d['combatant'+str(i)]['Melee_d8'] == 1:
                dice.append(8) 
                actions.append('Melee_d8')
            if d['combatant'+str(i)]['Move_d6'] == 1:
                dice.append(6) 
                actions.append('Move_d6')
            if d['combatant'+str(i)]['Spell_d10'] == 1:
                dice.append(10) 
                actions.append('Spell_d10')
            if d['combatant'+str(i)]['Other_d6'] == 1:
                dice.append(6) 
                actions.append('Other_d6')
            #print((name,dice))
            if d['combatant'+str(i)]['Advantage'] == '':
                rolls = []
                for die in dice:
                    rolls.append(random.randint(1,die))
                roll = sum(rolls) - d['combatant'+str(i)]['Bonus']
                output.append((name,dice,roll, actions))
            if d['combatant'+str(i)]['Advantage'] == 'Adv':
                rolls1 = []
                rolls2 = []
                for die in dice:
                    rolls1.append(random.randint(1,die))
                    rolls2.append(random.randint(1,die))
                roll = min(sum(rolls1), sum(rolls2)) -d['combatant'+str(i)]['Bonus']   
                output.append((name,dice,roll,actions))
            if d['combatant'+str(i)]['Advantage'] == 'Dis':
                rolls1 = []
                rolls2 = []
                for die in dice:
                    rolls1.append(random.randint(1,die))
                    rolls2.append(random.randint(1,die))
                roll = max(sum(rolls1), sum(rolls2))-d['combatant'+str(i)]['Bonus']           
                output.append((name,dice,roll,actions))                   
                
    output.sort(key = lambda x: x[2])
    textbox.insert('end', 'Name'.ljust(12)+ 'Roll'.ljust(6) + 'Action\n')
    for character in output:
        textbox.insert('end', character[0].ljust(12)+ str(character[2]).ljust(6) + str(character[3])+'\n')


#Make and place labels
for i in range(0,length):
    l1 = Label(master, text = "Combatant " + str(i) +":").grid(row = i+1, column = 0, sticky = W) 

#make and place entry boxes
names = []

for i in range(0,length):
    en = Entry(master)
    en.grid(row=i+1, column=order.index("Name"))
    names.append(en)    

#make and place entry boxes
bonus = []

for i in range(0,length):
    en = Entry(master,width=5)
    en.grid(row=i+1, column=order.index("Bonus"))
    bonus.append(en)   

#Checkboxes for d8 range
range_d4 = []

for i in range(0,length):
    range_d4.append(IntVar())
    l = Checkbutton(master, text="", variable=range_d4[i])
    l.grid(row=i+1, column=order.index("Range_d4"), sticky = E)   

#Checkboxes for d8 melee
melees_d8 = []

for i in range(0,length):
    melees_d8.append(IntVar())
    l = Checkbutton(master, text="", variable=melees_d8[i])
    l.grid(row=i+1, column= order.index("Melee_d8"), sticky = E)   

#Checkboxes for d8 melee
finesse_d6 = []

for i in range(0,length):
    finesse_d6.append(IntVar())
    l = Checkbutton(master, text="", variable=finesse_d6[i])
    l.grid(row=i+1, column=order.index("Finesse_d6"), sticky = E)       

#Checkboxes for d6 move
move_d6 = []

for i in range(0,length):
    move_d6.append(IntVar())
    l = Checkbutton(master, text="", variable=move_d6[i])
    l.grid(row=i+1, column= order.index("Move_d6"), sticky = E)   
    
cantrip_d6 = []

for i in range(0,length):
    cantrip_d6.append(IntVar())
    l = Checkbutton(master, text="", variable=cantrip_d6[i])
    l.grid(row=i+1, column= order.index("Cantrip_d6"), sticky = E)   

spell_d10 = []

for i in range(0,length):
    spell_d10.append(IntVar())
    l = Checkbutton(master, text="", variable=spell_d10[i])
    l.grid(row=i+1, column= order.index("Spell_d10"), sticky = E)   
    
other_d6 = []

for i in range(0,length):
    other_d6.append(IntVar())
    l = Checkbutton(master, text="", variable=other_d6[i])
    l.grid(row=i+1, column= order.index("Other_d6"), sticky = E)   
  
#Labels

for i in range(1,len(order)):
    w = Label(master, text=order[i])
    w.grid(row=0, column=i, sticky = E)  

#Advantage and Disadvantage, col = 
    
advantage = []
for i in range(0,length):    
    advantage.append(StringVar())
    
    adv = Radiobutton(master, text='Adv', variable=advantage[i])
    adv.config(indicatoron=0, bd=4, width=5, value="Adv")
    adv.grid(row=i+1, column=order.index("Adv--None--Dis"),
             sticky = E)
    
    no_adv = Radiobutton(master, text='no_adv', variable=advantage[i])
    no_adv.config(indicatoron=0, bd=4, width=7, value="", state = "active")
    no_adv.grid(row=i+1, column=order.index("Adv--None--Dis")+1,
                sticky = E)
    
    dis = Radiobutton(master, text='Dis', variable=advantage[i])
    dis.config(indicatoron=0, bd=4, width=5, value="Dis")
    dis.grid(row=i+1, column=order.index("Adv--None--Dis")+2,
             sticky = E)

button=Button(master,text="Roll Initiative",command = Roll).grid(row=length+2,column=0)

button2=Button(master,text="Copy",command = copy_box).grid(row=length+2,column=2)

textbox = Text(master, height=length+1, width=80)
textbox.grid(row=length+3,column=0,columnspan=10, sticky = NSEW)

mainloop()

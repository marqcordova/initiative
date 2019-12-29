from tkinter import * 
import pprint

master = Tk() 

#dictionary for holding all important varaibles
d={}
for x in range(0,10):
        d["combatant{0}".format(x)]={"Name": "",
                                      "Range_d4": 0,
                                      "Cantrip_d6": 0,                                      
                                      "Melee_d8": 0,
                                      "Move_d6": 0,
                                      "Spell_d10": 0}

#Make and place labels
for i in range(0,10):
    l1 = Label(master, text = "Combatant " + str(i) +":").grid(row = i+1, column = 0, sticky = W) 

#make and place entry boxes
entries = []

for i in range(0,10):
    en = Entry(master)
    en.grid(row=i+1, column=1)
    entries.append(en)    

#Checkboxes for d8 range
range_d4 = []

for i in range(0,10):
    range_d4.append(IntVar())
    l = Checkbutton(master, text="Range_d4", variable=range_d4[i])
    l.grid(row=i+1, column=4, sticky = E)   

#Checkboxes for d8 melee
melees_d8 = []

for i in range(0,10):
    melees_d8.append(IntVar())
    l = Checkbutton(master, text="Melee_d8", variable=melees_d8[i])
    l.grid(row=i+1, column=5, sticky = E)   
    
#Checkboxes for d6 move
move_d6 = []

for i in range(0,10):
    move_d6.append(IntVar())
    l = Checkbutton(master, text="Move_d6", variable=move_d6[i])
    l.grid(row=i+1, column=3, sticky = E)   
    
cantrip_d6 = []

for i in range(0,10):
    cantrip_d6.append(IntVar())
    l = Checkbutton(master, text="Cantrip_d6", variable=cantrip_d6[i])
    l.grid(row=i+1, column=6, sticky = E)   

spell_d10 = []

for i in range(0,10):
    spell_d10.append(IntVar())
    l = Checkbutton(master, text="Spell_d10", variable=spell_d10[i])
    l.grid(row=i+1, column=7, sticky = E)   
    
def Roll():
    for i in range(0,10):
        d['combatant'+str(i)]['Name'] = entries[i].get()
        d['combatant'+str(i)]['Melee_d8'] = melees_d8[i].get()
        d['combatant'+str(i)]['Move_d6'] = move_d6[i].get()
        d['combatant'+str(i)]['Range_d4'] = range_d4[i].get()
        d['combatant'+str(i)]['Spell_d10'] = spell_d10[i].get()
        d['combatant'+str(i)]['Cantrip_d6'] = cantrip_d6[i].get()

button=Button(master,text="Roll Initiative",command=Roll).grid(row=13,column=0)

mainloop()

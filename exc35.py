from sys import exit

#fungsi gold_room > fungsi finalnya neh
def gold_room():
    print "this room is full of gold. How much do you take ?"\
    #baca inputan lalu di save di next ??
    #lah bukannya next itu fungsi, cek diconsole python
    #katanya begini >>
    #"Return the next item from the iterator. If default is given and the iterator
    #is exhausted, it is returned instead of raising StopIteration"

    #jadi mah intinya mengembalikan sebuah nilai dari sebuah pengulanagan
    next = raw_input("> ")
    #sumpah python bahasa yang rada2 menurut gw ada kata in coba
    #knp harus 0 dan 1 ?? ada yang tau ?
    if "0" in next or "1" in next:
        #ubah input string jadi integer
        how_much = int(next)
    else:
        dead("man, learn to type a number")

    if how_much < 50:
        print "Nice, you are not greedy, you win!"
        #exit(0) adalah cara keluar yang baik
        #exit(1) adalah cara keluar yang buruk itu mengindikasikan erorr
        #exit(2) juga keluar yang mengandung error
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room():
    print "There is a bear here."
    print "the bear has a bunch of honey"
    print "the fat bear is in front of another door"
    print "how are you going to move the bear?"
    #inisiasi awal variabel, kasih tau kalo beruangnya blm gerak
    bear_moved = False

    #while true artinya  selama benar -_-
    #artinya selama programnya masih jalan, jalankan hal2 dibawahnya
    #infinite loop
    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("the bear looks at you then slaps your face off.")
        #taunt artinya mengalihkan bukan ?
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            #ubah nilai di variablenya jadi true
            bear_moved = True
        #dalam pilihan ini ingat ya bear_moved nya masih bernilai false
        elif next == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off")
        #pilihan ini variable bear_moved udah berubah jadi True
        elif next == "open door" and bear_moved:
            #go to gold_room function
            gold_room()
        else:
            print "i got no idea what that means."
        pass

def hugayaw_room():
    print "here you see the great evil hugayaw"
    print "he, it whatever you call it. Stares at you and you go insane."
    print "Do you flee for your life or eat you head"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        hugayaw_room()

#fungsi dead mempunyai argumen "why", itu adalah input
#jadi apa aja yang ada dalam kurung fungsi dead
#akan di gabungin dengan kata Good Job
def dead(why):
    print why," Good job!"
    exit(0)

#start function ! fungsi ini engga memberikan data apapun def start()
#segalanya bermula dari sini
    print "you are in a dark room"
    print "there is a door to your right and left"
    print "which one do you take?"
    # next adalah fungsi utk input setelah ??
    next = raw_input("> ")

    if next == "left":
        #kalo user masukin input left dia ke fungsi bear_room
        #cari fungsi bear_room !
        bear_room()
    elif next == "right":
        #user masukin input right masuk ke hugayaw_room
        #cari fungsi hugayaw_room
        hugayaw_room()
    else:
        #jika ga milih dari kedua pilihan diatas, kamu ke fungsi dead
        #cari fungsi dead
        dead("you stumble around the room until you starve")

## ini adalah programnya dijalakan, dimulai dari fungsi start
## bacalah dari fungsi start
### main  program ####
start()

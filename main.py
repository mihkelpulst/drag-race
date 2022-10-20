#from car import Car
#from track import Track
import time
from race import Race

#car1 = Car(66)
#car2 = Car(88)
#car3 = Car(54)

#print("Võistlevad auto: " + str(car1.number) + "," + str(car2.number) + " ja " + str(car3.number))
#print(car1.currentSpeed())
#print(car2.currentSpeed())
#print(car3.currentSpeed())

#Lets generate car tracks
#track1 =  Track(10, car1.number)
#track2 =  Track(10, car2.number)
#track3 =  Track(10, car3.number)


#print (track1.createTrack())
#print (track2.createTrack())
#print (track3.createTrack())


#Nimekiri autode numbritest
carNumbers = [22, 33, 44, 55, 88, 10]


#Määrame võidusõisust osavõtvad autod ja sõidu pikkuse.
race = Race(carNumbers, 100)

#Loome võidusõidu, ehk paneme autod rajale
race.createRace()

m = 5
race.callStart(m)

while True:
    for track in race.moveCar():
        for i in track:
            print(i, end="")
        print()
    print("\033["+str(len(carNumbers)+1)+"A")#Viib kursori tagasi autode arvu võrra +1, võimalik, et ei tööta Windowsis.
    if race.isFinished() == True:
        break
    time.sleep(0.03337)
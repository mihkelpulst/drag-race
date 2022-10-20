import time
from car import Car
from track import Track

class Race:
    def __init__(
        self,
        carNumbers:list,
        trackLength:int
        ):
        self.carNumbers = carNumbers
        self.trackLength = trackLength
        self.tracks = []
        self.cars = []

    def createRace(self):
        for i in self.carNumbers:
            self.cars.append(Car(i)) #Loome auto objektid ja lisame massiivi
            self.tracks.append(Track(self.trackLength, i).createTrack()) #Loome rajad ja paneme autod rajale
        
        #print(self.cars,"\n",self.tracks)


    def moveCar(self):
        i=0
        for track in self.tracks:
            carPos = track.index(self.carNumbers[i])
            carSpeed = self.cars[i].currentSpeed()
            track.insert(carPos + carSpeed, self.cars[i].number)
            track.pop(carPos)
            i+=1
        return self.tracks

    def isFinished(self):
        i=0
        for track in self.tracks:
            if track[self.trackLength-1] == self.cars[i].number:
                for m in range(len(self.tracks)):
                    print()
                print("\nCar " + str(self.cars[i].number) + " wins!")
                return True
            i+=1
        return False
    
    def callStart(self, m):
        self.m = m
        for i in range(self.m+1):
            if self.m > 0:
                print("Race Start in " + str(self.m), end="\r")
            else:
                print("GO             ", end="\r\n")
            self.m-=1
            time.sleep(1)
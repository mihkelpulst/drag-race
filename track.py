class Track:
    def __init__(
        self,
        length:int, # Track length
        car:int #Get car
        ):
        self.length = length
        self.car = car

    #Create track and put the car on the track.
    def createTrack(self):

        track = ["_"]*self.length
        track[0] = self.car
        track[self.length-1] = "|"

        return track
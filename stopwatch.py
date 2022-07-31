from calendar import c


class Chronometer:
    time = 0
    
    def __init__(self) -> None:
        pass
        
c1 = Chronometer()
c2 = Chronometer()

c1.time = 10
c2.time = 200

print(Chronometer.time)
print(c1.time)
print(c2.time)
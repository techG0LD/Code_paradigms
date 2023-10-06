class Pod_Racer:
    def __init__(self, max_speed, condition, price,owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner

    def repair(self):
        self.condition = 'repaired'


class Anakin_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price,owner = 'Anakikn'):
        super().__init__( max_speed, condition, price,owner)

    def boost(self):
        self.max_speed *= 2



class Sebulba_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price,owner = 'Sebulba'):
        super().__init__( max_speed, condition, price,owner)

    def flame_jet(self, other_pod):
        other_pod.condition = 'trashed'




anakins_pod = Anakin_Pod(28, 'perfect', 1000) 

sebulba_pod = Sebulba_Pod(50, 'perfect', 1000000)

print('anakin condition:',anakins_pod.condition)
print('sebulba condition:',sebulba_pod.condition)

sebulba_pod.flame_jet(anakins_pod)

print('anakin condition:',anakins_pod.condition)
print('sebulba condition:',sebulba_pod.condition)

anakins_pod.repair()

print('anakin condition:',anakins_pod.condition)
print('sebulba condition:',sebulba_pod.condition)



print('anakin max speed:',anakins_pod.max_speed)
print('sebulba max speed:',sebulba_pod.max_speed)

anakins_pod.boost()

print('anakin max speed:',anakins_pod.max_speed)
print('sebulba max speed:',sebulba_pod.max_speed)

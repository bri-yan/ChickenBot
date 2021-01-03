from classes.ability import Ability
import library.effects as effects

# Normal Abilities
peck = Ability("Peck", "normal", 40, 100)
zzz = Ability("Zzz", "normal", 0, 60, effects.sleep)

# Fire Abilities
flare = Ability("Flare", "fire", 40, 100)
ignite = Ability("Ignite", "fire", 0, 70, effects.burn)


# Ice Abilities
chill = Ability("Chill", "ice", 40, 100)
frost = Ability("Frost ", "ice", 0, 75, effects.frozen)

# Air Abilities
puff = Ability("Puff", "air", 40, 100) # change air to wind?
whirlwind = Ability("Whirlwind", "air", 0, 70, effects.confusion)

# Earth Abilities
earthquake = Ability("Earthquake", "earth", 100, 70)
tremor = Ability("Tremor", "earth", 0, 75, effects.confusion)


# Electric Abilities
shock = Ability("Shock", "electric", 40, 100)
stun = Ability("Stun", "electric", 0, 75, effects.paralyze)

# Water Abilities
splash = Ability("Splash", "water", 40, 100) # can add wet as a status effect (lowers accuracy)





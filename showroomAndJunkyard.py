showroom = set()
showroom = {"Jaguar E-Type", "Aston Martin DB5", "Lamborghini Miura", "Ferrari 250 California Spyder"}

print(len(showroom))

showroom.add("Jaguar E-Type")

print(showroom)

showroom.update(("A-Team Van", "Shelby Cobra GT500"))

showroom.discard(("A-Team Van"))

junkyard = set()
junkyard = {"Jaguar E-Type", "The General Lee", "Edsel", "Delorean DMC", "Lamborghini Miura"}

intersected_set = showroom.intersection(junkyard)

joined_showroom = showroom.union(junkyard)

joined_showroom.discard("The General Lee")
joined_showroom.discard("Edsel")


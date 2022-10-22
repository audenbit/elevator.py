# by fiad muntakim
import random, time

user_floor_level = int(
    input("What floor level are you on? (Floor levels go from 0-18) -> ")
)
wanted_floor_level = int(input("What floor level do you want to go to? -> "))
print()

if user_floor_level == wanted_floor_level:
    print(f"Oh, silly! You are already on floor {wanted_floor_level}!")

elev_a = random.randint(0, 18)
elev_b = random.randint(0, 18)
elev_chooser = random.randint(1, 2)


def user_floor_transport():
    print(f"Going to floor {wanted_floor_level}...")
    time.sleep(abs(wanted_floor_level - user_floor_level) / 2)
    print(f"Arrived at floor {wanted_floor_level}!")


if (user_floor_level == elev_a) and (user_floor_level == elev_b):
    print("...")
    print(
        f"It looks like both elevators A and B are on your floor, floor {user_floor_level}! Choosing one of the elevators randomly..."
    )

    if elev_chooser == 1:
        elev_chooser = "A"

    else:
        elev_chooser = "B"

    time.sleep(0.5)
    print(f"It looks like elevator {elev_chooser} was chosen!")

    user_floor_transport()

if (user_floor_level == elev_a) and not (user_floor_level == elev_b):
    print("...")
    print(f"It looks like elevator A is on your floor, floor {user_floor_level}!")
    user_floor_transport()

if not (user_floor_level == elev_a) and (user_floor_level == elev_b):
    print("...")
    print(f"It looks like elevator B is on your floor, floor {user_floor_level}!")
    user_floor_transport()


if (abs(elev_a - user_floor_level)) > (abs(elev_b - user_floor_level)):
    print("...")
    time.sleep(abs(elev_a - user_floor_level) / 2)
    print("Elevator A arrived!")
    user_floor_transport()

if (abs(elev_a - user_floor_level)) < (abs(elev_b - user_floor_level)):
    print("...")
    time.sleep(abs(elev_b - user_floor_level) / 2)
    print("Elevator B arrived!")
    user_floor_transport()

elif (abs(elev_a - user_floor_level)) == (abs(elev_b - user_floor_level)):
    print("...")
    print(f"Choosing one of the elevators randomly...")

    if elev_chooser == 1:
        time.sleep(abs(elev_a - user_floor_level) / 2)
        print("Elevator A arrived!")
        user_floor_transport()

    else:
        time.sleep(abs(elev_a - user_floor_level) / 2)
        print("Elevator A arrived!")
        user_floor_transport()

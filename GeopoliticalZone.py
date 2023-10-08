from enum import Enum


class GeopoliticalZone(Enum):
    NORTH_WEST = "Sokoto", "Kebbi", "Zamfara", "Katsina", "Kaduna", "Kano", "Jigawa"
    NORTH_EAST = "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"
    NORTH_CENTRAL = "Benue", "Kogi", "Kwara", "Nassarawa", "Niger", "Plateau", "FCT"
    SOUTH_EAST = "Abia", "Anambra", "Ebonyi", "Enugu", "Imo"
    SOUTH_WEST = "Ondo", "Osun", "Oyo", "Ekiti", "Lagos", "Ogun"
    SOUTH_SOUTH = "Akwa Ibom", "Bayelsa", "Cross River", "Edo", "Delta"


def Geopolitical():
    try:
        state = input("Enter your state : ")
        if state.isdigit():
            Geopolitical()
        elif state.capitalize() in GeopoliticalZone.SOUTH_WEST.value:
            print("SOUTH WEST")
        elif state.capitalize() in GeopoliticalZone.SOUTH_SOUTH.value:
            print("SOUTH SOUTH")
        elif state.capitalize() in GeopoliticalZone.SOUTH_EAST.value:
            print("SOUTH EAST")
        elif state.capitalize() in GeopoliticalZone.NORTH_EAST.value:
            print("NORTH EAST")
        elif state.capitalize() in GeopoliticalZone.NORTH_CENTRAL.value:
            print("NORTH CENTRAL")
        elif state.capitalize() in GeopoliticalZone.NORTH_WEST.value:
            print("NORTH WEST")
        else:
            Geopolitical()
    except ValueError:
        print("input valid state : ")
        Geopolitical()


if __name__ == '__main__':
    Geopolitical()

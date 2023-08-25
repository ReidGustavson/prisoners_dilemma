import random
import math
from Models import Crime
from .RoleGenerator import RoleGenerator

class CrimeGenerator:
    crime_names = ["Heist", "Kidnapping", "Assassination", "Hit", "GTA", "Smuggling", "Dealing", "No Permit"]
    
    @classmethod
    def new_crime(cls, lvl, roleTypes):
        name = random.choice(CrimeGenerator.crime_names)
        ev = 20 * (math.pow(5, lvl))
        roles = (RoleGenerator.new_role(lvl, roleType, ev) for roleType in roleTypes)
        return Crime(lvl, name, roles)

'''
Package Sorting Script
Author: Caroline O'Neill
Date: 07/28/25
Description:
    This script defines a function to sort packages intended for use in
    Thoughtful’s robotic automation factory. It sorts into 3 categories
    based on 2 criteria
    
    CRITERIA
        BULKY: if its volume (Width x Height x Length) is greater
            than or equal to 1,000,000 cm³ or when one of its dimensions
            is greater or equal to 150 cm.
        HEAVY: A package is heavy when its mass is greater or equal to 20 kg.
    
    CATEGORIES:
        STANDARD: NOT heavy AND NOT bulky
        SPECIAL: heavy XOR bulky
        REJECTED: heavy AND bulky
        
    
Disclosure: I used OpenAI’s ChatGPT to assist with structuring, documenting,
and reviewing parts of this script. All logic, testing, and final
implementation decisions are my own.
'''
from enum import Enum

class PackageCategory(Enum):
    STANDARD = 1
    SPECIAL = 2
    REJECTED = 3
    
SPECIAL_DIMENSION = 150 # cm
SPECIAL_VOLUME = 1000000 # cm^3
SPECIAL_MASS = 20 # kg


def sort(width: int, height: int, length: int, mass: int) -> PackageCategory:
    '''
    units are centimeters for the dimensions and kilogram for the mass

    '''
    heavy = False
    bulky = False
    
    # special dimension or special volume
    bulky = (
        width >= SPECIAL_DIMENSION or
        height >= SPECIAL_DIMENSION or
        length >= SPECIAL_DIMENSION or
        (width * height * length) >= SPECIAL_VOLUME
    )
    
    # special mass
    if mass >= SPECIAL_MASS:
        heavy = True
        
    if heavy and bulky:
        return PackageCategory.REJECTED
    elif heavy or bulky:
        return PackageCategory.SPECIAL
    else:
        return PackageCategory.STANDARD



# ----------------- Test Code -----------------

if __name__ == "__main__":
    
    input_packages = [
        (2, 2, 2, 15),			# vol 8, mass 15 -- standard
        (1, 2, 3, 25),			# vol 6, mass 25 -- special heavy
        (1, 2, 3, 20),			# vol 6, mass 20 -- special heavy
        (100, 100, 100, 5),		# vol 1000000, mass 19 -- special bulky tot volume
        (1, 1, 150, 5),			# vol 1000000, mass 19 -- special bulky dimension
        (1, 151, 1, 22),		# vol 151, mass 22 -- rejected
        (100, 120, 100, 22),	# vol 1200000, mass 22 -- rejected
    ]

    for p in input_packages:
        category = sort(*p)
        print(f"Dimensions: {p[:3]}, Mass: {p[3]}, Category: {category.name}")

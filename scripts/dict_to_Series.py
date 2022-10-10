from envtest import dict_to_Series
import pandas as pd 

new_dict = {
    "Pikachu": "Electric",
    "Charizard": "Fire",
    "Blastoise": "Water"
}

new_Series = dict_to_Series(new_dict)

print(new_Series)
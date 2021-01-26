import sys

sys.path.append(".")
from nuclear import Nuclear

president_jon = Nuclear('President Jon')
secratary_rick = Nuclear('Secratery Rick')

president_jon.set_code('missle code',2)
president_jon.set_code('radar code',4)
president_jon.set_code('ignition code',7)
print('President Jon is responsible for the codes:')
president_jon.print_codes()

print('\n')
print("Secratery Rick is repsonible for the codes:")
secratary_rick.set_code('nuclear arming code',1)
secratary_rick.print_codes()


speaker_of_house = Nuclear('Speaker Salmon')
print('\n')

print("To - String method for President Jon")
print("President Jon is responsible for the codes:")
print(str(president_jon))

print('\n')
print('Child Instances')
print(president_jon._ids)
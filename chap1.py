import math as m
"""
angle1 = float(input())
angle2 = float(input())
print(180.0-angle1-angle2)
"""
"""
cote1 = float(input())
cote2 = float(input())
print(m.sqrt(cote1**2 + cote2**2))
"""
"""
Celcius = float(input())
print(1.8*Celcius + 32)
"""
"""
Fahrenheit = float(input())
print((Fahrenheit-32)/1.8)
"""
"""
rayon = float(input())
print((rayon**2)*m.pi)
"""

secondes = int(input())
heure = secondes // 3600
minute = (secondes - (heure * 3600)) // 60
seconde = secondes - (heure * 3600) - (minute * 60)
print("%d:%2d:%0d" % (heure, minute, seconde))

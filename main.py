def TakingSouls(miles,souls):
  if miles > 6:
    print("Miles run " + str(miles) + ", souls taken " + str(souls) + ".")
  else:
    print("Stay Hard, keep running")
    TakingSouls(miles+1,souls+1)

TakingSouls(3,0)
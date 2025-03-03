import random
fb_gol = random.randint(0,5)
gs_gol = random.randint(0,5)

if fb_gol > gs_gol:
  print("FB" , fb_gol , "golle kazanmıştır.")
  
elif fb_gol == gs_gol:
  print("maç berabere.")
  
else:
  print("GS" , gs_gol , "golle kazanmıştır.")	
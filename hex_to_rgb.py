def hex_to_rgb(hex):
  
  print(tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))


hex_to_rgb("FFA501")
hex_to_rgb('FFFFFF')
hex_to_rgb('FF0000')
hex_to_rgb('000080')
hex_to_rgb('C0C0C0')
import gcodepy.src.gcodepy.gcode as gc

g = gc.Gcode(port = '')  

g.home()
g.zero_extruder()
g.set_bed_temp(90)
g.draw(delta = (5, 4, 4), e = 0)
g.draw(delta = (5, 4, 4), e = 0)

a = 1
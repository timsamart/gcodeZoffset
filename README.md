# gcodeZoffset
offsets the z coordinate in 3dprinter gcode. because of first layer issue in cura. Finally you can adjust the first layer offset!

in cura set the first layer height to 0.3mm. (0.3mm - 0.3mm = 0mm offset) which means the nozzle will have exactly 0.1mm offset from the glass plate.

just call:

python transformgcodez.py -f PATHTOYOURGCODEFILE

M28 mycodes.gcode; begin logging
M17; motors on
G28 F4000; home XYZ at a rate of 4000mm/sec
G90; absolute mode
M83; set the extruder to relative mode

M92 E4209; sets extruder to steps per mL for a D=22mm syringe

G1 E-5 F5; withdraw 5 ml at 5 ml/min (testing)
G4 S10; do nothing for 10 seconds

G1 X80 Y210 F4000; send plate to loading position at 4000 mm/sec
G4 S10; do nothing for 10 seconds

G1 Z120 F4000; move the nozzle to 120mm above plate at 4000 mm/sec
G4 S10; do nothing for 10 seconds


;G1 E40 F2; start infusion: 40ml at 2 ml/min 

;TODO: turn heater on here

;TODO: stage movements here

M18; motors off
M29; end logging


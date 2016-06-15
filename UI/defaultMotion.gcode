M28 mycodes.gcode; begin logging

;program the syringe pump driver registers:
;1: CTRL Register
;2: TORQUE Register
;3: OFF Register
;4: BLANK Register
;5: DECAY Register
;6: STALL Register
;7: DRIVE Register
M911.2 S R1 V3616 ; disable now
M911.2 S R2 V440
M911.2 S R3 V50
M911.2 S R4 V256
M911.2 S R5 V1296
M911.2 S R6 V2592
M911.2 S R7 V0
M911.2 S R1 V3617 ; enable now
; for 1/16 stepping: 0E21,01B8,0032,0100,0510,0A02,0000

M17; motors on
G28 F4000; home XYZ at a rate of 4000mm/sec
G90; absolute mode
;M83; set the extruder to relative mode

M92 E4209; sets extruder to steps per mL for a D=22mm syringe

;G1 E-5 F5; withdraw 5 ml at 5 ml/min (testing)
G4 S10; do nothing for 10 seconds

G1 X80 Y210 F4000; send plate to loading position at 4000 mm/sec
G4 S10; do nothing for 10 seconds

G1 Z120 F4000; move the nozzle to 120mm above plate at 4000 mm/sec
G4 S10; do nothing for 10 seconds

M190 S100; set bed temperature to 100 deg c and then wait for it

;G1 E40 F2; start infusion: 40ml at 2 ml/min
;M1910.2 E40.0 F0.04167; start infusion: 40ml at 2.5 ml/m
M1910.2 E5.0 F0.0833; start infusion: 5ml at 5 ml/m (=5/60)
;M1910.2 E5.0 F1.0; start infusion: 5ml at 1 ml/s

G4 S70; do nothing for 70 seconds (testing)
;stage movements now
G1 Y10 F200 ;move y to 10 at 200 mm/sec
G1 Y200 ;move y to 200 (at 200 mm/sec)
G1 Y10
G1 Y200
G1 Y10
G1 Y200
G1 Y10
G1 Y200
G1 Y10
G1 Y200
G1 Y10
G1 Y200
G1 Y10
G1 Y200
G1 Y10
G1 Y200

M1910.1 E0; stop infusion

M1910.2 E-5.0 F1.0; withdraw: 5ml at 1 ml/s

G4 S6; do nothing for 6 seconds (testing)

M140 S0; set the bed temperature to 0 deg C

M18; motors off
M29; end logging

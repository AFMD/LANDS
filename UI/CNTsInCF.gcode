



M999; enable all the things (in case the halt button was pressed)

;program the syringe pump driver registers:
;1: CTRL Register
;2: TORQUE Register
;3: OFF Register
;4: BLANK Register
;5: DECAY Register
;6: STALL Register
;7: DRIVE Register
M911.2 S R1 V3616 ; disable now (1/16 microstepping)
;M911.2 S R1 V3600 ; disable now (1/4 microstepping)
M911.2 S R2 V440
M911.2 S R3 V50
M911.2 S R4 V256
M911.2 S R5 V1296
M911.2 S R6 V2592
M911.2 S R7 V0
M911.2 S R1 V3617 ; enable now (1/16 microstepping)
;M911.2 S R1 V3601 ; enable now (1/4 microstepping)
; for 1/16 stepping: 0E21,01B8,0032,0100,0510,0A02,0000
; for 1/4 stepping: 0E11,01B8,0032,0100,0510,0A02,0000

M17; motors on
G28 F6000; home XYZ at a rate of 100mm/sec
G90; absolute mode

; hamilton gastight 1025 inner diameter = 23.0mm = 2.3cm
; syringe pump lead screw = 2mm/rotation = 0.2cm/rotation
; stepper motor = 200 steps/rotation
; driver board microstepping = 1/16 steps/pulse
; then steps per mL for a D23mm syringe = 1/(pi*(2.3/2)^2)*1/0.2*200*16 = 3851 pulses/mL
; then steps per mL for a D22mm syringe = 1/(pi*(2.2/2)^2)*1/0.2*200*16 = 4209 pulses/mL

;M92 E3851; sets extruder pulses per mL for a D=23mm syringe (hamilton gastight 1025)
M92 E1917; sets extruder pulses per mL for a D=32.6mm syringe (hamilton gastight 1050 aka 85020)
;M92 E3650; sets extruder pulses per mL for the free plastic syringes

G1 X80 Y210 F12000; send plate to loading position at 200 mm/sec
;G1 X10 Y210 F12000; send plate to safe nozzle position at 200 mm/sec

;G1 Z90 F6000; move the nozzle to XXmm above plate at 100 mm/sec
G1 Z40 F6000; move the nozzle to spray height at 100 mm/sec
;G1 Z45 F6000; markus trial height <-- gave a pretty great looking film
;TODO this needs calibration 62 is actually 72mm above plate

M190 S100; set bed temperature to 100 deg c and then wait for it

G4 S30; do nothing for 30 seconds (allow thermal)

;M1910.2 E4 F0.0666; start infusion: 4ml at 4 ml/m (4/60=0.0666666667)
;M1910.2 E40 F0.0333; start infusion: 40ml at 2 ml/m (2/60=0.03333333333)
;M1910.2 E40 F0.0167; start infusion: 40ml at 1 ml/m (1/60=0.0166666667)
M1910.2 E80 F0.06666; start infusion: 80ml at 4 ml/m (4/60=0.0666666667)



M28 mycodes.gcode; begin logging
;stage movements now





G1 X51 Y200 ; lap number 6 ends
G1 X10 Y210 ; send plate to safe nozzle position
M26;
M29; end logging
; select the file:
M23 mycodes.gcode





;G1 X80 Y100; send plate to roughgly the middle (testing)
;G4 S70; do nothing for 70 seconds (testing)

  M1910.1 E0; stop infusion
;M1910.2 E80 F0.06666; start infusion: 80ml at 4 ml/m (4/60=0.0666666667)

G1 X10 Y10 F6000; send plate to safe position at 100 mm/sec

;M1910.2 E-40.0 F1.0; withdraw: 40ml at 1 ml/s
:M1910.1 E0; stop infusion

;G4 S55; do nothing for 55 seconds (testing)
;M1910.1 E0; stop infusion

M140 S0; set the bed temperature to 0 deg C

M18; motors off
M112; disable all the things



M29; end logging



;select the file:
;M23 mycodes.gcode

;run it:
;M24

;M1910.2 E80 F0.06666; start infusion: 80ml at 4 ml/m (4/60=0.0666666667)
;M1910.1 E0; stop infusion

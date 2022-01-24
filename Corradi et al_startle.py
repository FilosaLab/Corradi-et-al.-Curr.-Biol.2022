### The code was written by Alessandro Filosa, and it can be used freely for non-commercial purposes.
### Please, cite our paper (Corradi et al. Current Biology, 2022) if you use this code for a publication.


from psychopy import sound, core
from psychopy.hardware import labjacks
from psychopy.hardware.labjacks import u3
import numpy as np
import time
import datetime as dt
from datetime import timedelta

d = u3.U3()

DAC0_REGISTER = 5000
DAC1_REGISTER = 5002
start_time=time.time()

FIO6_DIR_REGISTER = 6106
FIO6_STATE_REGISTER = 6006

d.writeRegister(FIO6_DIR_REGISTER, 0)  # Set FIO6 to digital input
trigsig = d.readRegister(FIO6_STATE_REGISTER)  # Read the state of FIO6

##d.writeRegister(FIO6_STATE_REGISTER, 0) # Set FIO6 low, Stim on

# Sound stimulus parameters

sound = sound.Sound(900, octave=3, sampleRate=44100, secs=0.003, bits=8)
sound.setVolume(1.0)

timeme=(time.time()-start_time)

# Sound stimulus starts

##core.wait(timeme+1)

iterations1 = 5 #number of times the sound is repeated)
iterations2 = 25 #number of times the sound is repeated)

tstep1 = timedelta(seconds=20).total_seconds()
tstep2 = timedelta(seconds=5).total_seconds()

##d.writeRegister(DAC0_REGISTER, 5.0)
start_time=time.time()


for i in np.arange(iterations1):
    d.writeRegister(DAC0_REGISTER, 5.0)
    core.wait(1) #interval between camera trigger and sound (in seconds)
    first_time=time.time()
    sound.play()
    core.wait(2) #recorded time after sound (in seconds)
    d.writeRegister(DAC0_REGISTER, 0)
    print("%s test"%(first_time-start_time))
    while time.time() < first_time + tstep1:
        1==1

for i in np.arange(iterations2):
    d.writeRegister(DAC0_REGISTER, 5.0)
    core.wait(1) #interval between camera trigger and sound (in seconds)
    first_time=time.time()
    sound.play()
    core.wait(2) #recorded time after sound (in seconds)
    d.writeRegister(DAC0_REGISTER, 0)
    print("%s habituation"%(first_time-start_time))
    while time.time() < first_time + tstep2:
        1==1

core.wait(5) #recovery time from habituation (in seconds)

d.writeRegister(DAC0_REGISTER, 5.0)
last_time=time.time()
sound.play()
core.wait(2) #recorded time after sound (in seconds)
d.writeRegister(DAC0_REGISTER, 0)
print("%s final test"%(last_time-start_time))
core.quit
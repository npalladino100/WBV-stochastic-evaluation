These programs generate and deliver signals to a vibrating platform, which are analyzed by accelerometers to determine the transmission distribution.

The WAV Generator program creates WAV files for a stochastic signal, which is passed through a 4th order Butterworth low pass filter with a cutoff frequency of 60 Hz.  In the first 5 minutes, the amplitude of the signal rises from zero to a level suitible for generating vibration in a metal platform.

A Raspberry Pi runs the program Vibration.py at startup, which schedules the WAV files to be played twice a day through the 3.5mm audio jack.  The signal is passed through an amplifier and into a transducer that actuates the metal platform.

An Arduino Mega with 16 analog inputs calibrates and collects data from multiple accelerometers (running the program accelerometer_read.ino).  This data is sent to the Raspberry Pi through USB.  The program Serial.py on the Raspberry Pi reads this data for any amount of time, and saves the acceleration values to a text file.  The program quickplot.py creates a rough graphical representation of this data.

The Raspberry Pi and the Arduino can be monitored and controlled remotely from another computer with VNC Viewer.

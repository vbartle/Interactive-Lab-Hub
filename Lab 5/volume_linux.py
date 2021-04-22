import alsaaudio
m = alsaaudio.Mixer()
vol = m.getvolume()
vol = int(vol[0])

newVol = vol + 10
m.setvolume(newVol)

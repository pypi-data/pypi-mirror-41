This is a package to find pitch of an audio signal ie. **wav file.**

Use the function by giving the input argument as the name of the *wav* file  *type==str*.
Function returns the value of the pitch of the audio.

import pitch
p=pitch.pitch_find('Sample.wav')

print('pitch =',p)


**Packages Required**
1.scipy
2.matplotlib
3.numpy


THE VALUE OF PITCH MAY BE IN THE RANGE OF AROUND(+7Hz to -7Hz) OF THE ACTUAL PITCH.

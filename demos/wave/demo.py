import wave
import sys


with wave.open('bojack.wav', 'rb') as file:
    with wave.open('test.wav', 'wb') as out:
        params = file.getparams()

        if params.nchannels != 1 or params.sampwidth != 1:
            sys.exit('wav file should be mono 8 bit')

        nframes = file.getnframes()
        out.setparams( (1, 1, params.framerate, nframes // 2, 'NONE', 'not compressed') )

        data = file.readframes(file.getnframes())
        out.writeframes( bytes([ data[i] for i in range(0, len(data), 2) ]) )

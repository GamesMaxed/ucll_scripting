import wave


with wave.open('bojack.wav', 'rb') as file:
    with wave.open('test.wav', 'wb') as out:
        nframes = file.getnframes()
        out.setparams( (1, 1, 44100, nframes // 2, 'NONE', 'not compressed') )

        data = file.readframes(file.getnframes())
        out.writeframes( bytes([ data[i] for i in range(0, len(data), 2) ]) )

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext): #uses self.ext without defining it
            raise Exception("Invalid file format")
        self.filename = filename
        
class MP3File(AudioFile):
    ext = "mp3" #here, in the child, ext is defined (self. exists only in functions)
    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav" #here, in the child, ext is defined
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg" #here, in the child, ext is defined
    def play(self):
        print("playing {} as ogg".format(self.filename))

if __name__=='__main__':
    ogg = OggFile("myfile.ogg")
    ogg.play()

    mp3 = MP3File("myfile.mp3")
    mp3.play()

    not_an_mp3 = MP3File("myfile.ogg")

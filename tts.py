from kokoro import KPipeline
import sounddevice as sd

class TTS:
    def __init__(self):
        self.pipeline=KPipeline(lang_code='a')

    def Speak(self,text):
        generate=self.pipeline(
            text=text,voice='af_heart',
            speed=1
            )

        for i,(gs,ps,audio) in enumerate(generate):
            sd.play(data=audio,samplerate=24000)
            sd.wait()

        print("text-to-speech completed....")


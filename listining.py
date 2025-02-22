import whisper
import pyaudio
import sounddevice as sd
from collections import deque
import numpy as np
import torch

class Listining:
    def __init__(self):
        self.device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model=whisper.load_model("large", device=self.device)

        self.sample_rate=16000
        self.chunk=1024
        self.channels=1
        self.silent_threshold=500
        self.deque=deque(maxlen=round(self.sample_rate/self.chunk * 5))

    def transcribe_audio(self,audio_data):
        results=self.model.transcribe(audio_data,fp16=torch.cuda.is_available())
        text=results['text']
        return text

    def Listen(self):
        self.audio=pyaudio.PyAudio()
        self.stream=self.audio.open(format=pyaudio.paInt16,
                        channels=self.channels,
                        rate=self.sample_rate,
                        input=True,
                        frames_per_buffer=self.chunk)
        
        self.frames=[]
        try:
            while True:
                data=self.stream.read(self.chunk,exception_on_overflow=False)
                audio_chunk=np.frombuffer(data,dtype=np.int16)
                self.frames.append(audio_chunk)

                self.deque.append(np.abs(audio_chunk).mean() < self.silent_threshold)

                if len(self.deque) == self.deque.maxlen and all(self.deque):
                    print("Silence detected for 5 seconds. Stopping recording.")
                    break
        except KeyboardInterrupt:
            print("Recording stopped manually.")

        print("Processing audio...")
        audio_data=np.concatenate(self.frames,axis=0).astype(np.float32) / 32768.0 
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        return self.transcribe_audio(audio_data)
    
l=Listining()
print(l.Listen())
    


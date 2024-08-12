from openai import OpenAI
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

audio_file= open("audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcription.text)

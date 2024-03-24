import whisper

model = whisper.load_model("small")
result = model.transcribe(r"C://Users//DAVID//Documents//PYTHON_UNIMAG//intro.wav", fp16=False)
print(result["text"])
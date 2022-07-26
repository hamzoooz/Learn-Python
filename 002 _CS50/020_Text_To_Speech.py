# # # # Need To Download pyttsx3 => pip install pyttsx3
# import pyttsx3
# # help(pyttsx3)
# hamza  = pyttsx3.init()
# hamza.setProperty("rate", 150)
# hamza.setProperty("volume", 0.9)
# name = input("Enter Your Name : ")
# hamza.say(f"Hello {name}")
# hamza.runAndWait()

# Convert Text To Speach Online 
from gtts import gTTS
import os
# tts = gTTS('السلام عليكم ورحمة الله وبركاته ', lang="ar")
tts = gTTS('الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ ( ) الرَّحْمَنِ الرَّحِيمِ ( ) مَالِكِ يَوْمِ الدِّينِ ( ) إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ () اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ () صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ ', lang="ar")
tts.save("hello.mp3")
os.system("hello.mp3")
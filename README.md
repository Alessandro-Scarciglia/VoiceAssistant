# VoiceAssistant
ROS2 Application of a Voice Assistant

# Structure
Marvin is my first experiment of voice assistant. It is coded within the ROS2 Framework and makes use of the *speech_recognition* module to implement low-level NLP functions. Each package implements a basic building block of a generic voice assistant.

![arch_voiceassistant](https://user-images.githubusercontent.com/58028470/200611846-c551197f-c919-47ff-adad-7f5150673839.png)

Since I have no constraints (yet) regarding the user's privacy, the Wake Word Detector (WWD) is englobed in the Speech-to-Text package, so that the assistant searches for the keyword within the input itself, instead of being triggered a priori.
Starting from such code of mine you can modify the *nl_understanding.py* node so that the server callback function can trigger a list of custom actions when a particular word has been said. 

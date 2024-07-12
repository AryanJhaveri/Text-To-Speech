from text_to_speech.exception import TTSException
from text_to_speech.logger import logger
from text_to_speech.entity.config_entity import TTSConfig
import sys
from text_to_speech.constants import TEXT_FILE_NAME
from text_to_speech.constants import CURRENT_TIME_STAMP
import os
from gtts import gTTS
import base64

class TTSapplication():
    def __init__(self, app_config = TTSConfig()) ->  None:
        try:
            self.app_config = app_config
            self.artifact_dir =app_config.artifact_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir
        except Exception as e:
            raise TTSException(e , sys)
        
    def text2speech(self, text, accent):
        try:
            # Ensure directories exist
            os.makedirs(self.text_dir, exist_ok=True)
            os.makedirs(self.audio_dir, exist_ok=True)

            text_file_name = TEXT_FILE_NAME
            text_file_path = os.path.join(self.text_dir, TEXT_FILE_NAME)

            # Log text input
            logger.info(f"Received text: {text}")

            with open(text_file_path, "a+") as file:
                file.write(f'\n{text}')

            # Create gTTS object
            tts = gTTS(text=text, lang='en', tld=accent, slow=False)

            file_name = f"converted_file_{CURRENT_TIME_STAMP}.mp3"
            audio_path = os.path.join(self.audio_dir, file_name)

            # Save the audio file
            tts.save(audio_path)
            logger.info(f"Audio file saved at: {audio_path}")

            # Read and encode the audio file to base64
            with open(audio_path, "rb") as file:
                audio_content = file.read()
                logger.info(f"Audio content length: {len(audio_content)}")
                base64_audio = base64.b64encode(audio_content).decode('utf-8')
                logger.info(f"Base64 encoded audio length: {len(base64_audio)}")

            return base64_audio

        except Exception as e:
            raise TTSException(e, sys)

        
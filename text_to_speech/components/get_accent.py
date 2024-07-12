from text_to_speech.exception import TTSException
from text_to_speech.logger import logger
import sys

def get_accent_tld(user_input):
    try:
        accent_input = {'Australia':'com.au',
                        'South Africa':'co.za',
                        'British': 'co.uk',
                        'Indian': 'co.in',
                        'Canadian': 'ca', 
                        'Irish':'ie',
                        'Spanish':'es'}
        tld= accent_input.get(user_input)
        return tld
    
    except Exception as e:
        raise TTSException(e, sys) 
        
        

def get_accent_message():
    try:
        accent = ['Australia', 'South Africa', 'British', 'Indian', 'Canadian', 'Irish', 'Spanish']
        return accent
    
    except Exception as e:
        raise TTSException(e, sys) from e 
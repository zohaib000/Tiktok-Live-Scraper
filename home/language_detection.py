from langdetect import detect, DetectorFactory
import sys
sys.setrecursionlimit(1500)
DetectorFactory.seed = 0

def get_language_name(code):
            language_map = {
                'af': 'Afrikaans',
                'am': 'Amharic',
                'ar': 'Arabic',
                'az': 'Azerbaijani',
                'be': 'Belarusian',
                'bg': 'Bulgarian',
                'bn': 'Bengali',
                'bs': 'Bosnian',
                'ca': 'Catalan',
                'ceb': 'Cebuano',
                'co': 'Corsican',
                'cs': 'Czech',
                'cy': 'Welsh',
                'da': 'Danish',
                'de': 'German',
                'el': 'Greek',
                'en': 'English',
                'eo': 'Esperanto',
                'es': 'Spanish',
                'et': 'Estonian',
                'eu': 'Basque',
                'fa': 'Persian',
                'fi': 'Finnish',
                'fil': 'Filipino',
                'fr': 'French',
                'fy': 'Frisian',
                'ga': 'Irish',
                'gd': 'Scots Gaelic',
                'gl': 'Galician',
                'gu': 'Gujarati',
                'ha': 'Hausa',
                'haw': 'Hawaiian',
                'hi': 'Hindi',
                'hmn': 'Hmong',
                'hr': 'Croatian',
                'ht': 'Haitian Creole',
                'hu': 'Hungarian',
                'hy': 'Armenian',
                'id': 'Indonesian',
                'ig': 'Igbo',
                'is': 'Icelandic',
                'it': 'Italian',
                'iw': 'Hebrew',
                'ja': 'Japanese',
                'jv': 'Javanese',
                'ka': 'Georgian',
                'kk': 'Kazakh',
                'km': 'Khmer',
                'kn': 'Kannada',
                'ko': 'Korean',
                'ku': 'Kurdish (Kurmanji)',
                'ky': 'Kyrgyz',
                'la': 'Latin',
                'lb': 'Luxembourgish',
                'lo': 'Lao',
                'lt': 'Lithuanian',
                'lv': 'Latvian',
                'mg': 'Malagasy',
                'mi': 'Maori',
                'mk': 'Macedonian',
                'ml': 'Malayalam',
                'mn': 'Mongolian',
                'mr': 'Marathi',
                'ms': 'Malay',
                'mt': 'Maltese',
                'my': 'Burmese',
                'ne': 'Nepali',
                'nl': 'Dutch',
                'no': 'Norwegian',
                'ny': 'Chichewa',
                'or': 'Odia (Oriya)',
                'pa': 'Punjabi',
                'pl': 'Polish',
                'ps': 'Pashto',
                'pt': 'Portuguese',
                'ro': 'Romanian',
                'ru': 'Russian',
                'rw': 'Kinyarwanda',
                'sd': 'Sindhi',
                'si': 'Sinhala',
                'sk': 'Slovak',
                'sl': 'Slovenian',
                'sm': 'Samoan',
                'sn': 'Shona',
                'so': 'Somali',
                'sq': 'Albanian',
                'sr': 'Serbian',
                'st': 'Sesotho',
                'su': 'Sundanese',
                'sv': 'Swedish',
                'sw': 'Swahili',
                'ta': 'Tamil',
                'te': 'Telugu',
                'tg': 'Tajik',
                'th': 'Thai',
                'tk': 'Turkmen',
                'tl': 'Filipino',
                'tr': 'Turkish',
                'tt': 'Tatar',
                'ug': 'Uyghur',
                'uk': 'Ukrainian',
                'ur': 'Urdu',
                'uz': 'Uzbek',
                'vi': 'Vietnamese',
                'xh': 'Xhosa',
                'yi': 'Yiddish',
                'yo': 'Yoruba',
                'zh-cn': 'Chinese (Simplified)',
                'zh-tw': 'Chinese (Traditional)',
                'zu': 'Zulu'
            }
            return language_map.get(code, 'Unknown')  


def detect_language(text):
        output_code=None
        try:
          output_code = detect(text)
        except:
          return "Not Found"
        output_name = get_language_name(output_code)

        print(f"Detected language code: {output_code}")
        print(f"Detected language name: {output_name}")

        return output_name
    

# detect_language("LEY DE ATRACCIÓN ✨\nTAROT Y ADIVINACIÓN 🪬🔮\nMAGIA Y HECHIZOS\nÚNICA CUENTA REAL🔺")
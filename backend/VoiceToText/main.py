from google.cloud import speech
import os
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

client = speech.SpeechClient.from_service_account_json('key.json')
fileName = "Input.mp3"

with open(fileName, 'rb') as f:
    mp3d = f.read()

audio_file = speech.RecognitionAudio(content = mp3d)

config = speech.RecognitionConfig(sample_rate_hertz = 44100,
                                  enable_automatic_punctuation = False,
                                  language_code= 'es-MX')

response = client.recognize(config=config, audio=audio_file)

print(response)
# https://speech.googleapis.com/v1p1beta1/speech:recognize
"""{
  "audio": {
    "content": "/* Your audio */"
  },
  "config": {
    "enableAutomaticPunctuation": true,
    "encoding": "LINEAR16",
    "languageCode": "en-US",
    "model": "default"
  }
} """





















"""
def sample_create_phrase_set(request):
     #Create a client

     #Initialize request argument(s)
    request = speech.CreatePhraseSetRequest(
        parent="parent_value",
   )

    # Make the request
    operation = client.create_phrase_set(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

def delete_and_insert():
    credentials_dict = {
        'type': 'service_account',
        'client_id': os.environ['BACKUP_CLIENT_ID'],
        'client_email': os.environ['jptjasc@gmail.com'],
        'private_key_id': os.environ['c324e59b3c1fd271dc8bdaf00a6171042f6608b9'],
        'private_key': os.environ['-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOFmn9gEl/PTBa\nn48V5XFjkVk+2uLOMu2FTNtqCxwZh1Vy9h5ZEK8yR+2DoemOpsaAV76CMqNdsjFW\nczrMQTDHf6WKcWhkDt5udS3M2cGVk38TG5lRLsNO46k3c5H1WKb+FtZZzfAdWtvd\nvNhpiuEiD2j5KRd6swIxeLN0ZHN3jOJchj6Er0V76DFDpjCnVJJubLcjkXJzQAfS\nn0SCikcohYDNArydKnDNQLItiuxOP0N+XpaYqEbPx7hNBCilRBPs6pMpJn1eIbHL\n/a3JgKEFTVvjNZLRS5yG7bNHfwkWQC/OXC0DkVaLyPXIb7F0EaER9mAXwznnX4i8\nEZW1/qddAgMBAAECggEABJ5eejqviv03UfSc+4/kkmdtwVmc9yOPjKr8CNyeYNkW\nWmj3JaZY0s7nXQmaJyMINFSjFZ5maGFntykGcpDsc7Ah6OAhR4rIw9926w4fR0ei\ns64s6bObV2+FOZOqu/2kYnHnFGSn4rSIVGgYzoa5BG8lel4II20TGcI7fVqJ9u4k\nSTOmUJwVijxEb+YCGtNtz0cK3uMIEoEWw4XzULou0XHrJum3TaLcthmUJRey+EHw\n//GgtOCFZqHNbX38utna/ZCrm7jJCYkSuiWjrGygH0CIQK7A5rebmE6NS6dHBzB0\nVhmCeVkPfrQK+scCI6xYBlOv6/eNYVpEw+VIWMmDeQKBgQD5K0sHh3BgkuBHDQa5\nhZDf5njgfNolqa/HKCtfql3AJVyv45CEwcgdRwhoylGmxUKQLMwPpBWYrVOgHyEv\nTI7X4jc6O8G6yt39SV/geMdUCauKxp5XLDFPa9XQI+W3kxntQuSMYgyQDsVMULFd\nRupIpMIY0PD/VP5+oYEpGTEO9QKBgQDTvMSaKcC4Ukv94VBKPEugR+x9/VDGvv2I\nwxQaD7tQITpnOsd0q0ro53iafk+G/dNj/VIZD0m7T5rSXXwZfTVfAJtZ553idZ1V\n6k2oASX3pFNWoUYgVC7x1QslSvo9biZMjrf5X5WfWyZ9W68BT0aCnteYhCKQKys0\nV6Wwnr6lyQKBgQDuNEpFR2DSoneQ1U4xfBQ1SMMUcaenS+KEtc1JZri7obxLVnVp\nxUwHWUobzBdlJL3u0TTAWzBeRo1kzX3PFxSUJGqB3HDnn1u78jKbiTueBqSdRiZH\n1jLJ56B/nGHXLuUhYsrVvkKeUdCilZ4KO2psyj3YtZ8/qkSmUMYGwVOaJQKBgBJy\nqfZ8mMv2b6SJEwPEyRoH6jT38ye90D0wMforULikjIAeAO7LVdWBBWMAilFKoDZg\nBd0lFdl6EBUwC/X0kMfcN6zXn0vxz2mC5o0yvGodKR2tI30BmK19UGFJbRAZHsEg\n1iqmB1VBDdNyP4cvrwcGa+Zf7Nr+x97hnBANZLLxAoGAK44kIfiatkAVv6t91HoM\n/ck1p4NVtqt3z5VGeTfcAmTU9+SAkvn8T7gjsoauSO6JOKR4N2icTEboidSyP1gF\n7O/pP+v0AyNB0YN/8d8cKpH85U9fck4DoMAJZKS3xLUtsUvOfWGnd1RxF1c/5bNm\nI07/6chjc2Ms/SUIcZYsVoA=\n-----END PRIVATE KEY-----\n",MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOFmn9gEl/PTBa\nn48V5XFjkVk+2uLOMu2FTNtqCxwZh1Vy9h5ZEK8yR+2DoemOpsaAV76CMqNdsjFW\nczrMQTDHf6WKcWhkDt5udS3M2cGVk38TG5lRLsNO46k3c5H1WKb+FtZZzfAdWtvd\nvNhpiuEiD2j5KRd6swIxeLN0ZHN3jOJchj6Er0V76DFDpjCnVJJubLcjkXJzQAfS\nn0SCikcohYDNArydKnDNQLItiuxOP0N+XpaYqEbPx7hNBCilRBPs6pMpJn1eIbHL\n/a3JgKEFTVvjNZLRS5yG7bNHfwkWQC/OXC0DkVaLyPXIb7F0EaER9mAXwznnX4i8\nEZW1/qddAgMBAAECggEABJ5eejqviv03UfSc+4/kkmdtwVmc9yOPjKr8CNyeYNkW\nWmj3JaZY0s7nXQmaJyMINFSjFZ5maGFntykGcpDsc7Ah6OAhR4rIw9926w4fR0ei\ns64s6bObV2+FOZOqu/2kYnHnFGSn4rSIVGgYzoa5BG8lel4II20TGcI7fVqJ9u4k\nSTOmUJwVijxEb+YCGtNtz0cK3uMIEoEWw4XzULou0XHrJum3TaLcthmUJRey+EHw\n//GgtOCFZqHNbX38utna/ZCrm7jJCYkSuiWjrGygH0CIQK7A5rebmE6NS6dHBzB0\nVhmCeVkPfrQK+scCI6xYBlOv6/eNYVpEw+VIWMmDeQKBgQD5K0sHh3BgkuBHDQa5\nhZDf5njgfNolqa/HKCtfql3AJVyv45CEwcgdRwhoylGmxUKQLMwPpBWYrVOgHyEv\nTI7X4jc6O8G6yt39SV/geMdUCauKxp5XLDFPa9XQI+W3kxntQuSMYgyQDsVMULFd\nRupIpMIY0PD/VP5+oYEpGTEO9QKBgQDTvMSaKcC4Ukv94VBKPEugR+x9/VDGvv2I\nwxQaD7tQITpnOsd0q0ro53iafk+G/dNj/VIZD0m7T5rSXXwZfTVfAJtZ553idZ1V\n6k2oASX3pFNWoUYgVC7x1QslSvo9biZMjrf5X5WfWyZ9W68BT0aCnteYhCKQKys0\nV6Wwnr6lyQKBgQDuNEpFR2DSoneQ1U4xfBQ1SMMUcaenS+KEtc1JZri7obxLVnVp\nxUwHWUobzBdlJL3u0TTAWzBeRo1kzX3PFxSUJGqB3HDnn1u78jKbiTueBqSdRiZH\n1jLJ56B/nGHXLuUhYsrVvkKeUdCilZ4KO2psyj3YtZ8/qkSmUMYGwVOaJQKBgBJy\nqfZ8mMv2b6SJEwPEyRoH6jT38ye90D0wMforULikjIAeAO7LVdWBBWMAilFKoDZg\nBd0lFdl6EBUwC/X0kMfcN6zXn0vxz2mC5o0yvGodKR2tI30BmK19UGFJbRAZHsEg\n1iqmB1VBDdNyP4cvrwcGa+Zf7Nr+x97hnBANZLLxAoGAK44kIfiatkAVv6t91HoM\n/ck1p4NVtqt3z5VGeTfcAmTU9+SAkvn8T7gjsoauSO6JOKR4N2icTEboidSyP1gF\n7O/pP+v0AyNB0YN/8d8cKpH85U9fck4DoMAJZKS3xLUtsUvOfWGnd1RxF1c/5bNm\nI07/6chjc2Ms/SUIcZYsVoA=\n'],
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project='myproject')
    bucket = client.get_bucket('mybucket')
    blob = bucket.blob('myfile')
    for blo in blob:
        blob.delete()
    blob.upload_from_filename('myfile')

"""

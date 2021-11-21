from source.project import Reader, Singleton
from source.producer import Producer

import json

if __name__ == '__main__':

    reader = Reader()
    result = reader.read(f"requirements.txt")

    singleton = Singleton()
    producer = Producer()

    for key in singleton.__dict__.keys():
        producer.request(key)

    with open('result.json', 'w') as converted_file:
        converted_file.write(json.dumps(singleton.__dict__))

from source.project import Reader, Project, Singleton
from source.producer import Producer

def test_producer_ok():
    
    reader = Reader()
    result = reader.read(f"requirements.txt")

    singleton = Singleton()
    producer = Producer()

    for key in singleton.__dict__.keys():
        producer.request(key)

    print('teste')
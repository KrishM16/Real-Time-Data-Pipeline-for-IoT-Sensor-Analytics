import time, json, random
from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {
        "sensor_id": f"S{random.randint(1,5)}",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(60, 100), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "vibration": round(random.uniform(0.01, 0.1), 3),
        "status": "normal" if random.random() > 0.05 else "anomaly"
    }
    producer.send('iot-sensor-data', value=data)
    print("Produced:", data)
    time.sleep(1)

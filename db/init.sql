CREATE TABLE IF NOT EXISTS iot_readings (
    sensor_id VARCHAR(10),
    timestamp TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    vibration FLOAT,
    status VARCHAR(20)
);

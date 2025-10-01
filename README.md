# 📡 Real-Time Data Pipeline for IoT Sensor Analytics 🚀  

This project demonstrates an **end-to-end real-time data engineering pipeline** for IoT sensor analytics. It covers **data ingestion, stream processing, ETL, storage, orchestration, and visualization**. The goal is to show how IoT data can be processed at scale to detect anomalies, monitor devices, and enable predictive maintenance.  

---

## 🔥 Key Features  
- ✅ Real-time **IoT data ingestion** using **Kafka** (with Python producer).  
- ✅ **Spark Structured Streaming** for scalable ETL & anomaly detection.  
- ✅ **Data Lake + Data Warehouse** architecture: Raw → Processed → Analytics.  
- ✅ **Delta Lake + PostgreSQL** for storage and querying.  
- ✅ **Apache Airflow** to orchestrate daily ETL pipelines.  
- ✅ **Power BI dashboards** for visualization & anomaly monitoring.  
- ✅ Fully **containerized setup** with **Docker Compose**.  

---

## 🏗️ System Architecture  
```text
IoT Devices (Simulated with Python Producer)  
         ↓  
Kafka Cluster (Message Broker)  
         ↓  
Spark Structured Streaming (ETL + Anomaly Detection)  
         ↓  
Delta Lake (Processed Data) & PostgreSQL (Analytics DB)  
         ↓  
Airflow (Orchestration)  
         ↓  
Power BI Dashboard (Visualization)  

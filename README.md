# Real-Time Data Pipeline with Kafka, Spark, and BigQuery  

## 📌 Description  
This project implements a **real-time data pipeline**, using **Apache Kafka** for data ingestion, **Apache Spark Streaming** for processing, and **Google BigQuery** for later analysis.  

The dataset consists of user activity data, including steps, calories burned, distance traveled, heart rate, and sleep hours.  

---

## 📂 Technologies Used  

- **🐍 Python**  
- **🛠 Apache Kafka** - Message broker for real-time data ingestion  
- **⚡ Apache Spark Streaming** - Stream processing framework  
- **☁ Google BigQuery** - Storage and analytics platform  
- **🐳 Docker** - For easy service setup  

---

## 🔧 Project Architecture  

```plaintext
User -> Kafka (Producer) -> Kafka (Broker) -> Spark Streaming (Consumer) -> BigQuery
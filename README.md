# **Real-Time Data Pipeline with Kafka, Spark, and Local Storage**

## 📌 **Description**  
This project implements a real-time data pipeline using **Apache Kafka** for data ingestion, **Apache Spark Streaming** for processing, and **local storage** for storing and analyzing the data.  

The dataset consists of **simulated user activity data**, including metrics such as steps, calories burned, distance traveled, heart rate, and sleep patterns. These records are continuously produced and consumed in real-time to demonstrate a streaming ETL workflow.  

## 📂 **Technologies Used**  
- 🐍 **Python** – Core programming language  
- 🛠 **Apache Kafka** – Message broker for real-time data ingestion  
- ⚡ **Apache Spark Streaming** – Stream processing framework  
- 🐳 **Docker** – Containerization for easy service setup  

## 🔧 **Project Architecture**  
```plaintext
User -> Kafka (Producer) -> Kafka (Broker) -> Spark Streaming (Consumer) -> Local Storage
```

1. **Producer**: Generates simulated user activity data and sends it to Kafka.  
2. **Kafka (Broker)**: Acts as a real-time event bus.  
3. **Spark Streaming (Consumer)**: Reads the streaming data from Kafka, processes it, and prepares it for storage.  
4. **BigQuery**: Stores the processed data for further analysis.  

## 📊 **Streaming Data Schema**  
Each record in the stream represents **a user activity event** with the following attributes:  

| Column              | Type      | Description                                      |
|---------------------|----------|--------------------------------------------------|
| `user_id`          | Integer   | Unique identifier for the user                   |
| `date`             | String    | Activity date (YYYY-MM-DD)                      |
| `steps`            | Integer   | Number of steps taken                           |
| `calories_burned`  | Float     | Calories burned during the activity             |
| `distance_km`      | Float     | Distance covered (in km)                        |
| `active_minutes`   | Integer   | Active minutes during the day                   |
| `sleep_hours`      | Float     | Total sleep duration in hours                   |
| `heart_rate_avg`   | Integer   | Average heart rate (bpm)                        |
| `workout_type`     | String    | Type of workout (e.g., running, cycling, yoga)  |
| `weather_conditions` | String  | Weather during the activity (e.g., sunny, rainy) |
| `location`         | String    | User’s location (e.g., New York, Tokyo, Sydney) |
| `mood`            | String     | User's mood (happy, neutral, sad)               |


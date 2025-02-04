from confluent_kafka import Producer
import json
import time
import random
from datetime import datetime, timedelta

# Kafka configuration
conf = {'bootstrap.servers': 'localhost:9092'}

# Create Producer instance
producer = Producer(conf)

# Topic to produce to
topic = 'user_activity'

# Simulate user activity data
def generate_user_activity():
    user_id = random.randint(1, 100)  # Random user ID between 1 and 100
    date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')  # Random date within the last year
    steps = random.randint(0, 30000)  # Steps taken
    calories_burned = round(random.uniform(0, 1000), 2)  # Calories burned
    distance_km = round(random.uniform(0, 50), 2)  # Distance in km
    active_minutes = random.randint(0, 1440)  # Active minutes in a day
    sleep_hours = round(random.uniform(0, 12), 1)  # Sleep hours
    heart_rate_avg = random.randint(50, 150)  # Average heart rate
    workout_type = random.choice(['running', 'cycling', 'swimming', 'yoga', None])  # Workout type (some nulls)
    weather_conditions = random.choice(['sunny', 'rainy', 'cloudy', 'snowy'])  # Weather conditions
    location = random.choice(['New York', 'London', 'Tokyo', 'Sydney'])  # Location
    mood = random.choice(['happy', 'neutral', 'sad'])  # Mood

    return {
        'user_id': user_id,
        'date': date,
        'steps': steps,
        'calories_burned': calories_burned,
        'distance_km': distance_km,
        'active_minutes': active_minutes,
        'sleep_hours': sleep_hours,
        'heart_rate_avg': heart_rate_avg,
        'workout_type': workout_type,
        'weather_conditions': weather_conditions,
        'location': location,
        'mood': mood
    }

# Produce messages
for _ in range(1000):  # Produce 1000 messages
    data = generate_user_activity()
    producer.produce(topic, key=str(data['user_id']), value=json.dumps(data))
    producer.flush()
    time.sleep(1)  # Simulate real-time data (1 message per second)
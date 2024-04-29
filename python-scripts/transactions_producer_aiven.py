import json
import random
import string
import uuid
from datetime import datetime

from faker import Faker
from kafka import KafkaProducer

fake = Faker()
topic_name = "financial_transactions"

producer = KafkaProducer(
 bootstrap_servers=f"sa-kafka-homework-carlsongould-2cdd.l.aivencloud.com:10358",
 security_protocol="SSL",
 ssl_cafile="/Users/jeffreycarlson/se-workspace/workspace/companies/aiven/notebooks/ca.pem",
 ssl_certfile="/Users/jeffreycarlson/se-workspace/workspace/companies/aiven/notebooks/service.cert",
 ssl_keyfile="/Users/jeffreycarlson/se-workspace/workspace/companies/aiven/notebooks/service.key" ,
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)

def generate_random_id():
    return str(uuid.uuid4())

def generate_random_account():
    return ''.join(random.choices(string.digits, k=10))

def generate_random_amount():
    return round(random.uniform(100, 10000), 2)

def generate_random_timestamp():
    return datetime.utcnow().isoformat()

def generate_event():
    event_id = generate_random_id() #payment id
    event_timestamp = generate_random_timestamp() #payment timestamp
    event_account_number = generate_random_account() #payees payment account
    event_account_holder = fake.name()#Payees name
    event_amount = generate_random_amount() #payment amount
    event_payment_details = str(fake.credit_card_full())
    event_url = str(fake.url())

    event_data = {
        'id': event_id,
        'payment_timestamp': event_timestamp,
        'account_number': event_account_number,
        'account_holder': event_account_holder,
        'payment_amount': event_amount,       
    }
    return event_data

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to topic {msg.topic()}")

def produce_event():
    event = generate_event()
    key = {'id': event['id']}
    value = event
    print( 'Sending Event Key: ', key, '\nSending Event payload:',event )
    producer.send(topic_name, key=key, value=value)

    producer.flush()
    #return value 

if __name__ == '__main__':
  produce_event()


import time
import random
import datetime
import pymysql

//Script will insert data into a database named 'payment'
conn = pymysql.connect(
    host="localhost",
    user="myuser",
    password="mypass",
    database="payment"
)
cursor = conn.cursor()
customers = [f"CUST{i}" for i in range(1, 5)]
transaction_types = ["DEPOSIT", "WITHDRAWAL"]

while True:
    for customer in customers:
        transaction_type = random.choice(transaction_types)
        reference_number = f"{customer}-{int(datetime.datetime.now().timestamp())}"
        description = f"{transaction_type} for {customer}"
        start_time = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        hour = random.randint(0, 23)
        #randdate = random.randint(3,10)

        transaction_start_time = datetime.datetime.now().replace(hour=hour)

        if hour >= 8 and hour <= 17:
          status = random.choice(["SUCCESS","PENDING","PENDING"])
          amount = random.uniform(4000, 10000)
          transaction_end_time = transaction_start_time + datetime.timedelta(seconds=random.randint(100, 900))
        else:
          status = random.choice(["SUCCESS","PENDING"])
          amount = random.uniform(10, 500)
          transaction_end_time = transaction_start_time + datetime.timedelta(seconds=random.randint(30, 200))

        query = "INSERT INTO payments (account_number, transaction_start_time, transaction_end_time, amount, transaction_type, reference_number, description, transaction_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        rsp=cursor.execute(query, (customer, transaction_start_time, transaction_end_time, amount, transaction_type, reference_number, description, status))
        print(f"Inserted data for customer {customer}, result: {rsp}")

    conn.commit()
    time.sleep(10)

conn.close()


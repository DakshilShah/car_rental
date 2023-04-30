import random
import time
import json

data = []

for i in range(100):
    start_time = int(time.time()) - random.randint(1, 1000)*3600

    rental_id = ''.join(random.choices(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

    start_comments = random.choice(
        ['', 'No issues - brand new and shiny!', 'Small dent on passenger door', 'Scratch on driver\'s door'])

    start_record = {"type": "START", "id": rental_id,
                    "timestamp": start_time, "comments": start_comments}

    data.append(start_record)

    # Only generate end record for some start records
    if random.random() < 0.5:
        end_time = start_time + random.randint(1, 24)*3600
        end_comments = random.choice(['', 'Car is missing both front wheels!',
                                      'Small dent on passenger door', 'Crack found in front passenger window'])

        end_record = {"type": "END", "id": rental_id,
                      "timestamp": end_time, "comments": end_comments}

        data.append(end_record)

data.append({"type": "END", "id": str(int(time.time())),
            "timestamp": 123499, "comments": ""})

# print(data)
with open('sample.json', 'w') as f:
    json.dump(data, f, indent=4)

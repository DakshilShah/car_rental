import json
import datetime

# read in the JSON file
with open('sample.json', 'r') as f:
    data = json.load(f)

summary = {}

# iterate over each record in the data
for record in data:
    # check if the id exists in the summary dictionary
    if record['id'] in summary:
        # if it exists, update the end time and comments
        summary[record['id']]['end_time'] = record['timestamp']
        summary[record['id']]['comments'] = record.get('comments', '')
    else:
        # if it doesn't exist, create a new entry in the summary dictionary
        summary[record['id']] = {
            'id': record['id'],
            'start_time': record['timestamp'],
            'end_time': '',
            'duration': '',
            'late_return': False,
            'damage': False,
            'comments': record.get('comments', '')
        }

# calculate the duration for each session
for session in summary.values():
    startTime_obj = datetime.datetime.fromtimestamp(int(session['start_time']))
    startTime = startTime_obj.strftime("%m/%d/%y %I:%M:%S %p")
    start_time = startTime
    endTime_obj = datetime.datetime.fromtimestamp(
        int(session['end_time'])) if session['end_time'] else ""
    endTime = endTime_obj.strftime(
        "%m/%d/%y %I:%M:%S %p") if session['end_time'] else ""
    end_time = endTime
    if start_time and end_time:
        duration = endTime_obj - startTime_obj
        session['duration'] = str(duration)
        session['late_return'] = True if duration.days >= 1 else False
        session['damage'] = bool(session['comments'])
    session['start_time'] = startTime
    session['end_time'] = endTime


# write the summary data to a new JSON file
with open('output.json', 'w') as f:
    json.dump(list(summary.values()), f, indent=4)

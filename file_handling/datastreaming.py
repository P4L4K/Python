'''datastreaming is continuoulsy sending feeds
           sending live datastreaming or realtime data sending
           it is continuous flow of data that is generated andprocessed in real time or near real time
           instead of dealing wiht a static dataset, where all data is avvailable at once, data stream involve the continuous and dynamic arrival of data over time

           eg: instagram, facebook, youtube
'''
import time
def data_stream_generator():
    count=0
    while True:
        yield f"Data Point {count}" #return -> yield
        count+=1
        time.sleep(3)

my_data=data_stream_generator()
for _ in range(5):
  data_point=next(my_data)
  print(data_point)

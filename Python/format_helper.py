
from input_helper import int_to_day

def format_date(date): #pass in (y,m,d)
     return months[date[1] - 1] + " " + str(date[2]) + ", " + str(date[0])


def format_time(time, with_seconds = False): #pass in (h,m,s)
     return str(time[0]) + ":" + str(time[1]) + (str(time[2]) if with_seconds else "" )


def draw_graph(data, height):

     data_min = min(data)
     data_max = max(data)
     data_range = data_max - data_min
     mult = data_range / height
     actual_width = len(data)

     print()
     for i in range(height, -1, -1):
          row = (i * mult) + data_min
          print(str(int(row)).rjust(5), end = "|")
          for j in range(actual_width):
               if row <= data[j]:
                    print(" #", end = "")
               else:
                    print("  ", end = "")
          print(" |", str(int(row)).ljust(5))
     print()
     print()

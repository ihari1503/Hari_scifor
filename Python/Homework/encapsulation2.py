class student:
  def __init__(self,name,studentid,present_days):
    self.name
    self.__studentid
    self.attendance

  def getstdid(self):
    return self.__studentid

  def attend(self,total_days):
    attendance = (self.present_days/total_days)*100
    print("Total Attendance is" +attendance)
    
 std = student("Aayush","SD1256",57)
   print(std.name)
   print(std.getstdid)
   print(std.present_days)



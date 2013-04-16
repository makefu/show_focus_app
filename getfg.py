from ctypes import *
import ctypes
from psutil import process_iter
import psutil

def getForegroundApp():
  hwnd = windll.user32.GetForegroundWindow()
  pid = c_ulong()
  threadid = windll.user32.GetWindowThreadProcessId(hwnd,byref(pid))
  processid = pid.value
  apps = filter(lambda p: p.pid == processid, process_iter())
  for app in apps:
    return (app.pid,app)

from time import sleep,strftime,localtime
curr = ()
print "PSUTIL Version: %s" % psutil.__version__
print "CTYPES Version: %s" % ctypes.__version__
while 1:
  try:
    now,app = getForegroundApp()
  except:
    print "Foreground is borken"
    now = None
  try:
    if curr != now:
      print "Pid: %s" %app.pid
      print "Name: %s" %app.name
      print "create_time: %s" % strftime("%a, %d %b %Y %H:%M:%S", localtime(app.create_time))
      try:
        print "exe: %s" %app.exe
      except:
        print "exe: has no executable path"
      print "cmdline: %s" %" ".join(app.cmdline)
      #print "Open Files: %s" % ";".join( [ f.path for f in  app.get_open_files()])
      try:
        parlvl = 1
        par = app.parent
        while 1:
          if par.pid == 0 : 
            print "parent: self"
            break
          print parlvl * 2 * " " + "ppid: %s" %par.pid
          print parlvl * 2 * " " + "parent: %s" %par.name
          try:
            print parlvl * 2 * " " + "exe: %s" %par.exe
          except:
            print parlvl * 2 * " " + "exe: has no executable path"
          print parlvl * 2 * " " + "cmdline: %s" % " ".join(par.cmdline)
          #print parlvl * 2 * " " + "Open Files: %s" % ";".join( [ f.path for f in  par.get_open_files()])
          par = par.parent
          parlvl = parlvl + 1
      except Exception as e:
        print "parent: end of parent (%s)" % str(e)
      print
      curr = now
    sleep(0.1)
  except Exception as e:
    print "Something went horribly wrong: %s" % str(e)

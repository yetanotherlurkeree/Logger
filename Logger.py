import datetime

class Logger:
    # Init function: makes the log file when possible and initializes values
    def __init__(self,logfile):
        try:
            self.logfile = open(logfile+".log", "a")
        except:
            input("Press enter to quit....")
        self.loglevel=2 # Only events lower than this number are written to the log file. Basically, a filter to not write everything. 
        self.OutputToShell=1 # this setting indicates whether the output should go to the shell. 

    # There are different types. The higher the number, the lower the priority
    def getType(self, aType):
        strLogType="Diagnostic"
        if (aType==1): strLogType="Error"
        if (aType==2): strLogType="Event"
        return strLogType

    # gets the timestamp in the correct format. 
    def getTimeStamp(self):
        strTS = datetime.datetime.now().isoformat()
        return strTS
        
    # Logs the event to the file by writing the type and event name
    def logEvent(self, aType, aEvent):
        strLogType= self.getType(aType)
        strTS = self.getTimeStamp()

        strLine = strTS + ": " + strLogType +": " + aEvent+ "\n"
        if (self.loglevel>=aType): self.logfile.write(strLine)
        if (self.OutputToShell>=aType): print(strLine)

    # Sets the log level
    def setLogLevel(self,aLoglevel):
        self.loglevel=int(aLoglevel)

    def stopLogging(self):
        self.logfile.close()

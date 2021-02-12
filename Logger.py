import datetime

class Logger:
    def __init__(self,logfile):
        try:
            self.logfile = open(logfile+".log", "a")
        except:
            input("Press enter to quit....")
        self.loglevel=2
        self.OutputToShell=1

    def getType(self, aType):
        strLogType="Diagnostic"
        if (aType==1): strLogType="Error"
        if (aType==2): strLogType="Event"
        return strLogType

    def getTimeStamp(self):
        strTS = datetime.datetime.now().isoformat()
        return strTS
        
    def logEvent(self, aType, aEvent):
        strLogType= self.getType(aType)
        strTS = self.getTimeStamp()

        strLine = strTS + ": " + strLogType +": " + aEvent+ "\n"
        if (self.loglevel>=aType): self.logfile.write(strLine)
        if (self.OutputToShell>=aType): print(strLine)

    def setLogLevel(self,aLoglevel):
        self.loglevel=int(aLoglevel)

    def stopLogging(self):
        self.logfile.close()

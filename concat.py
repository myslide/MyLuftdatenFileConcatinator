#concat the specified(per tempplate) files from opensensemap by year given.
#mysli 20240214
from datetime import date,timedelta

dateformat="%Y-%m-%d"
startYear=2023
endYear=2023
sensorID="12345"
folder="../archiv/2023/"
targetfolder="../archiv/"
fileNameTemplate="_bme280_sensor_"+sensorID+".csv"

fileout=str(startYear)+fileNameTemplate
incDay=timedelta(days=1)
startDate = date(startYear, 1, 1)
endDate = date(endYear, 12, 31)
targetFile=open(targetfolder+fileout,'a')
dateTag=startDate
removeHeader=False

while dateTag<=endDate:
    try:
        with open(folder+dateTag.strftime(dateformat)+fileNameTemplate,'r') as content:
            if (removeHeader):
                content.readline() #removes the header line
            targetFile.write(content.read())
            removeHeader=True
    except:
        print(folder+dateTag.strftime(dateformat)+fileNameTemplate+" skipped, since it does not exists.")
    dateTag=dateTag+incDay;

targetFile.close()
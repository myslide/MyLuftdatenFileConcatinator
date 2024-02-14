#Merges (according template) files from http://archive.sensor.community/ from the specified year. 
#used the files, imported by "MyLuftdatenArchiver". 
#mysli 20240214
from datetime import date,timedelta

dateformat="%Y-%m-%d"
startYear=2023
endYear=2023
sensorID="12345"#your individual id
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
            else:
                removeHeader=True            
            targetFile.write(content.read())  
    except Exception as err: 
            #print(f"Unexpected {err=}, {type(err)=}")
            print(folder+dateTag.strftime(dateformat)+fileNameTemplate+" skipped, since it does not exists.")
    dateTag=dateTag+incDay;

targetFile.close()
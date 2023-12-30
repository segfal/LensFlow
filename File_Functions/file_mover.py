import os, shutil,time,datetime

def move_files(source, destination):
    files = os.listdir(source)

    files.sort(key=lambda x: os.path.getmtime(os.path.join(source, x)))
    dates = {}
    for f in files:
        # mm/dd/yyyy format no seconds no minutes no day
        date = time.ctime(os.path.getmtime(os.path.join(source, f)))
        #transform date to mm.dd.yyyy
        date = datetime.datetime.strptime(date, "%a %b %d %H:%M:%S %Y")
        date = date.strftime("%m_%d_%Y")
        
        if date not in dates:
            dates[date] = [f]
        else:
            dates[date].append(f)
        
    for date in dates:
        #create folder for date
        if not os.path.exists(os.path.join(destination, date)):
            os.mkdir(os.path.join(destination, date))
            for f in dates[date]:
                if not os.path.exists(os.path.join(destination, date, f)):
                    shutil.move(os.path.join(source, f), os.path.join(destination, date))
        else:
            for f in dates[date]:
                #check if file already exists
                if not os.path.exists(os.path.join(destination, date, f)):
                    shutil.move(os.path.join(source, f), os.path.join(destination, date))
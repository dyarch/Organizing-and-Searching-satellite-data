import os
import glob
import zipfile
import shutil
dir_path = r'\\192.168.1.152\ncfc data\Nadams Input Data\Satellite_data'
os.chdir(dir_path)
target = open('resource_year.txt', 'w')
for zip_name in glob.glob('[0-9]*.zip'):
    z = zipfile.ZipFile(zip_name)
    date_flag = 0
    date_line = 0
    count = 0
    done = 0
    subdir = os.path.splitext(zip_name)[0]
    # subdir = zip_name[:-4]
    # print zip_name
    target.write(zip_name)
    target.write(":")
    with z.open('/{}/BAND_META.txt'.format(subdir)) as f:
        for line in f:
            for word in line.split('='):
                word = word.strip()
                count += 1
                if date_flag == 0:
                    if word == "DateOfPass":
                        # print word
                        date_line = count
                        date_flag = 1
                elif date_flag == 1:
                    if count == date_line+1:
                        year = word[-4:]
                        # print year
                        target.write(year)
                        target.write("\n")
                        if not os.path.exists(year):
                            os.makedirs(year)
                        done = 1
                if done == 1:
                    break
            else:
                continue
            break
    z.close()
target.close()
count = 0
with open('resource_year.txt','r') as f:
    for line in f:
        for word in line.split(':'):
            word = word.strip()
            count += 1
            # print word
            if count%2 == 1:
                zip_name = word
            else:
                year = word
                shutil.move(zip_name,year)
for folder_name in glob.glob('[0-9]*'):
    os.chdir(folder_name)
    target = open('resource_sensor.txt','w')
    for zip_name in glob.glob('[0-9]*.zip'):
        z = zipfile.ZipFile(zip_name)
        target.write(zip_name)
        target.write(":")
        count = 0
        sensor_flag = 0
        sensor_line = 0
        done = 0
        subdir = zip_name[:-4]
        with z.open('/{}/BAND_META.txt'.format(subdir)) as f:
            for line in f:
                for word in line.split('='):
                    word=word.strip()
                    count += 1
                    if sensor_flag == 0:
                        if word == 'Sensor':
                            sensor_flag = 1
                            sensor_line = count
                    elif sensor_flag == 1:
                        if count == sensor_line + 1:
                            sensor = word
                            target.write(sensor)
                            target.write("\n")
                            done = 1
                    if done == 1:
                        break
                else:
                    continue
                break
    z.close()
    target.close()
    count = 0
    with open('resource_sensor.txt','r') as  f:
        for line in f:
            for word in  line.split(':'):
                word = word.strip()
                count += 1
                if count%2 == 1:
                    zip_name = word
                else:
                    if word == 'AW':
                        sensor = 'AWIFS'
                    elif word == 'L3':
                        sensor = 'LISS-III'
                    elif word == 'SAR':
                        sensor = 'RISAT-I'
                    elif word == 'L4':
                        sensor = "LISS-IV"
                    else:
                        sensor = word
                    if not os.path.exists(sensor):
                        os.makedirs(sensor)
                    shutil.move(zip_name, sensor)
    os.chdir("..")
import glob
import os
import zipfile
def month_number(month):
    if month == 'JAN':
        month = 1
    elif month == 'FEB':
        month = 2
    elif month == 'MAR':
        month = 3
    elif month == 'APR':
        month = 4
    elif month == 'MAY':
        month = 5
    elif month == 'JUN':
        month = 6
    elif month == 'JUL':
        month = 7
    elif month == 'AUG':
        month = 8
    elif month == 'SEP':
        month = 9
    elif month == 'OCT':
        month = 10
    elif month == 'NOV':
        month = 11
    elif month == 'DEC':
        month = 12
    else:
        return 20
    return month
# print "Directory or Path: "
dir_path = r'Absolue-address-or-path-to-the-directory-where-the-data-is-stored'
os.chdir(dir_path)
n = 1
with open(r'C:\xampp\htdocs\mncfc\Typeone.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if n == 1:
            choice = line
        elif n == 2:
            dateofpass_one = line
        elif n == 3:
            dateofpass_two = line
        elif n == 4:
            sensor = line
        elif n == 5:
            startpath = line
        elif n == 6:
            startrow = line
        elif n == 7:
            endpath = line
        elif n == 8:
            endrow = line
        n += 1

if choice == "1":
    dayofpass_one = dateofpass_one[:-9]
    monthofpass_one = dateofpass_one[:-5]
    monthofpass_one = monthofpass_one[-3:]
    monthofpass_one = int(month_number(monthofpass_one))
    if monthofpass_one == 20:
        print "Invalid month entered."
    else:
        year = dateofpass_one[-4:]
        # print year
        dayofpass_two = dateofpass_two[:-9]
        monthofpass_two = dateofpass_two[:-5]
        monthofpass_two = monthofpass_two[-3:]
        monthofpass_two = int(month_number(monthofpass_two))
        if monthofpass_one == 20:
            print "Invalid month entered."
        else:
            # print dayofpass_one
            # print monthofpass_one
            # print dayofpass_two
            # print monthofpass_two
            os.chdir(year)
            if sensor == "1":
                sensor = "AWIFS"
            elif sensor == "2":
                sensor = "LISS-III"
            elif sensor == "3":
                sensor = "RISAT-I"
            elif sensor == "4":
                sensor = "LISS-IV"
            os.chdir(sensor)
            target = open(r'C:\xampp\htdocs\mncfc\Queryoneres.txt', 'w')
            targeter = open(r'C:\xampp\htdocs\mncfc\Coordinates.txt', 'w')
            for zip_name in glob.glob('[0-9]*.zip'):
                z = zipfile.ZipFile(zip_name)
                date_flag = 0
                date_line = 0
                printed = 0
                ullat_flag = 0
                ullat_line = 0
                ullon_flag = 0
                ullon_line = 0
                lrlat_flag = 0
                lrlat_line = 0
                lrlon_flag = 0
                lrlon_line = 0
                month = 0
                day = 0
                doner = 0
                checker = 0
                row_flag = 0
                row_line = 0
                path_flag = 0
                path_line = 0
                count = 0
                check = 0
                done = 0
                subdir = zip_name[:-4]
                with z.open('/{}/BAND_META.txt'.format(subdir)) as f:
                    for line in f:
                        for word in line.split('='):
                            word = word.strip()
                            # print word
                            count += 1
                            if date_flag == 0:
                                if word == "DateOfPass":
                                    # print word
                                    date_line = count
                                    date_flag = 1
                            elif date_flag == 1:
                                if count == date_line+1:
                                    day = word[:-9]
                                    # print day
                                    month = word[:-5]
                                    if month[1] == '-':
                                        month = month[-2:]
                                    else:
                                        month = month[-3:]
                                    month = int(month_number(month))
                                    if month < monthofpass_one:
                                        done = 1
                                    elif month == monthofpass_one:
                                        if monthofpass_one == monthofpass_two:
                                            if int(day) >= int(dayofpass_one):
                                                if int(day) <= int(dayofpass_two):
                                                    check += 1
                                        else:
                                            if int(day) >= int(dayofpass_one):
                                                check += 1
                                    elif month > monthofpass_one:
                                        if month < monthofpass_two:
                                            check += 1
                                        elif month == monthofpass_two:
                                            if int(day) <= int(dayofpass_two):
                                                check += 1
                                            else:
                                                done = 1
                                        else:
                                            done = 1
                            if row_flag == 0:
                                if word == "Row":
                                    row_flag = 1
                                    row_line = count
                            elif row_flag == 1:
                                if count == row_line+1:
                                    if int(word) >= int(startrow):
                                        if int(word) <= int(endrow):
                                            check += 1
                            if path_flag == 0:
                                if word == "Path":
                                    path_flag = 1
                                    path_line = count
                            elif path_flag == 1:
                                if count == path_line+1:
                                    if int(word) >= int(startpath):
                                        if int(word) <= int(endpath):
                                            check += 1
                            if check == 3 and printed == 0:
                                pwd = os.getcwd()
                                path_name = pwd+'\\'+zip_name
                                target.write(path_name)
                                target.write(" \n")
                                #print path_name
                                done = 1
                                printed = 1
                            if done == 1:
                                if ullat_flag == 0:
                                    if word == "ProdULLat":
                                        ullat_flag = 1
                                        ullat_line = count
                                elif ullat_flag == 1:
                                    if count == ullat_line+1:
                                        #print word
                                        one = word
                                        checker += 1
                                if ullon_flag == 0:
                                    if word == "ProdULLon":
                                        ullon_flag = 1
                                        ullon_line = count
                                elif ullon_flag == 1:
                                    if count == ullon_line +1:
                                        #print word
                                        two = word
                                        checker += 1
                                if lrlat_flag == 0:
                                    if word == "ProdLRLat":
                                        lrlat_flag = 1
                                        lrlat_line = count
                                elif lrlat_flag == 1:
                                    if count == lrlat_line+1:
                                        #print word
                                        three = word
                                        checker += 1
                                if lrlon_flag == 0:
                                    if word == "ProdLRLon":
                                        lrlon_flag = 1
                                        lrlon_line = count
                                elif lrlon_flag == 1:
                                    if count == lrlon_line+1:
                                        #print word
                                        four = word
                                        checker += 1
                            if checker == 4:
                                doner = 1
                            if done == 1 and doner == 1:
                                targeter.write(one)
                                targeter.write("\n")
                                targeter.write(two)
                                targeter.write("\n")
                                targeter.write(three)
                                targeter.write("\n")
                                targeter.write(four)
                                targeter.write("\n")
                                break
                        else:
                            continue
                        break
            target.close()

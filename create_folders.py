import os

#Utilizing the os library to make directory changes 
#This specific program was intended to be used to make multiple folders at once, rather than just hand naming each folder
def main():
    directoryName = 'Lab'
    for number in range(1,13):
        
        directoryName = directoryName + ' ' + str(number)
        try: 
            os.mkdir(directoryName) #Main command for making a directory
            print("Directory ", directoryName, " Created")
        except: 
            #Catching potential errors of folders already existing
            print("Directory ", directoryName, " already exists")
        directoryName = 'Lab'

if __name__ == '__main__':
    main()

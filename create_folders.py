import os

def main():
    directoryName = 'Lab'
    for i in range(1,13):
        
        directoryName = directoryName + ' ' + str(i)
        try: 
            os.mkdir(directoryName)
            print("Directory ", directoryName, " Created")
        except:
            print("Directory ", directoryName, " already exists")
        directoryName = 'Lab'

if __name__ == '__main__':
    main()
#writes csv
import csv
import os

def w_csv(x,output='FCfile.csv',verb = True):
    #accepts lists of other lists, spits out CSV file
    count = 1
    while file_present(output):
        output = output.split('.')[0] + "-" + str(count) + '.csv'
        count += 1
        if not file_present(output):
            break
 

    csv_out = open(output, 'w', newline='', encoding='utf-8')
    mywriter = csv.writer(csv_out)
    '''try:
        print("This is x: %s" % (x))
    except UnicodeEncodeError as UE:
        print("Cannot print to console due to Unicode Error")'''
    if verb: print("Saved file as \"{0}\"".format(output))

    mywriter.writerows(x)
    csv_out.close()
    
def file_present(x):
    #only checks current working directory
    full_path = os.getcwd() + '\\' + x
    if os.path.exists(full_path):
        return True
    if not os.path.exists(full_path):
        return False
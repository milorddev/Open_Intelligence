import multiprocessing
import subprocess
'''
def worker(file):

    if __name__ == '__main__':
        files = ["./Eyesight/Primitive_Eyesight.py","./Hearing/AmplitudeTest.py"]
        for i in files:
            p = multiprocessing.Process(target=worker(i))
            print p
'''

subprocess.Popen(['screen', '/Eyesight/Primitive_Eyesight.py']) 
subprocess.Popen(['screen', '/Hearing/AmplitudeTest.py']) 

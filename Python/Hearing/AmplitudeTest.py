#!/usr/bin/python

# open a microphone in pyAudio and listen for taps

import pyaudio
import struct
import math
import pygame
import sys

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Graph Amplitude')

Bottom = 480*.66;
Top = 480*.33;
done = False

Mult = Bottom - Top;
AmpValue = 9;

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



INITIAL_TAP_THRESHOLD = 0.010
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
# if we get this many noisy blocks in a row, increase the threshold
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
# if we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
# if the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

def get_rms( block ):
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768. 
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0
        self.AmpValue = 0;

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream

    def tapDetected(self):
        print "Tap!"
        #print get_rms(self.stream.read(INPUT_FRAMES_PER_BLOCK));
        

    def listen(self):
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError, e:
            # dammit. 
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = get_rms( block )
        self.AmpValue = amplitude * 300
        if amplitude > self.tap_threshold:
            # noisy block
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:
                # turn down the sensitivity
                self.tap_threshold *= 1.1
                print "turn down";
        else:            
            # quiet block.

            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                self.tapDetected()
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                # turn up the sensitivity
                self.tap_threshold *= 0.9
                print "turn up"
                
        

if __name__ == "__main__":
    tt = TapTester()

    count = 0;
    CurrentPoint = [count,AmpValue*Mult]
    OldPoint = CurrentPoint
    

    while not done:
            LinePlot = -1* tt.AmpValue + Bottom
            tt.listen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            if count < 641:
                CurrentPoint = [count,LinePlot]
                pygame.draw.line(screen, WHITE, OldPoint, CurrentPoint, 1)
                OldPoint = CurrentPoint
                count += 1;
                print tt.AmpValue
            else:
                count = 0;
                CurrentPoint = [count,LinePlot]
                pygame.draw.line(screen, WHITE, OldPoint, CurrentPoint, 1)
                OldPoint = CurrentPoint
                screen.fill(BLACK)

            pygame.draw.line(screen, WHITE, [0, Bottom], [640,Bottom], 2)
            pygame.draw.line(screen, WHITE, [0, Top], [640,Top], 2)
            pygame.display.update()

    pygame.quit()
    sys.exit()
        

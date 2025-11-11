#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.1post4),
    on May 01, 2025, at 15:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.1post4'
expName = 'Raven'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1920,1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='Z:\\CAMLab-UGrad-write\\WM Precision - SP 2025\\Tasks\\Raven\\Raven_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color='white', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'white'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='On this task, you will have to generate solutions to problems.\n\nOn each trial, you see a 3 x 3 pattern. The bottom-right piece to the pattern will be missing.\n\nYour task is to select from a set of possible options the piece that best completes the pattern.\n\nWe will start with a couple practice items.\n\nClick the mouse to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "practice1" ---
    matrix_5 = visual.ImageStim(
        win=win,
        name='matrix_5', units='pix', 
        image='picA.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 200), draggable=False, size=(540, 360),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ans1_5 = visual.ImageStim(
        win=win,
        name='ans1_5', units='pix', 
        image='picAresp.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, -200), draggable=False, size=(805, 320),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse_6 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_6.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "practice1_ans" ---
    matrix_6 = visual.ImageStim(
        win=win,
        name='matrix_6', units='pix', 
        image='picA.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 320), draggable=False, size=(540, 360),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ans1_6 = visual.ImageStim(
        win=win,
        name='ans1_6', units='pix', 
        image='picAresp.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=True, size=(805, 320),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse_7 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_7.mouseClock = core.Clock()
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Numbers 4, 6, and 7 cannot be the correct pieces, because they only show a single circle.\n\nNumbers 1, 3, and 5 cannot be correct because even though they show multiple circles, they still don\\'t show enough.\n\nFinally, number 2 cannot be correct because it actually shows too many circles.\n\nSo, the correct answer must be 8. Does that make sense?\n\nPlease click the mouse to continue.",
        font='Arial',
        pos=(0, -.30), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "practice2" ---
    matrix_2 = visual.ImageStim(
        win=win,
        name='matrix_2', units='pix', 
        image='picB.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 200), draggable=False, size=(540, 360),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ans1_2 = visual.ImageStim(
        win=win,
        name='ans1_2', units='pix', 
        image='picBresp.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, -200), draggable=False, size=(805, 320),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse_3 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "practice2_ans" ---
    matrix_3 = visual.ImageStim(
        win=win,
        name='matrix_3', units='pix', 
        image='picB.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 320), draggable=False, size=(540, 360),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ans1_3 = visual.ImageStim(
        win=win,
        name='ans1_3', units='pix', 
        image='picBresp.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(805, 320),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse_4 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_4.mouseClock = core.Clock()
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Number 3 was the correct answer because that is the only one that fits the pattern.\n\nDo you have any questions?\n\nPlease click the mouse to continue.',
        font='Arial',
        pos=(0, -.30), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "practice3" ---
    matrix_8 = visual.ImageStim(
        win=win,
        name='matrix_8', units='pix', 
        image='picC.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 200), draggable=False, size=(540, 360),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ans1_8 = visual.ImageStim(
        win=win,
        name='ans1_8', units='pix', 
        image='picCresp.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, -200), draggable=False, size=(805, 320),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse_9 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_9.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "practice3_ans" ---
    matrix_7 = visual.ImageStim(
        win=win,
        name='matrix_7', units='pix', 
        image='picC.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 320), draggable=False, size=(540, 360),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ans1_7 = visual.ImageStim(
        win=win,
        name='ans1_7', units='pix', 
        image='picCresp.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(805, 320),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mouse_8 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_8.mouseClock = core.Clock()
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Number 2 was correct because that is the only one that fits the pattern.\n\nIt allows the crosses to keep getting bigger going across the bottom row, and it allows the crosses to keep getting bigger going down the right-hand column.\n\nDo you have any questions?\n\nPlease click the mouse to continue.',
        font='Arial',
        pos=(0, -.30), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "start_real" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='You will find the problems in this set slowly get more difficult.\n\nIn every problem you should use the same method of working. Look along each row and decide what the missing figure is like.\n\nLook down each column and decide again, and choose the piece you find that is right in both ways.\n\nWhen you have found it, click on the answer using the mouse.\n\nYou have 10 minutes to complete 18 problems. You may not get to all the problems, so complete as many as possible.\n\nYour accuracy is what matters most. Do you have any questions? If so, ask the experimenter now.\n\nIf not, please click the mouse to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse_10 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_10.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial" ---
    matrix = visual.ImageStim(
        win=win,
        name='matrix', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 200), draggable=False, size=(540, 360),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ans1 = visual.ImageStim(
        win=win,
        name='ans1', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-300, -120), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    ans2 = visual.ImageStim(
        win=win,
        name='ans2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, -120), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ans3 = visual.ImageStim(
        win=win,
        name='ans3', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, -120), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    ans4 = visual.ImageStim(
        win=win,
        name='ans4', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(300, -120), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    ans5 = visual.ImageStim(
        win=win,
        name='ans5', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-300, -250), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    ans6 = visual.ImageStim(
        win=win,
        name='ans6', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-100, -250), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    ans7 = visual.ImageStim(
        win=win,
        name='ans7', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(100, -250), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    ans8 = visual.ImageStim(
        win=win,
        name='ans8', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(300, -250), draggable=False, size=(170, 120),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    item_number = visual.TextStim(win=win, name='item_number',
        text='',
        font='Arial',
        pos=(-.3, .3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code
    win.mouseVisible = True
    
    # --- Initialize components for Routine "end_exp" ---
    text = visual.TextStim(win=win, name='text',
        text='That is the end of the experiment!\n\nThis window will close automatically...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[text_2, mouse_2],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    gotValidClick = False  # until a click is received
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        # *mouse_2* updates
        
        # if mouse_2 is starting this frame...
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            # update status
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_2.x', mouse_2.x)
    thisExp.addData('mouse_2.y', mouse_2.y)
    thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
    thisExp.addData('mouse_2.midButton', mouse_2.midButton)
    thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
    thisExp.addData('mouse_2.time', mouse_2.time)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice1" ---
    # create an object to store info about Routine practice1
    practice1 = data.Routine(
        name='practice1',
        components=[matrix_5, ans1_5, mouse_6],
    )
    practice1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_6
    mouse_6.x = []
    mouse_6.y = []
    mouse_6.leftButton = []
    mouse_6.midButton = []
    mouse_6.rightButton = []
    mouse_6.time = []
    mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for practice1
    practice1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice1.tStart = globalClock.getTime(format='float')
    practice1.status = STARTED
    thisExp.addData('practice1.started', practice1.tStart)
    practice1.maxDuration = None
    # keep track of which components have finished
    practice1Components = practice1.components
    for thisComponent in practice1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice1" ---
    practice1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *matrix_5* updates
        
        # if matrix_5 is starting this frame...
        if matrix_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_5.frameNStart = frameN  # exact frame index
            matrix_5.tStart = t  # local t and not account for scr refresh
            matrix_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_5.started')
            # update status
            matrix_5.status = STARTED
            matrix_5.setAutoDraw(True)
        
        # if matrix_5 is active this frame...
        if matrix_5.status == STARTED:
            # update params
            pass
        
        # *ans1_5* updates
        
        # if ans1_5 is starting this frame...
        if ans1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_5.frameNStart = frameN  # exact frame index
            ans1_5.tStart = t  # local t and not account for scr refresh
            ans1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ans1_5.started')
            # update status
            ans1_5.status = STARTED
            ans1_5.setAutoDraw(True)
        
        # if ans1_5 is active this frame...
        if ans1_5.status == STARTED:
            # update params
            pass
        # *mouse_6* updates
        
        # if mouse_6 is starting this frame...
        if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_6.frameNStart = frameN  # exact frame index
            mouse_6.tStart = t  # local t and not account for scr refresh
            mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_6.started', t)
            # update status
            mouse_6.status = STARTED
            mouse_6.mouseClock.reset()
            prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
        if mouse_6.status == STARTED:  # only update if started and not finished!
            buttons = mouse_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_6):
                            gotValidClick = True
                            mouse_6.clicked_name.append(obj.name)
                            mouse_6.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_6.getPos()
                        mouse_6.x.append(x)
                        mouse_6.y.append(y)
                        buttons = mouse_6.getPressed()
                        mouse_6.leftButton.append(buttons[0])
                        mouse_6.midButton.append(buttons[1])
                        mouse_6.rightButton.append(buttons[2])
                        mouse_6.time.append(mouse_6.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice1" ---
    for thisComponent in practice1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice1
    practice1.tStop = globalClock.getTime(format='float')
    practice1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice1.stopped', practice1.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_6.x', mouse_6.x)
    thisExp.addData('mouse_6.y', mouse_6.y)
    thisExp.addData('mouse_6.leftButton', mouse_6.leftButton)
    thisExp.addData('mouse_6.midButton', mouse_6.midButton)
    thisExp.addData('mouse_6.rightButton', mouse_6.rightButton)
    thisExp.addData('mouse_6.time', mouse_6.time)
    thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name)
    thisExp.nextEntry()
    # the Routine "practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice1_ans" ---
    # create an object to store info about Routine practice1_ans
    practice1_ans = data.Routine(
        name='practice1_ans',
        components=[matrix_6, ans1_6, mouse_7, text_4],
    )
    practice1_ans.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_7
    mouse_7.x = []
    mouse_7.y = []
    mouse_7.leftButton = []
    mouse_7.midButton = []
    mouse_7.rightButton = []
    mouse_7.time = []
    mouse_7.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for practice1_ans
    practice1_ans.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice1_ans.tStart = globalClock.getTime(format='float')
    practice1_ans.status = STARTED
    thisExp.addData('practice1_ans.started', practice1_ans.tStart)
    practice1_ans.maxDuration = None
    # keep track of which components have finished
    practice1_ansComponents = practice1_ans.components
    for thisComponent in practice1_ans.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice1_ans" ---
    practice1_ans.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *matrix_6* updates
        
        # if matrix_6 is starting this frame...
        if matrix_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_6.frameNStart = frameN  # exact frame index
            matrix_6.tStart = t  # local t and not account for scr refresh
            matrix_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_6.started')
            # update status
            matrix_6.status = STARTED
            matrix_6.setAutoDraw(True)
        
        # if matrix_6 is active this frame...
        if matrix_6.status == STARTED:
            # update params
            pass
        
        # *ans1_6* updates
        
        # if ans1_6 is starting this frame...
        if ans1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_6.frameNStart = frameN  # exact frame index
            ans1_6.tStart = t  # local t and not account for scr refresh
            ans1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ans1_6.started')
            # update status
            ans1_6.status = STARTED
            ans1_6.setAutoDraw(True)
        
        # if ans1_6 is active this frame...
        if ans1_6.status == STARTED:
            # update params
            pass
        # *mouse_7* updates
        
        # if mouse_7 is starting this frame...
        if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_7.frameNStart = frameN  # exact frame index
            mouse_7.tStart = t  # local t and not account for scr refresh
            mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_7.started', t)
            # update status
            mouse_7.status = STARTED
            mouse_7.mouseClock.reset()
            prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
        if mouse_7.status == STARTED:  # only update if started and not finished!
            buttons = mouse_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_7):
                            gotValidClick = True
                            mouse_7.clicked_name.append(obj.name)
                            mouse_7.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_7.getPos()
                        mouse_7.x.append(x)
                        mouse_7.y.append(y)
                        buttons = mouse_7.getPressed()
                        mouse_7.leftButton.append(buttons[0])
                        mouse_7.midButton.append(buttons[1])
                        mouse_7.rightButton.append(buttons[2])
                        mouse_7.time.append(mouse_7.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice1_ans.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice1_ans.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice1_ans" ---
    for thisComponent in practice1_ans.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice1_ans
    practice1_ans.tStop = globalClock.getTime(format='float')
    practice1_ans.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice1_ans.stopped', practice1_ans.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_7.x', mouse_7.x)
    thisExp.addData('mouse_7.y', mouse_7.y)
    thisExp.addData('mouse_7.leftButton', mouse_7.leftButton)
    thisExp.addData('mouse_7.midButton', mouse_7.midButton)
    thisExp.addData('mouse_7.rightButton', mouse_7.rightButton)
    thisExp.addData('mouse_7.time', mouse_7.time)
    thisExp.addData('mouse_7.clicked_name', mouse_7.clicked_name)
    thisExp.nextEntry()
    # the Routine "practice1_ans" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice2" ---
    # create an object to store info about Routine practice2
    practice2 = data.Routine(
        name='practice2',
        components=[matrix_2, ans1_2, mouse_3],
    )
    practice2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    mouse_3.x = []
    mouse_3.y = []
    mouse_3.leftButton = []
    mouse_3.midButton = []
    mouse_3.rightButton = []
    mouse_3.time = []
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for practice2
    practice2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice2.tStart = globalClock.getTime(format='float')
    practice2.status = STARTED
    thisExp.addData('practice2.started', practice2.tStart)
    practice2.maxDuration = None
    # keep track of which components have finished
    practice2Components = practice2.components
    for thisComponent in practice2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice2" ---
    practice2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *matrix_2* updates
        
        # if matrix_2 is starting this frame...
        if matrix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_2.frameNStart = frameN  # exact frame index
            matrix_2.tStart = t  # local t and not account for scr refresh
            matrix_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_2.started')
            # update status
            matrix_2.status = STARTED
            matrix_2.setAutoDraw(True)
        
        # if matrix_2 is active this frame...
        if matrix_2.status == STARTED:
            # update params
            pass
        
        # *ans1_2* updates
        
        # if ans1_2 is starting this frame...
        if ans1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_2.frameNStart = frameN  # exact frame index
            ans1_2.tStart = t  # local t and not account for scr refresh
            ans1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ans1_2.started')
            # update status
            ans1_2.status = STARTED
            ans1_2.setAutoDraw(True)
        
        # if ans1_2 is active this frame...
        if ans1_2.status == STARTED:
            # update params
            pass
        # *mouse_3* updates
        
        # if mouse_3 is starting this frame...
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            # update status
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_3.getPos()
                        mouse_3.x.append(x)
                        mouse_3.y.append(y)
                        buttons = mouse_3.getPressed()
                        mouse_3.leftButton.append(buttons[0])
                        mouse_3.midButton.append(buttons[1])
                        mouse_3.rightButton.append(buttons[2])
                        mouse_3.time.append(mouse_3.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice2" ---
    for thisComponent in practice2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice2
    practice2.tStop = globalClock.getTime(format='float')
    practice2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice2.stopped', practice2.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_3.x', mouse_3.x)
    thisExp.addData('mouse_3.y', mouse_3.y)
    thisExp.addData('mouse_3.leftButton', mouse_3.leftButton)
    thisExp.addData('mouse_3.midButton', mouse_3.midButton)
    thisExp.addData('mouse_3.rightButton', mouse_3.rightButton)
    thisExp.addData('mouse_3.time', mouse_3.time)
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name)
    thisExp.nextEntry()
    # the Routine "practice2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice2_ans" ---
    # create an object to store info about Routine practice2_ans
    practice2_ans = data.Routine(
        name='practice2_ans',
        components=[matrix_3, ans1_3, mouse_4, text_3],
    )
    practice2_ans.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_4
    mouse_4.x = []
    mouse_4.y = []
    mouse_4.leftButton = []
    mouse_4.midButton = []
    mouse_4.rightButton = []
    mouse_4.time = []
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for practice2_ans
    practice2_ans.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice2_ans.tStart = globalClock.getTime(format='float')
    practice2_ans.status = STARTED
    thisExp.addData('practice2_ans.started', practice2_ans.tStart)
    practice2_ans.maxDuration = None
    # keep track of which components have finished
    practice2_ansComponents = practice2_ans.components
    for thisComponent in practice2_ans.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice2_ans" ---
    practice2_ans.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *matrix_3* updates
        
        # if matrix_3 is starting this frame...
        if matrix_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_3.frameNStart = frameN  # exact frame index
            matrix_3.tStart = t  # local t and not account for scr refresh
            matrix_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_3.started')
            # update status
            matrix_3.status = STARTED
            matrix_3.setAutoDraw(True)
        
        # if matrix_3 is active this frame...
        if matrix_3.status == STARTED:
            # update params
            pass
        
        # *ans1_3* updates
        
        # if ans1_3 is starting this frame...
        if ans1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_3.frameNStart = frameN  # exact frame index
            ans1_3.tStart = t  # local t and not account for scr refresh
            ans1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ans1_3.started')
            # update status
            ans1_3.status = STARTED
            ans1_3.setAutoDraw(True)
        
        # if ans1_3 is active this frame...
        if ans1_3.status == STARTED:
            # update params
            pass
        # *mouse_4* updates
        
        # if mouse_4 is starting this frame...
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_4.started', t)
            # update status
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_4):
                            gotValidClick = True
                            mouse_4.clicked_name.append(obj.name)
                            mouse_4.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_4.getPos()
                        mouse_4.x.append(x)
                        mouse_4.y.append(y)
                        buttons = mouse_4.getPressed()
                        mouse_4.leftButton.append(buttons[0])
                        mouse_4.midButton.append(buttons[1])
                        mouse_4.rightButton.append(buttons[2])
                        mouse_4.time.append(mouse_4.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice2_ans.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice2_ans.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice2_ans" ---
    for thisComponent in practice2_ans.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice2_ans
    practice2_ans.tStop = globalClock.getTime(format='float')
    practice2_ans.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice2_ans.stopped', practice2_ans.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_4.x', mouse_4.x)
    thisExp.addData('mouse_4.y', mouse_4.y)
    thisExp.addData('mouse_4.leftButton', mouse_4.leftButton)
    thisExp.addData('mouse_4.midButton', mouse_4.midButton)
    thisExp.addData('mouse_4.rightButton', mouse_4.rightButton)
    thisExp.addData('mouse_4.time', mouse_4.time)
    thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name)
    thisExp.nextEntry()
    # the Routine "practice2_ans" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice3" ---
    # create an object to store info about Routine practice3
    practice3 = data.Routine(
        name='practice3',
        components=[matrix_8, ans1_8, mouse_9],
    )
    practice3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_9
    mouse_9.x = []
    mouse_9.y = []
    mouse_9.leftButton = []
    mouse_9.midButton = []
    mouse_9.rightButton = []
    mouse_9.time = []
    mouse_9.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for practice3
    practice3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice3.tStart = globalClock.getTime(format='float')
    practice3.status = STARTED
    thisExp.addData('practice3.started', practice3.tStart)
    practice3.maxDuration = None
    # keep track of which components have finished
    practice3Components = practice3.components
    for thisComponent in practice3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice3" ---
    practice3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *matrix_8* updates
        
        # if matrix_8 is starting this frame...
        if matrix_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_8.frameNStart = frameN  # exact frame index
            matrix_8.tStart = t  # local t and not account for scr refresh
            matrix_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_8.started')
            # update status
            matrix_8.status = STARTED
            matrix_8.setAutoDraw(True)
        
        # if matrix_8 is active this frame...
        if matrix_8.status == STARTED:
            # update params
            pass
        
        # *ans1_8* updates
        
        # if ans1_8 is starting this frame...
        if ans1_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_8.frameNStart = frameN  # exact frame index
            ans1_8.tStart = t  # local t and not account for scr refresh
            ans1_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ans1_8.started')
            # update status
            ans1_8.status = STARTED
            ans1_8.setAutoDraw(True)
        
        # if ans1_8 is active this frame...
        if ans1_8.status == STARTED:
            # update params
            pass
        # *mouse_9* updates
        
        # if mouse_9 is starting this frame...
        if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_9.frameNStart = frameN  # exact frame index
            mouse_9.tStart = t  # local t and not account for scr refresh
            mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_9.started', t)
            # update status
            mouse_9.status = STARTED
            mouse_9.mouseClock.reset()
            prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
        if mouse_9.status == STARTED:  # only update if started and not finished!
            buttons = mouse_9.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_9):
                            gotValidClick = True
                            mouse_9.clicked_name.append(obj.name)
                            mouse_9.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_9.getPos()
                        mouse_9.x.append(x)
                        mouse_9.y.append(y)
                        buttons = mouse_9.getPressed()
                        mouse_9.leftButton.append(buttons[0])
                        mouse_9.midButton.append(buttons[1])
                        mouse_9.rightButton.append(buttons[2])
                        mouse_9.time.append(mouse_9.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice3" ---
    for thisComponent in practice3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice3
    practice3.tStop = globalClock.getTime(format='float')
    practice3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice3.stopped', practice3.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_9.x', mouse_9.x)
    thisExp.addData('mouse_9.y', mouse_9.y)
    thisExp.addData('mouse_9.leftButton', mouse_9.leftButton)
    thisExp.addData('mouse_9.midButton', mouse_9.midButton)
    thisExp.addData('mouse_9.rightButton', mouse_9.rightButton)
    thisExp.addData('mouse_9.time', mouse_9.time)
    thisExp.addData('mouse_9.clicked_name', mouse_9.clicked_name)
    thisExp.nextEntry()
    # the Routine "practice3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice3_ans" ---
    # create an object to store info about Routine practice3_ans
    practice3_ans = data.Routine(
        name='practice3_ans',
        components=[matrix_7, ans1_7, mouse_8, text_5],
    )
    practice3_ans.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_8
    mouse_8.x = []
    mouse_8.y = []
    mouse_8.leftButton = []
    mouse_8.midButton = []
    mouse_8.rightButton = []
    mouse_8.time = []
    mouse_8.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for practice3_ans
    practice3_ans.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice3_ans.tStart = globalClock.getTime(format='float')
    practice3_ans.status = STARTED
    thisExp.addData('practice3_ans.started', practice3_ans.tStart)
    practice3_ans.maxDuration = None
    # keep track of which components have finished
    practice3_ansComponents = practice3_ans.components
    for thisComponent in practice3_ans.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice3_ans" ---
    practice3_ans.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *matrix_7* updates
        
        # if matrix_7 is starting this frame...
        if matrix_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_7.frameNStart = frameN  # exact frame index
            matrix_7.tStart = t  # local t and not account for scr refresh
            matrix_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_7.started')
            # update status
            matrix_7.status = STARTED
            matrix_7.setAutoDraw(True)
        
        # if matrix_7 is active this frame...
        if matrix_7.status == STARTED:
            # update params
            pass
        
        # *ans1_7* updates
        
        # if ans1_7 is starting this frame...
        if ans1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_7.frameNStart = frameN  # exact frame index
            ans1_7.tStart = t  # local t and not account for scr refresh
            ans1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ans1_7.started')
            # update status
            ans1_7.status = STARTED
            ans1_7.setAutoDraw(True)
        
        # if ans1_7 is active this frame...
        if ans1_7.status == STARTED:
            # update params
            pass
        # *mouse_8* updates
        
        # if mouse_8 is starting this frame...
        if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_8.frameNStart = frameN  # exact frame index
            mouse_8.tStart = t  # local t and not account for scr refresh
            mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_8.started', t)
            # update status
            mouse_8.status = STARTED
            mouse_8.mouseClock.reset()
            prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
        if mouse_8.status == STARTED:  # only update if started and not finished!
            buttons = mouse_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_8):
                            gotValidClick = True
                            mouse_8.clicked_name.append(obj.name)
                            mouse_8.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_8.getPos()
                        mouse_8.x.append(x)
                        mouse_8.y.append(y)
                        buttons = mouse_8.getPressed()
                        mouse_8.leftButton.append(buttons[0])
                        mouse_8.midButton.append(buttons[1])
                        mouse_8.rightButton.append(buttons[2])
                        mouse_8.time.append(mouse_8.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice3_ans.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice3_ans.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice3_ans" ---
    for thisComponent in practice3_ans.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice3_ans
    practice3_ans.tStop = globalClock.getTime(format='float')
    practice3_ans.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice3_ans.stopped', practice3_ans.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_8.x', mouse_8.x)
    thisExp.addData('mouse_8.y', mouse_8.y)
    thisExp.addData('mouse_8.leftButton', mouse_8.leftButton)
    thisExp.addData('mouse_8.midButton', mouse_8.midButton)
    thisExp.addData('mouse_8.rightButton', mouse_8.rightButton)
    thisExp.addData('mouse_8.time', mouse_8.time)
    thisExp.addData('mouse_8.clicked_name', mouse_8.clicked_name)
    thisExp.nextEntry()
    # the Routine "practice3_ans" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "start_real" ---
    # create an object to store info about Routine start_real
    start_real = data.Routine(
        name='start_real',
        components=[text_6, mouse_10],
    )
    start_real.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_10
    mouse_10.x = []
    mouse_10.y = []
    mouse_10.leftButton = []
    mouse_10.midButton = []
    mouse_10.rightButton = []
    mouse_10.time = []
    gotValidClick = False  # until a click is received
    # store start times for start_real
    start_real.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_real.tStart = globalClock.getTime(format='float')
    start_real.status = STARTED
    thisExp.addData('start_real.started', start_real.tStart)
    start_real.maxDuration = None
    # keep track of which components have finished
    start_realComponents = start_real.components
    for thisComponent in start_real.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_real" ---
    start_real.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        # *mouse_10* updates
        
        # if mouse_10 is starting this frame...
        if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_10.started', t)
            # update status
            mouse_10.status = STARTED
            mouse_10.mouseClock.reset()
            prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
        if mouse_10.status == STARTED:  # only update if started and not finished!
            buttons = mouse_10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = mouse_10.getPos()
                    mouse_10.x.append(x)
                    mouse_10.y.append(y)
                    buttons = mouse_10.getPressed()
                    mouse_10.leftButton.append(buttons[0])
                    mouse_10.midButton.append(buttons[1])
                    mouse_10.rightButton.append(buttons[2])
                    mouse_10.time.append(mouse_10.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start_real.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_real.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_real" ---
    for thisComponent in start_real.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_real
    start_real.tStop = globalClock.getTime(format='float')
    start_real.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_real.stopped', start_real.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_10.x', mouse_10.x)
    thisExp.addData('mouse_10.y', mouse_10.y)
    thisExp.addData('mouse_10.leftButton', mouse_10.leftButton)
    thisExp.addData('mouse_10.midButton', mouse_10.midButton)
    thisExp.addData('mouse_10.rightButton', mouse_10.rightButton)
    thisExp.addData('mouse_10.time', mouse_10.time)
    # Run 'End Routine' code from code_2
    loop_timer = core.Clock()
    thisExp.nextEntry()
    # the Routine "start_real" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('raven_trialList.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[matrix, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, item_number, mouse],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        matrix.setImage(matrix_image)
        ans1.setImage(ans1_image)
        ans2.setImage(ans2_image)
        ans3.setImage(ans3_image)
        ans4.setImage(ans4_image)
        ans5.setImage(ans5_image)
        ans6.setImage(ans6_image)
        ans7.setImage(ans7_image)
        ans8.setImage(ans8_image)
        item_number.setText(item_n)
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *matrix* updates
            
            # if matrix is starting this frame...
            if matrix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                matrix.frameNStart = frameN  # exact frame index
                matrix.tStart = t  # local t and not account for scr refresh
                matrix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(matrix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'matrix.started')
                # update status
                matrix.status = STARTED
                matrix.setAutoDraw(True)
            
            # if matrix is active this frame...
            if matrix.status == STARTED:
                # update params
                pass
            
            # *ans1* updates
            
            # if ans1 is starting this frame...
            if ans1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans1.frameNStart = frameN  # exact frame index
                ans1.tStart = t  # local t and not account for scr refresh
                ans1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans1.started')
                # update status
                ans1.status = STARTED
                ans1.setAutoDraw(True)
            
            # if ans1 is active this frame...
            if ans1.status == STARTED:
                # update params
                pass
            
            # *ans2* updates
            
            # if ans2 is starting this frame...
            if ans2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans2.frameNStart = frameN  # exact frame index
                ans2.tStart = t  # local t and not account for scr refresh
                ans2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans2.started')
                # update status
                ans2.status = STARTED
                ans2.setAutoDraw(True)
            
            # if ans2 is active this frame...
            if ans2.status == STARTED:
                # update params
                pass
            
            # *ans3* updates
            
            # if ans3 is starting this frame...
            if ans3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans3.frameNStart = frameN  # exact frame index
                ans3.tStart = t  # local t and not account for scr refresh
                ans3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans3.started')
                # update status
                ans3.status = STARTED
                ans3.setAutoDraw(True)
            
            # if ans3 is active this frame...
            if ans3.status == STARTED:
                # update params
                pass
            
            # *ans4* updates
            
            # if ans4 is starting this frame...
            if ans4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans4.frameNStart = frameN  # exact frame index
                ans4.tStart = t  # local t and not account for scr refresh
                ans4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans4.started')
                # update status
                ans4.status = STARTED
                ans4.setAutoDraw(True)
            
            # if ans4 is active this frame...
            if ans4.status == STARTED:
                # update params
                pass
            
            # *ans5* updates
            
            # if ans5 is starting this frame...
            if ans5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans5.frameNStart = frameN  # exact frame index
                ans5.tStart = t  # local t and not account for scr refresh
                ans5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans5.started')
                # update status
                ans5.status = STARTED
                ans5.setAutoDraw(True)
            
            # if ans5 is active this frame...
            if ans5.status == STARTED:
                # update params
                pass
            
            # *ans6* updates
            
            # if ans6 is starting this frame...
            if ans6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans6.frameNStart = frameN  # exact frame index
                ans6.tStart = t  # local t and not account for scr refresh
                ans6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans6.started')
                # update status
                ans6.status = STARTED
                ans6.setAutoDraw(True)
            
            # if ans6 is active this frame...
            if ans6.status == STARTED:
                # update params
                pass
            
            # *ans7* updates
            
            # if ans7 is starting this frame...
            if ans7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans7.frameNStart = frameN  # exact frame index
                ans7.tStart = t  # local t and not account for scr refresh
                ans7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans7.started')
                # update status
                ans7.status = STARTED
                ans7.setAutoDraw(True)
            
            # if ans7 is active this frame...
            if ans7.status == STARTED:
                # update params
                pass
            
            # *ans8* updates
            
            # if ans8 is starting this frame...
            if ans8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans8.frameNStart = frameN  # exact frame index
                ans8.tStart = t  # local t and not account for scr refresh
                ans8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans8.started')
                # update status
                ans8.status = STARTED
                ans8.setAutoDraw(True)
            
            # if ans8 is active this frame...
            if ans8.status == STARTED:
                # update params
                pass
            
            # *item_number* updates
            
            # if item_number is starting this frame...
            if item_number.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                item_number.frameNStart = frameN  # exact frame index
                item_number.tStart = t  # local t and not account for scr refresh
                item_number.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item_number, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item_number.started')
                # update status
                item_number.status = STARTED
                item_number.setAutoDraw(True)
            
            # if item_number is active this frame...
            if item_number.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse.getPos()
                            mouse.x.append(x)
                            mouse.y.append(y)
                            buttons = mouse.getPressed()
                            mouse.leftButton.append(buttons[0])
                            mouse.midButton.append(buttons[1])
                            mouse.rightButton.append(buttons[2])
                            mouse.time.append(mouse.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            # Run 'Each Frame' code from code
            if loop_timer.getTime() > 600:
                continueRoutine = False
                trials.finished = True
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # store data for trials (TrialHandler)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.leftButton', mouse.leftButton)
        trials.addData('mouse.midButton', mouse.midButton)
        trials.addData('mouse.rightButton', mouse.rightButton)
        trials.addData('mouse.time', mouse.time)
        trials.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_exp" ---
    # create an object to store info about Routine end_exp
    end_exp = data.Routine(
        name='end_exp',
        components=[text],
    )
    end_exp.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end_exp
    end_exp.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_exp.tStart = globalClock.getTime(format='float')
    end_exp.status = STARTED
    thisExp.addData('end_exp.started', end_exp.tStart)
    end_exp.maxDuration = None
    # keep track of which components have finished
    end_expComponents = end_exp.components
    for thisComponent in end_exp.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_exp" ---
    end_exp.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.tStopRefresh = tThisFlipGlobal  # on global time
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end_exp.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_exp.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_exp" ---
    for thisComponent in end_exp.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_exp
    end_exp.tStop = globalClock.getTime(format='float')
    end_exp.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end_exp.stopped', end_exp.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end_exp.maxDurationReached:
        routineTimer.addTime(-end_exp.maxDuration)
    elif end_exp.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

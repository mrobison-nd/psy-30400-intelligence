/************** 
 * Raven *
 **************/


// store info about the experiment session:
let expName = 'Raven';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(practice1RoutineBegin());
flowScheduler.add(practice1RoutineEachFrame());
flowScheduler.add(practice1RoutineEnd());
flowScheduler.add(practice1_ansRoutineBegin());
flowScheduler.add(practice1_ansRoutineEachFrame());
flowScheduler.add(practice1_ansRoutineEnd());
flowScheduler.add(practice2RoutineBegin());
flowScheduler.add(practice2RoutineEachFrame());
flowScheduler.add(practice2RoutineEnd());
flowScheduler.add(practice2_ansRoutineBegin());
flowScheduler.add(practice2_ansRoutineEachFrame());
flowScheduler.add(practice2_ansRoutineEnd());
flowScheduler.add(practice3RoutineBegin());
flowScheduler.add(practice3RoutineEachFrame());
flowScheduler.add(practice3RoutineEnd());
flowScheduler.add(practice3_ansRoutineBegin());
flowScheduler.add(practice3_ansRoutineEachFrame());
flowScheduler.add(practice3_ansRoutineEnd());
flowScheduler.add(start_realRoutineBegin());
flowScheduler.add(start_realRoutineEachFrame());
flowScheduler.add(start_realRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(end_expRoutineBegin());
flowScheduler.add(end_expRoutineEachFrame());
flowScheduler.add(end_expRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'raven_trialList.xlsx', 'path': 'raven_trialList.xlsx'},
    {'name': 'pic1.bmp', 'path': 'pic1.bmp'},
    {'name': '1a.bmp', 'path': '1a.bmp'},
    {'name': '1b.bmp', 'path': '1b.bmp'},
    {'name': '1c.bmp', 'path': '1c.bmp'},
    {'name': '1d.bmp', 'path': '1d.bmp'},
    {'name': '1e.bmp', 'path': '1e.bmp'},
    {'name': '1f.bmp', 'path': '1f.bmp'},
    {'name': '1g.bmp', 'path': '1g.bmp'},
    {'name': '1h.bmp', 'path': '1h.bmp'},
    {'name': 'pic3.bmp', 'path': 'pic3.bmp'},
    {'name': '3a.bmp', 'path': '3a.bmp'},
    {'name': '3b.bmp', 'path': '3b.bmp'},
    {'name': '3c.bmp', 'path': '3c.bmp'},
    {'name': '3d.bmp', 'path': '3d.bmp'},
    {'name': '3e.bmp', 'path': '3e.bmp'},
    {'name': '3f.bmp', 'path': '3f.bmp'},
    {'name': '3g.bmp', 'path': '3g.bmp'},
    {'name': '3h.bmp', 'path': '3h.bmp'},
    {'name': 'pic5.bmp', 'path': 'pic5.bmp'},
    {'name': '5a.bmp', 'path': '5a.bmp'},
    {'name': '5b.bmp', 'path': '5b.bmp'},
    {'name': '5c.bmp', 'path': '5c.bmp'},
    {'name': '5d.bmp', 'path': '5d.bmp'},
    {'name': '5e.bmp', 'path': '5e.bmp'},
    {'name': '5f.bmp', 'path': '5f.bmp'},
    {'name': '5g.bmp', 'path': '5g.bmp'},
    {'name': '5h.bmp', 'path': '5h.bmp'},
    {'name': 'pic7.bmp', 'path': 'pic7.bmp'},
    {'name': '7a.bmp', 'path': '7a.bmp'},
    {'name': '7b.bmp', 'path': '7b.bmp'},
    {'name': '7c.bmp', 'path': '7c.bmp'},
    {'name': '7d.bmp', 'path': '7d.bmp'},
    {'name': '7e.bmp', 'path': '7e.bmp'},
    {'name': '7f.bmp', 'path': '7f.bmp'},
    {'name': '7g.bmp', 'path': '7g.bmp'},
    {'name': '7h.bmp', 'path': '7h.bmp'},
    {'name': 'pic9.bmp', 'path': 'pic9.bmp'},
    {'name': '9a.bmp', 'path': '9a.bmp'},
    {'name': '9b.bmp', 'path': '9b.bmp'},
    {'name': '9c.bmp', 'path': '9c.bmp'},
    {'name': '9d.bmp', 'path': '9d.bmp'},
    {'name': '9e.bmp', 'path': '9e.bmp'},
    {'name': '9f.bmp', 'path': '9f.bmp'},
    {'name': '9g.bmp', 'path': '9g.bmp'},
    {'name': '9h.bmp', 'path': '9h.bmp'},
    {'name': 'pic11.bmp', 'path': 'pic11.bmp'},
    {'name': '11a.bmp', 'path': '11a.bmp'},
    {'name': '11b.bmp', 'path': '11b.bmp'},
    {'name': '11c.bmp', 'path': '11c.bmp'},
    {'name': '11d.bmp', 'path': '11d.bmp'},
    {'name': '11e.bmp', 'path': '11e.bmp'},
    {'name': '11f.bmp', 'path': '11f.bmp'},
    {'name': '11g.bmp', 'path': '11g.bmp'},
    {'name': '11h.bmp', 'path': '11h.bmp'},
    {'name': 'pic13.bmp', 'path': 'pic13.bmp'},
    {'name': '13a.bmp', 'path': '13a.bmp'},
    {'name': '13b.bmp', 'path': '13b.bmp'},
    {'name': '13c.bmp', 'path': '13c.bmp'},
    {'name': '13d.bmp', 'path': '13d.bmp'},
    {'name': '13e.bmp', 'path': '13e.bmp'},
    {'name': '13f.bmp', 'path': '13f.bmp'},
    {'name': '13g.bmp', 'path': '13g.bmp'},
    {'name': '13h.bmp', 'path': '13h.bmp'},
    {'name': 'pic15.bmp', 'path': 'pic15.bmp'},
    {'name': '15a.bmp', 'path': '15a.bmp'},
    {'name': '15b.bmp', 'path': '15b.bmp'},
    {'name': '15c.bmp', 'path': '15c.bmp'},
    {'name': '15d.bmp', 'path': '15d.bmp'},
    {'name': '15e.bmp', 'path': '15e.bmp'},
    {'name': '15f.bmp', 'path': '15f.bmp'},
    {'name': '15g.bmp', 'path': '15g.bmp'},
    {'name': '15h.bmp', 'path': '15h.bmp'},
    {'name': 'pic17.bmp', 'path': 'pic17.bmp'},
    {'name': '17a.bmp', 'path': '17a.bmp'},
    {'name': '17b.bmp', 'path': '17b.bmp'},
    {'name': '17c.bmp', 'path': '17c.bmp'},
    {'name': '17d.bmp', 'path': '17d.bmp'},
    {'name': '17e.bmp', 'path': '17e.bmp'},
    {'name': '17f.bmp', 'path': '17f.bmp'},
    {'name': '17g.bmp', 'path': '17g.bmp'},
    {'name': '17h.bmp', 'path': '17h.bmp'},
    {'name': 'pic19.bmp', 'path': 'pic19.bmp'},
    {'name': '19a.bmp', 'path': '19a.bmp'},
    {'name': '19b.bmp', 'path': '19b.bmp'},
    {'name': '19c.bmp', 'path': '19c.bmp'},
    {'name': '19d.bmp', 'path': '19d.bmp'},
    {'name': '19e.bmp', 'path': '19e.bmp'},
    {'name': '19f.bmp', 'path': '19f.bmp'},
    {'name': '19g.bmp', 'path': '19g.bmp'},
    {'name': '19h.bmp', 'path': '19h.bmp'},
    {'name': 'pic21.bmp', 'path': 'pic21.bmp'},
    {'name': '21a.bmp', 'path': '21a.bmp'},
    {'name': '21b.bmp', 'path': '21b.bmp'},
    {'name': '21c.bmp', 'path': '21c.bmp'},
    {'name': '21d.bmp', 'path': '21d.bmp'},
    {'name': '21e.bmp', 'path': '21e.bmp'},
    {'name': '21f.bmp', 'path': '21f.bmp'},
    {'name': '21g.bmp', 'path': '21g.bmp'},
    {'name': '21h.bmp', 'path': '21h.bmp'},
    {'name': 'pic23.bmp', 'path': 'pic23.bmp'},
    {'name': '23a.bmp', 'path': '23a.bmp'},
    {'name': '23b.bmp', 'path': '23b.bmp'},
    {'name': '23c.bmp', 'path': '23c.bmp'},
    {'name': '23d.bmp', 'path': '23d.bmp'},
    {'name': '23e.bmp', 'path': '23e.bmp'},
    {'name': '23f.bmp', 'path': '23f.bmp'},
    {'name': '23g.bmp', 'path': '23g.bmp'},
    {'name': '23h.bmp', 'path': '23h.bmp'},
    {'name': 'pic25.bmp', 'path': 'pic25.bmp'},
    {'name': '25a.bmp', 'path': '25a.bmp'},
    {'name': '25b.bmp', 'path': '25b.bmp'},
    {'name': '25c.bmp', 'path': '25c.bmp'},
    {'name': '25d.bmp', 'path': '25d.bmp'},
    {'name': '25e.bmp', 'path': '25e.bmp'},
    {'name': '25f.bmp', 'path': '25f.bmp'},
    {'name': '25g.bmp', 'path': '25g.bmp'},
    {'name': '25h.bmp', 'path': '25h.bmp'},
    {'name': 'pic27.bmp', 'path': 'pic27.bmp'},
    {'name': '27a.bmp', 'path': '27a.bmp'},
    {'name': '27b.bmp', 'path': '27b.bmp'},
    {'name': '27c.bmp', 'path': '27c.bmp'},
    {'name': '27d.bmp', 'path': '27d.bmp'},
    {'name': '27e.bmp', 'path': '27e.bmp'},
    {'name': '27f.bmp', 'path': '27f.bmp'},
    {'name': '27g.bmp', 'path': '27g.bmp'},
    {'name': '27h.bmp', 'path': '27h.bmp'},
    {'name': 'pic29.bmp', 'path': 'pic29.bmp'},
    {'name': '29a.bmp', 'path': '29a.bmp'},
    {'name': '29b.bmp', 'path': '29b.bmp'},
    {'name': '29c.bmp', 'path': '29c.bmp'},
    {'name': '29d.bmp', 'path': '29d.bmp'},
    {'name': '29e.bmp', 'path': '29e.bmp'},
    {'name': '29f.bmp', 'path': '29f.bmp'},
    {'name': '29g.bmp', 'path': '29g.bmp'},
    {'name': '29h.bmp', 'path': '29h.bmp'},
    {'name': 'pic31.bmp', 'path': 'pic31.bmp'},
    {'name': '31a.bmp', 'path': '31a.bmp'},
    {'name': '31b.bmp', 'path': '31b.bmp'},
    {'name': '31c.bmp', 'path': '31c.bmp'},
    {'name': '31d.bmp', 'path': '31d.bmp'},
    {'name': '31e.bmp', 'path': '31e.bmp'},
    {'name': '31f.bmp', 'path': '31f.bmp'},
    {'name': '31g.bmp', 'path': '31g.bmp'},
    {'name': '31h.bmp', 'path': '31h.bmp'},
    {'name': 'pic33.bmp', 'path': 'pic33.bmp'},
    {'name': '33a.bmp', 'path': '33a.bmp'},
    {'name': '33b.bmp', 'path': '33b.bmp'},
    {'name': '33c.bmp', 'path': '33c.bmp'},
    {'name': '33d.bmp', 'path': '33d.bmp'},
    {'name': '33e.bmp', 'path': '33e.bmp'},
    {'name': '33f.bmp', 'path': '33f.bmp'},
    {'name': '33g.bmp', 'path': '33g.bmp'},
    {'name': '33h.bmp', 'path': '33h.bmp'},
    {'name': 'pic35.bmp', 'path': 'pic35.bmp'},
    {'name': '35a.bmp', 'path': '35a.bmp'},
    {'name': '35b.bmp', 'path': '35b.bmp'},
    {'name': '35c.bmp', 'path': '35c.bmp'},
    {'name': '35d.bmp', 'path': '35d.bmp'},
    {'name': '35e.bmp', 'path': '35e.bmp'},
    {'name': '35f.bmp', 'path': '35f.bmp'},
    {'name': '35g.bmp', 'path': '35g.bmp'},
    {'name': '35h.bmp', 'path': '35h.bmp'},
    {'name': 'picA.bmp', 'path': 'picA.bmp'},
    {'name': 'picAresp.bmp', 'path': 'picAresp.bmp'},
    {'name': 'picB.bmp', 'path': 'picB.bmp'},
    {'name': 'picBresp.bmp', 'path': 'picBresp.bmp'},
    {'name': 'picC.bmp', 'path': 'picC.bmp'},
    {'name': 'picCresp.bmp', 'path': 'picCresp.bmp'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.1post4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var text_2;
var mouse_2;
var practice1Clock;
var matrix_5;
var ans1_5;
var mouse_6;
var practice1_ansClock;
var matrix_6;
var ans1_6;
var mouse_7;
var text_4;
var practice2Clock;
var matrix_2;
var ans1_2;
var mouse_3;
var practice2_ansClock;
var matrix_3;
var ans1_3;
var mouse_4;
var text_3;
var practice3Clock;
var matrix_8;
var ans1_8;
var mouse_9;
var practice3_ansClock;
var matrix_7;
var ans1_7;
var mouse_8;
var text_5;
var start_realClock;
var text_6;
var mouse_10;
var trialClock;
var matrix;
var ans1;
var ans2;
var ans3;
var ans4;
var ans5;
var ans6;
var ans7;
var ans8;
var item_number;
var mouse;
var end_expClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'On this task, you will have to generate solutions to problems.\n\nOn each trial, you see a 3 x 3 pattern. The bottom-right piece to the pattern will be missing.\n\nYour task is to select from a set of possible options the piece that best completes the pattern.\n\nWe will start with a couple practice items.\n\nClick the mouse to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "practice1"
  practice1Clock = new util.Clock();
  matrix_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'matrix_5', units : 'pix', 
    image : 'picA.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 200], 
    draggable: false,
    size : [540, 360],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ans1_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans1_5', units : 'pix', 
    image : 'picAresp.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 200)], 
    draggable: false,
    size : [805, 320],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mouse_6 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_6.mouseClock = new util.Clock();
  // Initialize components for Routine "practice1_ans"
  practice1_ansClock = new util.Clock();
  matrix_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'matrix_6', units : 'pix', 
    image : 'picA.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 320], 
    draggable: false,
    size : [540, 360],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ans1_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans1_6', units : 'pix', 
    image : 'picAresp.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: true,
    size : [805, 320],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mouse_7 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_7.mouseClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: "Numbers 4, 6, and 7 cannot be the correct pieces, because they only show a single circle.\n\nNumbers 1, 3, and 5 cannot be correct because even though they show multiple circles, they still don\\'t show enough.\n\nFinally, number 2 cannot be correct because it actually shows too many circles.\n\nSo, the correct answer must be 8. Does that make sense?\n\nPlease click the mouse to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "practice2"
  practice2Clock = new util.Clock();
  matrix_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'matrix_2', units : 'pix', 
    image : 'picB.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 200], 
    draggable: false,
    size : [540, 360],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ans1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans1_2', units : 'pix', 
    image : 'picBresp.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 200)], 
    draggable: false,
    size : [805, 320],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "practice2_ans"
  practice2_ansClock = new util.Clock();
  matrix_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'matrix_3', units : 'pix', 
    image : 'picB.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 320], 
    draggable: false,
    size : [540, 360],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ans1_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans1_3', units : 'pix', 
    image : 'picBresp.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [805, 320],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mouse_4 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_4.mouseClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Number 3 was the correct answer because that is the only one that fits the pattern.\n\nDo you have any questions?\n\nPlease click the mouse to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "practice3"
  practice3Clock = new util.Clock();
  matrix_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'matrix_8', units : 'pix', 
    image : 'picC.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 200], 
    draggable: false,
    size : [540, 360],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ans1_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans1_8', units : 'pix', 
    image : 'picCresp.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 200)], 
    draggable: false,
    size : [805, 320],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mouse_9 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_9.mouseClock = new util.Clock();
  // Initialize components for Routine "practice3_ans"
  practice3_ansClock = new util.Clock();
  matrix_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'matrix_7', units : 'pix', 
    image : 'picC.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 320], 
    draggable: false,
    size : [540, 360],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ans1_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans1_7', units : 'pix', 
    image : 'picCresp.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [805, 320],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mouse_8 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_8.mouseClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Number 2 was correct because that is the only one that fits the pattern.\n\nIt allows the crosses to keep getting bigger going across the bottom row, and it allows the crosses to keep getting bigger going down the right-hand column.\n\nDo you have any questions?\n\nPlease click the mouse to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "start_real"
  start_realClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'You will find the problems in this set slowly get more difficult.\n\nIn every problem you should use the same method of working. Look along each row and decide what the missing figure is like.\n\nLook down each column and decide again, and choose the piece you find that is right in both ways.\n\nWhen you have found it, click on the answer using the mouse.\n\nYou have 10 minutes to complete 18 problems. You may not get to all the problems, so complete as many as possible.\n\nYour accuracy is what matters most. Do you have any questions? If so, ask the experimenter now.\n\nIf not, please click the mouse to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  mouse_10 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_10.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  matrix = new visual.ImageStim({
    win : psychoJS.window,
    name : 'matrix', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 200], 
    draggable: false,
    size : [540, 360],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ans1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans1', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 300), (- 120)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  ans2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 100), (- 120)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  ans3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans3', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [100, (- 120)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  ans4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans4', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [300, (- 120)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  ans5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans5', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 300), (- 250)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  ans6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans6', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 100), (- 250)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  ans7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans7', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [100, (- 250)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  ans8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ans8', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [300, (- 250)], 
    draggable: false,
    size : [170, 120],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  item_number = new visual.TextStim({
    win: psychoJS.window,
    name: 'item_number',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), 1.0]),  opacity: undefined,
    depth: -9.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  psychoJS.window.mouseVisible = true;
  
  // Initialize components for Routine "end_exp"
  end_expClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'That is the end of the experiment!\n\nThis window will close automatically...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var welcomeMaxDurationReached;
var gotValidClick;
var welcomeMaxDuration;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    // current position of the mouse:
    mouse_2.x = [];
    mouse_2.y = [];
    mouse_2.leftButton = [];
    mouse_2.midButton = [];
    mouse_2.rightButton = [];
    mouse_2.time = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    welcomeMaxDuration = null
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(text_2);
    welcomeComponents.push(mouse_2);
    
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_2.getPos();
          mouse_2.x.push(_mouseXYs[0]);
          mouse_2.y.push(_mouseXYs[1]);
          mouse_2.leftButton.push(_mouseButtons[0]);
          mouse_2.midButton.push(_mouseButtons[1]);
          mouse_2.rightButton.push(_mouseButtons[2]);
          mouse_2.time.push(mouse_2.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_2.x', mouse_2.x);
    psychoJS.experiment.addData('mouse_2.y', mouse_2.y);
    psychoJS.experiment.addData('mouse_2.leftButton', mouse_2.leftButton);
    psychoJS.experiment.addData('mouse_2.midButton', mouse_2.midButton);
    psychoJS.experiment.addData('mouse_2.rightButton', mouse_2.rightButton);
    psychoJS.experiment.addData('mouse_2.time', mouse_2.time);
    
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice1MaxDurationReached;
var practice1MaxDuration;
var practice1Components;
function practice1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice1' ---
    t = 0;
    practice1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice1MaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_6
    // current position of the mouse:
    mouse_6.x = [];
    mouse_6.y = [];
    mouse_6.leftButton = [];
    mouse_6.midButton = [];
    mouse_6.rightButton = [];
    mouse_6.time = [];
    mouse_6.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('practice1.started', globalClock.getTime());
    practice1MaxDuration = null
    // keep track of which components have finished
    practice1Components = [];
    practice1Components.push(matrix_5);
    practice1Components.push(ans1_5);
    practice1Components.push(mouse_6);
    
    practice1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice1' ---
    // get current time
    t = practice1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *matrix_5* updates
    if (t >= 0.0 && matrix_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      matrix_5.tStart = t;  // (not accounting for frame time here)
      matrix_5.frameNStart = frameN;  // exact frame index
      
      matrix_5.setAutoDraw(true);
    }
    
    
    // *ans1_5* updates
    if (t >= 0.0 && ans1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1_5.tStart = t;  // (not accounting for frame time here)
      ans1_5.frameNStart = frameN;  // exact frame index
      
      ans1_5.setAutoDraw(true);
    }
    
    // *mouse_6* updates
    if (t >= 0.0 && mouse_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_6.tStart = t;  // (not accounting for frame time here)
      mouse_6.frameNStart = frameN;  // exact frame index
      
      mouse_6.status = PsychoJS.Status.STARTED;
      mouse_6.mouseClock.reset();
      prevButtonState = mouse_6.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_6.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_6.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_6.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_6.clickableObjects)) {
              mouse_6.clickableObjects = [mouse_6.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_6.clickableObjects) {
              if (obj.contains(mouse_6)) {
                  gotValidClick = true;
                  mouse_6.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_6.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_6.clickableObjects)) {
              mouse_6.clickableObjects = [mouse_6.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_6.clickableObjects) {
              if (obj.contains(mouse_6)) {
                  gotValidClick = true;
                  mouse_6.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_6.getPos();
            mouse_6.x.push(_mouseXYs[0]);
            mouse_6.y.push(_mouseXYs[1]);
            mouse_6.leftButton.push(_mouseButtons[0]);
            mouse_6.midButton.push(_mouseButtons[1]);
            mouse_6.rightButton.push(_mouseButtons[2]);
            mouse_6.time.push(mouse_6.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice1' ---
    practice1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice1.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_6.x', mouse_6.x);
    psychoJS.experiment.addData('mouse_6.y', mouse_6.y);
    psychoJS.experiment.addData('mouse_6.leftButton', mouse_6.leftButton);
    psychoJS.experiment.addData('mouse_6.midButton', mouse_6.midButton);
    psychoJS.experiment.addData('mouse_6.rightButton', mouse_6.rightButton);
    psychoJS.experiment.addData('mouse_6.time', mouse_6.time);
    psychoJS.experiment.addData('mouse_6.clicked_name', mouse_6.clicked_name);
    
    // the Routine "practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice1_ansMaxDurationReached;
var practice1_ansMaxDuration;
var practice1_ansComponents;
function practice1_ansRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice1_ans' ---
    t = 0;
    practice1_ansClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice1_ansMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_7
    // current position of the mouse:
    mouse_7.x = [];
    mouse_7.y = [];
    mouse_7.leftButton = [];
    mouse_7.midButton = [];
    mouse_7.rightButton = [];
    mouse_7.time = [];
    mouse_7.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('practice1_ans.started', globalClock.getTime());
    practice1_ansMaxDuration = null
    // keep track of which components have finished
    practice1_ansComponents = [];
    practice1_ansComponents.push(matrix_6);
    practice1_ansComponents.push(ans1_6);
    practice1_ansComponents.push(mouse_7);
    practice1_ansComponents.push(text_4);
    
    practice1_ansComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice1_ansRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice1_ans' ---
    // get current time
    t = practice1_ansClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *matrix_6* updates
    if (t >= 0.0 && matrix_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      matrix_6.tStart = t;  // (not accounting for frame time here)
      matrix_6.frameNStart = frameN;  // exact frame index
      
      matrix_6.setAutoDraw(true);
    }
    
    
    // *ans1_6* updates
    if (t >= 0.0 && ans1_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1_6.tStart = t;  // (not accounting for frame time here)
      ans1_6.frameNStart = frameN;  // exact frame index
      
      ans1_6.setAutoDraw(true);
    }
    
    // *mouse_7* updates
    if (t >= 0.0 && mouse_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_7.tStart = t;  // (not accounting for frame time here)
      mouse_7.frameNStart = frameN;  // exact frame index
      
      mouse_7.status = PsychoJS.Status.STARTED;
      mouse_7.mouseClock.reset();
      prevButtonState = mouse_7.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_7.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_7.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_7.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_7.clickableObjects)) {
              mouse_7.clickableObjects = [mouse_7.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_7.clickableObjects) {
              if (obj.contains(mouse_7)) {
                  gotValidClick = true;
                  mouse_7.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_7.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_7.clickableObjects)) {
              mouse_7.clickableObjects = [mouse_7.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_7.clickableObjects) {
              if (obj.contains(mouse_7)) {
                  gotValidClick = true;
                  mouse_7.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_7.getPos();
            mouse_7.x.push(_mouseXYs[0]);
            mouse_7.y.push(_mouseXYs[1]);
            mouse_7.leftButton.push(_mouseButtons[0]);
            mouse_7.midButton.push(_mouseButtons[1]);
            mouse_7.rightButton.push(_mouseButtons[2]);
            mouse_7.time.push(mouse_7.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice1_ansComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice1_ansRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice1_ans' ---
    practice1_ansComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice1_ans.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_7.x', mouse_7.x);
    psychoJS.experiment.addData('mouse_7.y', mouse_7.y);
    psychoJS.experiment.addData('mouse_7.leftButton', mouse_7.leftButton);
    psychoJS.experiment.addData('mouse_7.midButton', mouse_7.midButton);
    psychoJS.experiment.addData('mouse_7.rightButton', mouse_7.rightButton);
    psychoJS.experiment.addData('mouse_7.time', mouse_7.time);
    psychoJS.experiment.addData('mouse_7.clicked_name', mouse_7.clicked_name);
    
    // the Routine "practice1_ans" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice2MaxDurationReached;
var practice2MaxDuration;
var practice2Components;
function practice2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice2' ---
    t = 0;
    practice2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice2MaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_3
    // current position of the mouse:
    mouse_3.x = [];
    mouse_3.y = [];
    mouse_3.leftButton = [];
    mouse_3.midButton = [];
    mouse_3.rightButton = [];
    mouse_3.time = [];
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('practice2.started', globalClock.getTime());
    practice2MaxDuration = null
    // keep track of which components have finished
    practice2Components = [];
    practice2Components.push(matrix_2);
    practice2Components.push(ans1_2);
    practice2Components.push(mouse_3);
    
    practice2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice2' ---
    // get current time
    t = practice2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *matrix_2* updates
    if (t >= 0.0 && matrix_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      matrix_2.tStart = t;  // (not accounting for frame time here)
      matrix_2.frameNStart = frameN;  // exact frame index
      
      matrix_2.setAutoDraw(true);
    }
    
    
    // *ans1_2* updates
    if (t >= 0.0 && ans1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1_2.tStart = t;  // (not accounting for frame time here)
      ans1_2.frameNStart = frameN;  // exact frame index
      
      ans1_2.setAutoDraw(true);
    }
    
    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_3.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_3.clickableObjects)) {
              mouse_3.clickableObjects = [mouse_3.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_3.clickableObjects) {
              if (obj.contains(mouse_3)) {
                  gotValidClick = true;
                  mouse_3.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_3.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_3.clickableObjects)) {
              mouse_3.clickableObjects = [mouse_3.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_3.clickableObjects) {
              if (obj.contains(mouse_3)) {
                  gotValidClick = true;
                  mouse_3.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_3.getPos();
            mouse_3.x.push(_mouseXYs[0]);
            mouse_3.y.push(_mouseXYs[1]);
            mouse_3.leftButton.push(_mouseButtons[0]);
            mouse_3.midButton.push(_mouseButtons[1]);
            mouse_3.rightButton.push(_mouseButtons[2]);
            mouse_3.time.push(mouse_3.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice2' ---
    practice2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice2.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_3.x', mouse_3.x);
    psychoJS.experiment.addData('mouse_3.y', mouse_3.y);
    psychoJS.experiment.addData('mouse_3.leftButton', mouse_3.leftButton);
    psychoJS.experiment.addData('mouse_3.midButton', mouse_3.midButton);
    psychoJS.experiment.addData('mouse_3.rightButton', mouse_3.rightButton);
    psychoJS.experiment.addData('mouse_3.time', mouse_3.time);
    psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name);
    
    // the Routine "practice2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice2_ansMaxDurationReached;
var practice2_ansMaxDuration;
var practice2_ansComponents;
function practice2_ansRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice2_ans' ---
    t = 0;
    practice2_ansClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice2_ansMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_4
    // current position of the mouse:
    mouse_4.x = [];
    mouse_4.y = [];
    mouse_4.leftButton = [];
    mouse_4.midButton = [];
    mouse_4.rightButton = [];
    mouse_4.time = [];
    mouse_4.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('practice2_ans.started', globalClock.getTime());
    practice2_ansMaxDuration = null
    // keep track of which components have finished
    practice2_ansComponents = [];
    practice2_ansComponents.push(matrix_3);
    practice2_ansComponents.push(ans1_3);
    practice2_ansComponents.push(mouse_4);
    practice2_ansComponents.push(text_3);
    
    practice2_ansComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice2_ansRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice2_ans' ---
    // get current time
    t = practice2_ansClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *matrix_3* updates
    if (t >= 0.0 && matrix_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      matrix_3.tStart = t;  // (not accounting for frame time here)
      matrix_3.frameNStart = frameN;  // exact frame index
      
      matrix_3.setAutoDraw(true);
    }
    
    
    // *ans1_3* updates
    if (t >= 0.0 && ans1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1_3.tStart = t;  // (not accounting for frame time here)
      ans1_3.frameNStart = frameN;  // exact frame index
      
      ans1_3.setAutoDraw(true);
    }
    
    // *mouse_4* updates
    if (t >= 0.0 && mouse_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_4.tStart = t;  // (not accounting for frame time here)
      mouse_4.frameNStart = frameN;  // exact frame index
      
      mouse_4.status = PsychoJS.Status.STARTED;
      mouse_4.mouseClock.reset();
      prevButtonState = mouse_4.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_4.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_4.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_4.clickableObjects)) {
              mouse_4.clickableObjects = [mouse_4.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_4.clickableObjects) {
              if (obj.contains(mouse_4)) {
                  gotValidClick = true;
                  mouse_4.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_4.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_4.clickableObjects)) {
              mouse_4.clickableObjects = [mouse_4.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_4.clickableObjects) {
              if (obj.contains(mouse_4)) {
                  gotValidClick = true;
                  mouse_4.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_4.getPos();
            mouse_4.x.push(_mouseXYs[0]);
            mouse_4.y.push(_mouseXYs[1]);
            mouse_4.leftButton.push(_mouseButtons[0]);
            mouse_4.midButton.push(_mouseButtons[1]);
            mouse_4.rightButton.push(_mouseButtons[2]);
            mouse_4.time.push(mouse_4.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice2_ansComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice2_ansRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice2_ans' ---
    practice2_ansComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice2_ans.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_4.x', mouse_4.x);
    psychoJS.experiment.addData('mouse_4.y', mouse_4.y);
    psychoJS.experiment.addData('mouse_4.leftButton', mouse_4.leftButton);
    psychoJS.experiment.addData('mouse_4.midButton', mouse_4.midButton);
    psychoJS.experiment.addData('mouse_4.rightButton', mouse_4.rightButton);
    psychoJS.experiment.addData('mouse_4.time', mouse_4.time);
    psychoJS.experiment.addData('mouse_4.clicked_name', mouse_4.clicked_name);
    
    // the Routine "practice2_ans" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice3MaxDurationReached;
var practice3MaxDuration;
var practice3Components;
function practice3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice3' ---
    t = 0;
    practice3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice3MaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_9
    // current position of the mouse:
    mouse_9.x = [];
    mouse_9.y = [];
    mouse_9.leftButton = [];
    mouse_9.midButton = [];
    mouse_9.rightButton = [];
    mouse_9.time = [];
    mouse_9.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('practice3.started', globalClock.getTime());
    practice3MaxDuration = null
    // keep track of which components have finished
    practice3Components = [];
    practice3Components.push(matrix_8);
    practice3Components.push(ans1_8);
    practice3Components.push(mouse_9);
    
    practice3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice3' ---
    // get current time
    t = practice3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *matrix_8* updates
    if (t >= 0.0 && matrix_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      matrix_8.tStart = t;  // (not accounting for frame time here)
      matrix_8.frameNStart = frameN;  // exact frame index
      
      matrix_8.setAutoDraw(true);
    }
    
    
    // *ans1_8* updates
    if (t >= 0.0 && ans1_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1_8.tStart = t;  // (not accounting for frame time here)
      ans1_8.frameNStart = frameN;  // exact frame index
      
      ans1_8.setAutoDraw(true);
    }
    
    // *mouse_9* updates
    if (t >= 0.0 && mouse_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_9.tStart = t;  // (not accounting for frame time here)
      mouse_9.frameNStart = frameN;  // exact frame index
      
      mouse_9.status = PsychoJS.Status.STARTED;
      mouse_9.mouseClock.reset();
      prevButtonState = mouse_9.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_9.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_9.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_9.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_9.clickableObjects)) {
              mouse_9.clickableObjects = [mouse_9.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_9.clickableObjects) {
              if (obj.contains(mouse_9)) {
                  gotValidClick = true;
                  mouse_9.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_9.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_9.clickableObjects)) {
              mouse_9.clickableObjects = [mouse_9.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_9.clickableObjects) {
              if (obj.contains(mouse_9)) {
                  gotValidClick = true;
                  mouse_9.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_9.getPos();
            mouse_9.x.push(_mouseXYs[0]);
            mouse_9.y.push(_mouseXYs[1]);
            mouse_9.leftButton.push(_mouseButtons[0]);
            mouse_9.midButton.push(_mouseButtons[1]);
            mouse_9.rightButton.push(_mouseButtons[2]);
            mouse_9.time.push(mouse_9.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice3' ---
    practice3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice3.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_9.x', mouse_9.x);
    psychoJS.experiment.addData('mouse_9.y', mouse_9.y);
    psychoJS.experiment.addData('mouse_9.leftButton', mouse_9.leftButton);
    psychoJS.experiment.addData('mouse_9.midButton', mouse_9.midButton);
    psychoJS.experiment.addData('mouse_9.rightButton', mouse_9.rightButton);
    psychoJS.experiment.addData('mouse_9.time', mouse_9.time);
    psychoJS.experiment.addData('mouse_9.clicked_name', mouse_9.clicked_name);
    
    // the Routine "practice3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice3_ansMaxDurationReached;
var practice3_ansMaxDuration;
var practice3_ansComponents;
function practice3_ansRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice3_ans' ---
    t = 0;
    practice3_ansClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice3_ansMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_8
    // current position of the mouse:
    mouse_8.x = [];
    mouse_8.y = [];
    mouse_8.leftButton = [];
    mouse_8.midButton = [];
    mouse_8.rightButton = [];
    mouse_8.time = [];
    mouse_8.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('practice3_ans.started', globalClock.getTime());
    practice3_ansMaxDuration = null
    // keep track of which components have finished
    practice3_ansComponents = [];
    practice3_ansComponents.push(matrix_7);
    practice3_ansComponents.push(ans1_7);
    practice3_ansComponents.push(mouse_8);
    practice3_ansComponents.push(text_5);
    
    practice3_ansComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice3_ansRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice3_ans' ---
    // get current time
    t = practice3_ansClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *matrix_7* updates
    if (t >= 0.0 && matrix_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      matrix_7.tStart = t;  // (not accounting for frame time here)
      matrix_7.frameNStart = frameN;  // exact frame index
      
      matrix_7.setAutoDraw(true);
    }
    
    
    // *ans1_7* updates
    if (t >= 0.0 && ans1_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1_7.tStart = t;  // (not accounting for frame time here)
      ans1_7.frameNStart = frameN;  // exact frame index
      
      ans1_7.setAutoDraw(true);
    }
    
    // *mouse_8* updates
    if (t >= 0.0 && mouse_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_8.tStart = t;  // (not accounting for frame time here)
      mouse_8.frameNStart = frameN;  // exact frame index
      
      mouse_8.status = PsychoJS.Status.STARTED;
      mouse_8.mouseClock.reset();
      prevButtonState = mouse_8.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_8.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_8.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_8.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_8.clickableObjects)) {
              mouse_8.clickableObjects = [mouse_8.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_8.clickableObjects) {
              if (obj.contains(mouse_8)) {
                  gotValidClick = true;
                  mouse_8.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_8.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_8.clickableObjects)) {
              mouse_8.clickableObjects = [mouse_8.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_8.clickableObjects) {
              if (obj.contains(mouse_8)) {
                  gotValidClick = true;
                  mouse_8.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_8.getPos();
            mouse_8.x.push(_mouseXYs[0]);
            mouse_8.y.push(_mouseXYs[1]);
            mouse_8.leftButton.push(_mouseButtons[0]);
            mouse_8.midButton.push(_mouseButtons[1]);
            mouse_8.rightButton.push(_mouseButtons[2]);
            mouse_8.time.push(mouse_8.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice3_ansComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice3_ansRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice3_ans' ---
    practice3_ansComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice3_ans.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_8.x', mouse_8.x);
    psychoJS.experiment.addData('mouse_8.y', mouse_8.y);
    psychoJS.experiment.addData('mouse_8.leftButton', mouse_8.leftButton);
    psychoJS.experiment.addData('mouse_8.midButton', mouse_8.midButton);
    psychoJS.experiment.addData('mouse_8.rightButton', mouse_8.rightButton);
    psychoJS.experiment.addData('mouse_8.time', mouse_8.time);
    psychoJS.experiment.addData('mouse_8.clicked_name', mouse_8.clicked_name);
    
    // the Routine "practice3_ans" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var start_realMaxDurationReached;
var start_realMaxDuration;
var start_realComponents;
function start_realRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_real' ---
    t = 0;
    start_realClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    start_realMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_10
    // current position of the mouse:
    mouse_10.x = [];
    mouse_10.y = [];
    mouse_10.leftButton = [];
    mouse_10.midButton = [];
    mouse_10.rightButton = [];
    mouse_10.time = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('start_real.started', globalClock.getTime());
    start_realMaxDuration = null
    // keep track of which components have finished
    start_realComponents = [];
    start_realComponents.push(text_6);
    start_realComponents.push(mouse_10);
    
    start_realComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function start_realRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_real' ---
    // get current time
    t = start_realClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    // *mouse_10* updates
    if (t >= 0.0 && mouse_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_10.tStart = t;  // (not accounting for frame time here)
      mouse_10.frameNStart = frameN;  // exact frame index
      
      mouse_10.status = PsychoJS.Status.STARTED;
      mouse_10.mouseClock.reset();
      prevButtonState = mouse_10.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_10.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_10.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_10.getPos();
          mouse_10.x.push(_mouseXYs[0]);
          mouse_10.y.push(_mouseXYs[1]);
          mouse_10.leftButton.push(_mouseButtons[0]);
          mouse_10.midButton.push(_mouseButtons[1]);
          mouse_10.rightButton.push(_mouseButtons[2]);
          mouse_10.time.push(mouse_10.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    start_realComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var loop_timer;
function start_realRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_real' ---
    start_realComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('start_real.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_10.x', mouse_10.x);
    psychoJS.experiment.addData('mouse_10.y', mouse_10.y);
    psychoJS.experiment.addData('mouse_10.leftButton', mouse_10.leftButton);
    psychoJS.experiment.addData('mouse_10.midButton', mouse_10.midButton);
    psychoJS.experiment.addData('mouse_10.rightButton', mouse_10.rightButton);
    psychoJS.experiment.addData('mouse_10.time', mouse_10.time);
    
    // Run 'End Routine' code from code_2
    loop_timer = new util.Clock();
    
    // the Routine "start_real" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'raven_trialList.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialMaxDurationReached;
var trialMaxDuration;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    matrix.setImage(matrix_image);
    ans1.setImage(ans1_image);
    ans2.setImage(ans2_image);
    ans3.setImage(ans3_image);
    ans4.setImage(ans4_image);
    ans5.setImage(ans5_image);
    ans6.setImage(ans6_image);
    ans7.setImage(ans7_image);
    ans8.setImage(ans8_image);
    item_number.setText(item_n);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(matrix);
    trialComponents.push(ans1);
    trialComponents.push(ans2);
    trialComponents.push(ans3);
    trialComponents.push(ans4);
    trialComponents.push(ans5);
    trialComponents.push(ans6);
    trialComponents.push(ans7);
    trialComponents.push(ans8);
    trialComponents.push(item_number);
    trialComponents.push(mouse);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *matrix* updates
    if (t >= 0.0 && matrix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      matrix.tStart = t;  // (not accounting for frame time here)
      matrix.frameNStart = frameN;  // exact frame index
      
      matrix.setAutoDraw(true);
    }
    
    
    // *ans1* updates
    if (t >= 0.0 && ans1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1.tStart = t;  // (not accounting for frame time here)
      ans1.frameNStart = frameN;  // exact frame index
      
      ans1.setAutoDraw(true);
    }
    
    
    // *ans2* updates
    if (t >= 0.0 && ans2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans2.tStart = t;  // (not accounting for frame time here)
      ans2.frameNStart = frameN;  // exact frame index
      
      ans2.setAutoDraw(true);
    }
    
    
    // *ans3* updates
    if (t >= 0.0 && ans3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans3.tStart = t;  // (not accounting for frame time here)
      ans3.frameNStart = frameN;  // exact frame index
      
      ans3.setAutoDraw(true);
    }
    
    
    // *ans4* updates
    if (t >= 0.0 && ans4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans4.tStart = t;  // (not accounting for frame time here)
      ans4.frameNStart = frameN;  // exact frame index
      
      ans4.setAutoDraw(true);
    }
    
    
    // *ans5* updates
    if (t >= 0.0 && ans5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans5.tStart = t;  // (not accounting for frame time here)
      ans5.frameNStart = frameN;  // exact frame index
      
      ans5.setAutoDraw(true);
    }
    
    
    // *ans6* updates
    if (t >= 0.0 && ans6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans6.tStart = t;  // (not accounting for frame time here)
      ans6.frameNStart = frameN;  // exact frame index
      
      ans6.setAutoDraw(true);
    }
    
    
    // *ans7* updates
    if (t >= 0.0 && ans7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans7.tStart = t;  // (not accounting for frame time here)
      ans7.frameNStart = frameN;  // exact frame index
      
      ans7.setAutoDraw(true);
    }
    
    
    // *ans8* updates
    if (t >= 0.0 && ans8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans8.tStart = t;  // (not accounting for frame time here)
      ans8.frameNStart = frameN;  // exact frame index
      
      ans8.setAutoDraw(true);
    }
    
    
    // *item_number* updates
    if (t >= 0.0 && item_number.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_number.tStart = t;  // (not accounting for frame time here)
      item_number.frameNStart = frameN;  // exact frame index
      
      item_number.setAutoDraw(true);
    }
    
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse.clickableObjects)) {
              mouse.clickableObjects = [mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse.clickableObjects) {
              if (obj.contains(mouse)) {
                  gotValidClick = true;
                  mouse.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse.clickableObjects = eval([ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse.clickableObjects)) {
              mouse.clickableObjects = [mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse.clickableObjects) {
              if (obj.contains(mouse)) {
                  gotValidClick = true;
                  mouse.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse.getPos();
            mouse.x.push(_mouseXYs[0]);
            mouse.y.push(_mouseXYs[1]);
            mouse.leftButton.push(_mouseButtons[0]);
            mouse.midButton.push(_mouseButtons[1]);
            mouse.rightButton.push(_mouseButtons[2]);
            mouse.time.push(mouse.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // Run 'Each Frame' code from code
    if ((loop_timer.getTime() > 600)) {
        continueRoutine = false;
        trials.finished = true;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    // Run 'End Routine' code from code
    loop_timer = new util.Clock();
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_expMaxDurationReached;
var end_expMaxDuration;
var end_expComponents;
function end_expRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_exp' ---
    t = 0;
    end_expClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    end_expMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('end_exp.started', globalClock.getTime());
    end_expMaxDuration = null
    // keep track of which components have finished
    end_expComponents = [];
    end_expComponents.push(text);
    
    end_expComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function end_expRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_exp' ---
    // get current time
    t = end_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    end_expComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_expRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_exp' ---
    end_expComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end_exp.stopped', globalClock.getTime());
    if (end_expMaxDurationReached) {
        routineTimer.add(end_expMaxDuration);
    } else {
        routineTimer.add(-5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

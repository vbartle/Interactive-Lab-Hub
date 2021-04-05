let label = "waiting...";
let classifier;
let modelURL = 'https://teachablemachine.withgoogle.com/models/RmpzfNMxd/';

// STEP 1: Load the model!
function preload() {
  classifier = ml5.soundClassifier(modelURL + 'model.json');
}

function setup() {
  createCanvas(640, 520);

  // STEP 2: Start classifying (will listen to mic by default)
  classifyAudio();
}

// STEP 2 classify!
function classifyAudio() {
  classifier.classify(gotResults);
}
let emoji = "🚪";

function draw() {
  background(0);
  textAlign(CENTER, CENTER);
  // Pick an emoji based on label
  if (label == "Background Noise") {
    // emoji = "🚪";
  } else if (label == "knock_") {
    emoji = "👀";
  } else if (label == "Class 4") {
    emoji = "👋";
  }

  // Draw the emoji
  textSize(256);
  text(emoji, width / 2, height / 2);
}

// STEP 3: Get the classification!
function gotResults(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  // Store the label
  label = results[0].label;
}

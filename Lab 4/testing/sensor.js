
// function reportReading() {
//     const temperature = (Math.random() * 20) - 5; // Range of -5 to 15
//     process.stdout.write(temperature + '\n'); // Write with newline char
//     setTimeout(reportReading, Math.random() * 5000); // Wait 0 to 5 seconds
// }
// reportReading();

// const { useEffect } = require("react");

// let label = "waiting...";
// let classifier;
// let modelURL = 'https://teachablemachine.withgoogle.com/models/RmpzfNMxd/';

// // var ml5 = require('./ml5.js')

// var nodes = [];
// var render = function(component, props, targetNode, callback) {
//   var reactElement = React.createElement(component, props, null);
//   ReactDOM.render(reactElement, targetNode, callback);
//   nodes.push(targetNode);
//   useEffect(() => {
//     ml5 = require('ml5')
//   }, [])
  
//   return reactElement;
// }

// function setup() {
//     createCanvas(640, 520);
  
//     // STEP 2: Start classifying (will listen to mic by default)
//     classifyAudio();
// }

// function draw() {
// background(0);
// textAlign(CENTER, CENTER);
// // // Pick an emoji based on label
// // if (label == "Background Noise") {
// //   // emoji = "🚪";
// // } else if (label == "knock_") {
// //   emoji = "👀";
// // } else if (label == "Class 4") {
// //   emoji = "👋";
// // }
// console.log()

// // Draw the emoji
// textSize(256);
// text(emoji, width / 2, height / 2);
// }

// // STEP 1: Load the model!
// function preload() {
//   classifier = ml5.soundClassifier(modelURL + 'model.json');
// }

// // STEP 2 classify!
// function classifyAudio() {
//   classifier.classify(gotResults);
// }

// // STEP 3: Get the classification!
// function gotResults(error, results) {
//   if (error) {
//     console.error(error);
//     return;
//   }
//   // Store the label
//   label = results[0].label;
//   process.stdout.write(label+'\n')
// }
// preload();
// classifyAudio();

"use strict";
exports.__esModule = true;
var React = require("react");
var ReactDOM = require("react-dom");
// exports.gooddata = require("@gooddata/gooddata-js");

// var GDRC  = require("@gooddata/react-components"); // GoodData React Components

// buffer of DOM elements rendering React components
var nodes = [];

// utility to mount React nodes to target DOM elements
// exports.ReactContentRenderer = {
//   unmountAll: function() {
//     if (nodes.length === 0) {
//       return;
//     }
//     nodes.forEach(node => React.unmountComponentAtNode(node));
//     nodes = [];
//   },
//   unmount: function(node) {
//     React.unmountComponentAtNode(node)
//   },
//   /**
//    * Creates, renders and returns a React element created
//    * from component class using given props and rendered
//    * into the targetNode.
//    */
//   render: function(component, props, targetNode, callback) {
//     var reactElement = React.createElement(component, props, null);
//     ReactDOM.render(reactElement, targetNode, callback);
//     nodes.push(targetNode);
//     return reactElement;
//   }

  
// };

// var render = function(component, props, targetNode, callback) {
//   var reactElement = React.createElement(component, props, null);
//   ReactDOM.render(reactElement, targetNode, callback);
//   nodes.push(targetNode);
//   return () => {5}
//   useEffect(() => {
//     ml5 = require('ml5') 
//     return () => {
//       console.log(ml5)}
//   }, [])

// re-export GoodData React components
// for (var prop in GDRC) {
//   if (GDRC.hasOwnProperty(prop)) {
//     exports[prop] = GDRC[prop];
//   }
// }

// var render = function Welcome(props) {
//   return 5;
// }

// console.log(render)

// From backbone
var extend = function(protoProps) {
  var parent = this;
  var child;

  var extendObj = function(obj1, obj2) {
     for (var i in obj1) {
        if (obj1.hasOwnProperty(i)) {
           obj2[i] = obj1[i];
        }
     }
  };

  if (protoProps && hasOwnProperty.call(protoProps, 'constructor')) {
    child = protoProps.constructor;
  } else {
    child = function() { return parent.apply(this, arguments); };
  }

  var Surrogate = function(){ this.constructor = child; };
  Surrogate.prototype = parent.prototype;
  child.prototype = new Surrogate;

  if (protoProps) extendObj(child.prototype, protoProps);

  child.__super__ = parent.prototype;

  return child;
};

React.Component.extend = extend;

var MyComponent = React.Component.extend({
  constructor: function() {

    
      console.log('hello from react component');

      this.state = {
          open: false
      };

      React.Component.apply(this, arguments);
  }
});

new MyComponent();
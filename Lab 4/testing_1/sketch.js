// Examples use jsonplaceholder.typicode.com for a Mock Data API

let url = 'https://localhost:5050';
let postData = { userId: 1, title: 'p5 Clicked!', body: 'p5.js is very cool.' };

function setup() {
  createCanvas(100, 100);
  background(200);
}

function mousePressed() {
  httpPost(url, 'json', postData, function(result) {
    strokeWeight(2);
    text(result.body, mouseX, mouseY);
  });
}
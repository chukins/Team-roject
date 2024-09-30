"use strict"

let weightEntry = document.getElementById("weight-entry");
let heightEntry = document.getElementById("height-entry");
let bmiDisplay = document.getElementById("display-bmi");

let weight = 1;
let height = 1;

document.getElementById("weight-entry").addEventListener("input", (entry) => {
    console.log("entered: " + entry.target.value);
    weight = entry.target.value;
    calculate();
});

document.getElementById("height-entry").addEventListener("input", (entry) => {
    console.log("entered: " + entry.target.value);
    height = entry.target.value;
    calculate();
});

function calculate() {
    document.getElementById("display-bmi").innerHTML = "Your BMI index is: " + Math.round(weight / ((height/100) ** 2) * 100) / 100;
}
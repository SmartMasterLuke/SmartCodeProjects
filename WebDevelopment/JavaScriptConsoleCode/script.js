// Easy way to log something in the browser console
console.log("Hello it's me, Smart Master Luke!");

// Different data types of variables
var varVariable = "varVariable: I'm a globally defined variable. You can change my value anywhere.";
let letVariable = "letVariable: I'm a block scope defined variable. You can only change me in the scope that I exist.";
const constVariable = "constVariable: I'm a constant. You can't override me."

console.log(varVariable);
console.log(letVariable);
console.log(constVariable);

// Value assignment of variables at different places in the code
var a = null;
var b = 3;

console.log(a);

var a = 5;
var b = a;

console.log("b = " + b);

// Define uninitiated variables
var c;
var d;
var e;

c = 2;
d = 5;
e = 50;
f = 77;
g = 101;
h = "I'm a beautiful ";

c += 5;
d -= c;
e *= c;
f /= 7;
g %= d;
h += "string.";

console.log("c = " + c);
console.log("d = " + d);
console.log("e = " + e);
console.log("f = " + f);
console.log("g = " + g);
console.log("h = " + h);

// Basic arithmetic operations
var sum = 2 + 5;
var dif = 5 - 2;
var pro = 2 * 5;
var quo = 5 / 2;

console.log("Sum = " + sum);
console.log("Difference = " + dif);
console.log("Product = " + pro);
console.log("Quotient = " + quo);

// Incrementing

//
var myArray = ["Smart", "Master", "Luke"];
var popAfterFirstValue = myArray.pop();
var shiftAfterFirstValue = myArray.shift();

console.log("My array: " + myArray);
console.log("Only the first value of myArray: " + popAfterFirstValue);
console.log("All values from myArray except of the first one: " + shiftAfterFirstValue);

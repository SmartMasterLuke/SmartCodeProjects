// Easy way to log something in the browser console
console.log("Hello it's me, Smart Master Luke!");

// Different data types of variables
var variableVar = "I'm a var"; // Value of that variable can be changed anywhere
let variableLet = "I'm a let"; // Value of that variable can only be changed in same scope - ES6
const variableConst = "I'm a const" // Value of that variable can't be changed - ES6



var myArray = ["Smart", "Master", "Luke"];
var popAfterFirstValue = myArray.pop();
var shiftAfterFirstValue = myArray.shift();

console.log("My array: " + myArray);
console.log("Only the first value of myArray: " + popAfterFirstValue);
console.log("All values from myArray except of the first one: " + shiftAfterFirstValue);

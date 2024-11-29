/* Real Calculator */
/*
function dis(val) {
  document.getElementById("display").value += val;
}

function appendToDisplay(input) {
  display.value += input;
}

function clearDisplay() {
  display.value = "";
}

function calculate() {
  display.value = eval(display.value);
}*/

/* Actual S1 Challenge */

var num1 = 15;
var num2 = 25;

// Function to give values and operation
function calculate(num1, num2, op) {
  // Gives value to 'OperatorList' as an array of strings
  operatorlist = ["add", "subtract", "divide", "multiply"];
  // If the operator doesnt pass, by checking the values of the array, then a message will pop up
  if (!operatorlist.includes(String(op))) {
    return "Unknown operation. Please use 'add', 'subtract', 'multiply', or 'divide'.";
  }
  // Is checking if the value is a numeric one. i.e num1 = a numeric number instead of verbal (string)
  if (typeof num1 !== "number" || typeof num2 !== "number") {
    return "Invalid input: both arguments must be numbers!";
  }
  // Begins a loop where if the operator matches value then a funtion matching that value will be applied
  if (op === "add") {
    return num1 + num2;
  }
  if (op === "subtract") {
    return num1 - num2;
  }
  if (op === "divide") {
    // If the value of a number equals to 0 an Error message will pop up
    if (num2 === 0) {
      return "You cannot divide by Zero";
    }
    return num1 / num2;
  }
  if (op === "multiply") {
    return num1 * num2;
  }
}

/* Switch/Case - Bonus */

/*  switch (op) {
    case 'add': {
      return num1 + num2;
    }
    case 'subtract': {
      return num1 - num2;
    }
    case 'divide': {
      if (num2 === 0) {
        return 'You cannot divide by Zero';
      }
      return num1 / num2;
    }
    case 'multiply': {
      return num1 * num2;
    }
  } */
// }

/* Valid inputs */

console.log(calculate(15, 25, "add")); // Output: 40
console.log(calculate(15, 25, "subtract")); // Output: -10
console.log(calculate(15, 25, "divide")); // Output: 375
console.log(calculate(15, 25, "multiply")); // Output: 0.6

/* Invalid inputs */

console.log(calculate("Fifteen", 25, "multiply")); // Invalid input: both arguments must be numbers.

console.log(calculate(15, 25, "Apple")); // Unknown operation. Please use 'add', 'subtract', 'multiply', or 'divide'.

console.log(calculate(15, 0, "divide")); // You cannot divide by Zero

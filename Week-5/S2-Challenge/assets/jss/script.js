/* Main Calculation */

function dis(val) {
  document.getElementById("display").value += val
}

function appendToDisplay(input) {
  display.value += input;
}

function clearDisplay() {
  display.value = "";
}

function calculate() {
  display.value = eval(display.value);
}




//  String Methods :-

const fruit = ['apple', 'banana', 'cherry', 'dragonFruit', 'elderberry']
const favfruit = "Leo's favourite fruit is Bananas!"

// This string capitalizes the first character of each string in the array.

const UpperCase = fruit
    .map((fruit) => fruit.charAt(0).toUpperCase() + fruit.slice(1))
    .join(" ")
console.log(UpperCase); // Expected OutPut - "Apple Banana Cherry DragonFruit Elderberry"

// This string swaps the first characters with a "$".

const Swap = fruit.map(fruit => '$' + fruit.slice(1))
console.log(Swap.join(" ")) // Expected OutPut - "$pple $anana $herry $ragonFruit $lderberry"

// This uses a regular expression to replace the first occurrence of 'Leo's' with 'My'.

const Alter = /Leo's/
console.log(favfruit.replace(Alter, "My")) // Expected OutPut - "My favourite fruit is Bananas!"


// Example of Use :-

const mess = 'I   aM        OK       WithThiS MESS!!            '

// This fixes the messy text by removing extra spacing, separating 'WithThiS', changing all text to lowercase, and then capitalizing the first letter of each word.
const fix = mess
    .trimEnd()
    .replace(/([A-Z][a-z])/g, ' $1') // Key 1
    .split(/\s+/) // Key 2
    .map(word => word.toLocaleLowerCase())
    .map(word => word.charAt(0).toLocaleUpperCase() + word.slice(1));
console.log(fix.join(' ')) // Expected OutPut - "I Am Ok With This Mess!!"

// Key 1:
    // '/--/' creates an expression, which is any valid set of variable and operators evaluated into a single value.

    // '(--)' creates a capturing group, which acts like a grouping operator that can group subpatterns, allowing you to apply quantifiers or use disjunctions with in it.

    // '[A-Z]' Is a character class that denotes a range of characters for UpperCase letters from A-Z.

    // '[a-z]' Is a character class that denotes a range of characters for LowerCase letters from a-z.

    // 'g' Is a modifier standing for 'Global Search' which when used will search for all matches in the string and not stop at the first one it encounters.

    // '-$1' The '-' (space) inserts a space before the search. The '$1' is a reference to the FIRST capturing group, in this case an UpperCase letter followed by one lowercase letter and putting a space before any of those matches. This is what helps split the two words 'withThis' into two separate words.

// Key 2:
    // '\s' Tries to match any WhiteSpace character (spaces, tabs, etc) that exists along a string. Split uses RegEx (Regular Expressions) to ensure proper splitting by whitespace.

    // '+' In a search it indicates one or more occurrences of the previous element.

        // Both together '\s+' inside a '.split' ensures that the string is split into equal short spaces at any sequence of WhiteSpacing.


// Real-World Scenario :-

const customerOrder = [
    {
        name: "Leo",
        want: "Mocha",
        quantity: 2
    },
    {
        name: "Vitor",
        want: "Espresso",
        quantity: 6
    },
    {
        name: "Jason",
        want: "Latte",
        quantity: 4
    }
]

const prices = {
    "Mocha": 4.99,
    "Espresso": 3.45,
    "Latte": 4.55
}

function padBothSides(str, totalLength) { // This Func makes 2 arguments, str (the string to pad) and totalLength (desired final length).

    str = String(str); // Converts 'str' into a string which avoids 'type-related' issues from occuring.

    const halfLength = Math.floor((totalLength - str.length) / 2); // 'Math.floor' is a function that rounds the number down to the nearest whole number which was useful in this case as there was some padding that required '11'. It then divides it by 2 using the '/ 2' to then fully calulate half of the required padding.

    return str
        .padStart(str.length + halfLength, ' ') // The 'str.lenght' is a property that gives the value of how many characters there are in the string.

        .padEnd(totalLength, ' '); // The 'totalLength' represents the desired length of the final padded string.

        // From the 'Return', it completes the funtion. So when the function is first called (line 102), it exacutes it and upon reaching return, it returns to the place it was first called, again line 102, but with the value of the function. Then it goes on to the following time its called (line 103), and repeats until its no longer called.
}


function placedOrder(orderList) {
    const border = "~".repeat(60); // This gives a '~' multiplied by 60 value to the const 'border'.
    const title = "|    Name    |    Order    |    Quantity    |    Total     |"; // This gives a desired string style value to the const 'title'.

    console.log(`${border}\n${title}\n${border}`); // Prints out in the format written. '\n' creates a new line, so instead of printing everything on one line, it splits across three lines due to the placeholders and line breaks.

    orderList.forEach(customerOrder => { // Iterates over each customerOrder in the orderList array and performs an action on each element.

        const name = padBothSides(customerOrder.name, 10); 
        const typeOfCoffee = padBothSides(customerOrder.want,11); 
        const quantity = padBothSides(customerOrder.quantity, 14);// 'name', 'typeOfCoffee' & 'quantity' all give the same action do add padding with their respective values, incased in the 'padBothSides' function (line 84) which ensures that each value is centered within its column, contributing to a neatly formatted output.

        const total = "£" + (prices[customerOrder.want] * customerOrder.quantity).toFixed(2); // This action is what calculates the total price of each order to give it a new final value to the 'customerOrder'. First it adds a '£' string to the start so it has a clearer indication of what type of value it represents. Then it grabs the value of each property corresponding with the value equal to its string inside both the 'prices' and 'customerOrder' arrays, for example, 'Mocha' at £4.99 multiplied by quantity (2) results in a total of £9.98. toFixed(2) ensures the total is rounded to two decimal places (0.00<== ). For example if I had two numbers that went to the third decimal (i.e- 1.985 + 1.906), together their real value would be '3.891', but as i set the limit to '2' and the third number is below 5, it gets rounded down to '3.89'. Alternatively if it was '1.989 + 1.907' where the new total value would be '3.896', because the third decimal is 5 or higher it would be rounded up to '3.90'. Even with a zero value, it still shows as i specifically requested it to show up to two decimal spaces.

        const totalstr = total.padStart(12, ' '); // This differs from the 'padBothSides' mainly because for visual apeal the price will need to be printed on the far right. This is achieved by implementing a 'padStart' methhod to give the desired length of spacing before the text (left side). Alternatively if I wanted the padding to be after the text (right side), then instead of 'padStart', 'padEnd' would achieve that.

        console.log(`| ${name} | ${typeOfCoffee} | ${quantity} | ${totalstr} |`); // Constructs a formatted string for each order, with each piece of data (name, type of coffee, quantity, and total) properly aligned within the table's columns, using template literals and the padBothSides function for centering.
    })

    console.log(border); // Finally, logs the bottom border to complete the table.
}
placedOrder(customerOrder); // Calls the placedOrder function and passes the customerOrder array as an argument.This initiates the process of formatting and printing the order details in a neatly formatted table.


// Expected Output:

/*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|    Name    |    Order    |    Quantity    |    Total     |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|    Leo     |    Mocha    |       2        |        £9.00 |
|   Vitor    |  Espresso   |       6        |       £18.00 |
|   Jason    |    Latte    |       4        |       £16.00 |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
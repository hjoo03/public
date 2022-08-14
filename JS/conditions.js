var input = prompt();

// Check type
if (input == "true") {
    input = true;
}
else if (input == "false") {
    input = false;
}
else if (Number.isNaN(input)) {
    input = Number(input);
}

switch (true) {
    case typeof(input) == "string":
        alert("It is a String.");
        break;
    
    case typeof(input) == "number":
        alert("It is a number.");
        break;

    case typeof(input) == "boolean":
        alert("It is a boolean.");
        break;
}

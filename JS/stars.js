for (var i = 0; i < 14; i++) {
    var output = ''
    for (var j = 14; j - i> 0; j--) {
        output += ' '
    }
    stars = i * 2 - 1
    for (var k = 0; k < stars; k++) {
        output += '*'
    }
    console.log(output)
}
let filterElements = function (criteria, ...elements) {
    let output = []
    for (var i = 0; i < elements.length; i++) {
        if (elements[i] > criteria) {
            output.push(elements[i])
        }
    }
    console.log(output)
}
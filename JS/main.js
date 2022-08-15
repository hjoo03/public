const arr = [1, 2, 3, 4, 5]

arr.forEach(function (value, index, array) {
    console.log(`${index}번째 요소: ${value}`)
    console.log(`array: ${array}`)
})
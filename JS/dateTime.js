var dateTime = function() {
    const datetime = new Date();
    var year = datetime.getFullYear();
    var month = ("00" + (datetime.getMonth() + 1)).slice(-2);
    var date = ("00" + datetime.getDate()).slice(-2);
    var hour = ("00" + datetime.getHours()).slice(-2);
    var minute = ("00" + datetime.getMinutes()).slice(-2);
    var second = ("00" + datetime.getSeconds()).slice(-2);
    return String(year) + "/" + String(month) + "/" +
    String(date) + " " + String(hour) + ":" +
    String(minute) + ":" + String(second);
}
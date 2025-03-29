loadData();

function loadData() {
    seats = [];
    totalPrice = 0.0;
}

function refreshData() {
    document.getElementById('seat-selected-pretty').innerHTML = seats;
    document.getElementById('total-cost').innerHTML = totalPrice;

    document.getElementById('seat-input').value = seats.join("-");
}

function seatClick(id) {
    if (seats.includes(id)) {
        // remove seat
        seats.splice(seats.indexOf(id), 1);
        document.getElementById(id).style.filter = null;
    } else {
        // add seat
        seats.push(id);
        document.getElementById(id).style.filter = "drop-shadow(4px 4px 0 #febd10)";
    }
    totalPrice = seats.length * parseFloat(document.getElementById("price").innerHTML);
    refreshData();
}
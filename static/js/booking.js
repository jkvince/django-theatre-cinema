loadData();

function loadData() {
    seats = [];
    totalPrice = 0.0;
}

function refreshData() {
    document.getElementById('seat-selected-list').innerHTML = seats;
}

function seatClick(id) {
    if (seats.includes(id)) {
        seats.splice(seats.indexOf(id), 1);
    } else {
        seats.push(id)
    }
    console.log(seats);
    refreshData();
}
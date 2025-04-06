loadData();

function loadData() {
    seatsSelected = [];
    totalPrice = 0.0;
}

function refreshData() {
    document.getElementById('seat-selected-pretty').innerHTML = seatsSelected;
    document.getElementById('total-cost').innerHTML = totalPrice;

    document.getElementById('seat-input').value = seatsSelected.join("-");
}

function seatClick(id) {
    if (seatsSelected.includes(id)) {
        // remove seat
        seatsSelected.splice(seatsSelected.indexOf(id), 1);
        document.getElementById(id).style.filter = null;
    } else {
        // add seat
        seatsSelected.push(id);
        document.getElementById(id).style.filter = "drop-shadow(4px 4px 0 #febd10)";
    }
    totalPrice = seatsSelected.length * parseFloat(document.getElementById("price").innerHTML);
    refreshData();
}

function createGrid() {
    let string_elements = "";

    for (row = 0; row < grid_rows; row++) {
        string_elements += "<tr>";
        for (column = 0; column < grid_columns; column++) {
            string_elements += "<td>";

            let seat = grid.find(item => item.location_row == row && item.location_column == column);
            if (seat != null) {
                string_elements += `<img draggable=false id="` + seat.number + `"`;

                string_elements += `src="`;
                if (bookedSeats.includes(seat.number)) {
                    if (seat.premium == true) {
                        string_elements += imgLinks["premium_booked"];
                    } else if (seat.accessible == true) {
                        string_elements += imgLinks["accessible_booked"];
                    } else {
                        string_elements += imgLinks["base_booked"];
                    }
                    string_elements += `">`;
                } else {
                    if (seat.premium == true) {
                        if (premium == true) {
                            string_elements += imgLinks["premium"] + `"`;
                            string_elements += `class="clickable" onclick="seatClick('` + seat.number + `');"`;
                        } else {
                            string_elements += imgLinks["premium_booked"] + `"`;
                        }
                    } else if (seat.accessible == true) {
                        string_elements += imgLinks["accessible"] + `"`;
                        string_elements += `class="clickable" onclick="seatClick('` + seat.number + `');"`;
                    } else {
                        string_elements += imgLinks["base"] + `"`;
                        string_elements += `class="clickable" onclick="seatClick('` + seat.number + `');"`;
                    }
                    string_elements += `>`;
                }
            }
            string_elements += "</td>";
        }
        string_elements += "</tr>";
    }

    document.getElementById('table').innerHTML = string_elements;
}
loadData();

function loadData() {
    selection_row = null;
    selection_column = null;
}

function updateStateForm(cursorState) {
    if (cursorState == "emptycell") {
        document.getElementById('number-input').disabled = true;
        document.getElementById('seat-type-input').disabled = true;
        document.getElementById('delete-seat').disabled = true;
        document.getElementById('create-seat').disabled = false;

    } else if (cursorState == "filledcell") {
        document.getElementById('number-input').disabled = false;
        document.getElementById('seat-type-input').disabled = false;
        document.getElementById('delete-seat').disabled = false;
        document.getElementById('create-seat').disabled = true;

    } else if (cursorState == "unselected") {
        document.getElementById('number-input').disabled = true;
        document.getElementById('seat-type-input').disabled = true;
        document.getElementById('delete-seat').disabled = true;
        document.getElementById('create-seat').disabled = true;
    }
}

function gridChanged() {
    grid_rows = document.getElementById('grid-row').value;
    grid_columns = document.getElementById('grid-col').value;

    // add here removing seats out of bounds
    refreshGrid();
}

function gridClick(id) {
    id = id.split("-");

    if (Number(id[0]) == selection_row && Number(id[1]) == selection_column) {
        // unselect
        selection_row = null;
        selection_column = null;

        updateStateForm('unselected');
    } else {
        selection_row = Number(id[0]);
        selection_column = Number(id[1]);

        document.getElementById('number-input').disabled = false;
        document.getElementById('seat-type-input').disabled = false;

        let seat = grid.find(item => item.location_row == selection_row && item.location_column == selection_column);
        
        if (seat != null) {
            // filled cell
            updateStateForm('filledcell');
            document.getElementById('number-input').value = seat.number;
        
            if (seat.premium == true) {
                document.getElementById('seat-type-input').value = 'premium';
            } else if (seat.accessible == true) {
                document.getElementById('seat-type-input').value = 'accessible';
            } else {
                document.getElementById('seat-type-input').value = 'base';
            }
        } else {
            // empty cell
            updateStateForm('emptycell');
        }

    }
    
    refreshGrid();
}

function refreshGrid() {
    string_elements = "";

    for (row=0; row<grid_rows; row++) {
        string_elements += "<tr>";
        for (column=0; column<grid_columns; column++) {
            string_elements += `<td class="clickable" onclick="gridClick('` + row + "-" + column + `');">`;

            if (row == selection_row && column == selection_column) {
                string_elements += `<img id='cursor' src="` + imgLinks["cursor"] + `">`;
            }
            
            let seat = grid.find(item => item.location_row == row && item.location_column == column);
            if (seat != null) {
                string_elements += `<img id="` + seat.number + `" src="`;
                if (seat.premium == true) {
                    string_elements += imgLinks["premium"];
                } else if (seat.accessible == true) {
                    string_elements += imgLinks["accessible"];
                } else {
                    string_elements += imgLinks["base"];
                }
                string_elements += `">`;
            }

            string_elements += "</td>";
        }
        string_elements += "</tr>";
    }

    document.getElementById('table').innerHTML = string_elements;
}
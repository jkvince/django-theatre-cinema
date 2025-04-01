function gridChanged() {
    grid_rows = document.getElementById('grid-row').value;
    grid_columns = document.getElementById('grid-col').value;

    // add here removing seats out of bounds
    refreshGrid();
}

function refreshGrid() {
    string_elements = "";

    for (row=0; row<grid_rows; row++) {
        string_elements += "<tr>";
        for (column=0; column<grid_columns; column++) {
            string_elements += `<td class="clickable">`;
            
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
                string_elements += `"`;
                // add function call onclick
                string_elements += `>`;
            }


            string_elements += "</td>";
        }
        string_elements += "</tr>";
    }


    document.getElementById('table').innerHTML = string_elements;

}
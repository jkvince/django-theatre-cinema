class Plan {
    constructor(rows_in=30, columns_in=30) {
        this.rows = rows_in;
        this.columns = columns_in;

    }

    getRows() { return this.rows }
    getColumns() { return this.columns }
    setRows(rows_in) { this.rows = rows_in }
    setColumns(columns_in) { this.columns = columns_in }
}


function changeSize(param) {
    if (param == 'rows') {
        console.log("changed rows")
    } else if (param == 'columns') {
        console.log("changed columns")
    }

}


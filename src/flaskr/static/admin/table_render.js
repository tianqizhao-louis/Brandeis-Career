function createTableBody(table_head, table_dict) {
    let tbody = document.createElement('tbody');
    // table_head.forEach(function (eachHead, index) {
    //
    // });
    Object.keys(table_dict).forEach(function (key) {
        let tr = document.createElement('tr');
        let this_dict = table_dict[key];

        table_head.forEach(function (eachHead, index) {
           let new_td = document.createElement('td');
           new_td.textContent = this_dict[eachHead];
           tr.appendChild(new_td)
        });

        tbody.appendChild(tr);
    });

    return tbody;
}

function createTable(table_name, table_head, table_dict) {
    let table_render = document.createElement('table');
    table_render.className = 'table';
    table_render.id = 'table-view';
    table_render.appendChild(createTableHead(table_head));
    table_render.appendChild(createTableBody(table_head, table_dict));
    return table_render;
}

function createTableHead(table_head) {
    let thead = document.createElement('thead');
    let tr = document.createElement('tr');
    table_head.forEach(function (eachHead, index) {
        tr.appendChild(createEachTableHead(eachHead));
    });
    thead.appendChild(tr);
    return thead;
}

function createEachTableHead(elementName) {
    let th = document.createElement('th');
    th.textContent = elementName;
    return th;
}

document.addEventListener('DOMContentLoaded', () => {
    const table_name = fetch_table["table_name"];
    const table_head = fetch_table["schema"];
    let table_dict = fetch_table["table_dict"];

    const table_selector = document.querySelector("#render-table");

    if (table_type === "professor") {
        table_selector.appendChild(createTable(table_name, table_head, table_dict));
    }else if (table_type === "gender") {
        table_selector.appendChild(createTable(table_name, table_head, table_dict));
    } else if (table_type === "concentration") {
        table_selector.appendChild(createTable(table_name, table_head, table_dict));
    } else if (table_type === "job_merged_table") {
        table_selector.appendChild(createTable(table_name, table_head, table_dict));
    } else if (table_type === "company") {
        table_selector.appendChild(createTable(table_name, table_head, table_dict));
    }
});
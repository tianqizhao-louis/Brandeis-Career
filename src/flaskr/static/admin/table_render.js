// function createProfessorTable(prof_dict) {
//     let prof_table = document.createElement('table');
//     prof_table.className = 'table';
//     prof_table.id = 'render-prof-table';
//     prof_table.appendChild(createTableHead());
//     prof_table.appendChild(createTableBody(prof_dict));
//     return prof_table;
// }
//
// function createTableBody(prof_dict) {
//     let tbody = document.createElement('tbody');
//
//     Object.keys(prof_dict).forEach(function (key) {
//         let tr = document.createElement('tr');
//         let item_id = key;
//         let item_dict = prof_dict[key]
//         let td_first_name = document.createElement('td');
//         td_first_name.textContent = item_dict["first_name"];
//         tr.appendChild(td_first_name);
//
//         let td_last_name = document.createElement('td');
//         td_last_name.textContent = item_dict["last_name"];
//         tr.appendChild(td_last_name);
//         tbody.appendChild(tr);
//     });
//     return tbody;
// }
//
// function createTableHead() {
//     let thead = document.createElement('thead');
//     let tr = document.createElement('tr');
//
//     let table_header = ['First Name', 'Last Name']
//     table_header.forEach(function (eachElement, index){
//         tr.appendChild(createEachTableHead(eachElement));
//     });
//     thead.appendChild(tr);
//     return thead;
// }
//
// function createEachTableHead(elementName) {
//     let th = document.createElement('th');
//     th.textContent = elementName;
//     return th;
// }


function professorTableRenderer(fetch_table) {
    const table_selector = document.querySelector("#render-table");
    const table_head = extractProfessorTableHead(fetch_table);

    let table_prof = document.createElement('table');
    table_prof.className = 'table';
    table_prof.id = 'table-view';
    table_prof.appendChild(createProfessorTableHead(table_head));
    table_prof.appendChild(createProfessorTableBody(fetch_table));
    table_selector.append(table_prof);
}

function createProfessorTableBody(fetch_table) {
    let tbody = document.createElement('tbody');

    Object.keys(fetch_table).forEach(function (key) {
        let tr = document.createElement('tr');
        let item_id = key;
        let item_dict = fetch_table[key];
        let td_first_name = document.createElement('td');
        td_first_name.textContent = item_dict["first_name"];
        tr.appendChild(td_first_name);
        let td_last_name = document.createElement('td');
        td_last_name.textContent = item_dict["last_name"];
        tr.appendChild(td_last_name);

        let td_id = document.createElement('td');
        td_id.textContent = item_dict["professor_id"];
        tr.appendChild(td_id)
        tbody.appendChild(tr);
    });

    return tbody;
}

function createProfessorTableHead(table_head) {
    let thead = document.createElement('thead');
    let tr = document.createElement('tr');

    table_head.forEach(function (eachHead, index) {
       tr.appendChild(createProfessorEachTableHead(eachHead));
    });
    thead.appendChild(tr);
    return thead
}

function createProfessorEachTableHead(elementName) {
    let th = document.createElement('th');
    th.textContent = elementName;
    return th;
}

function extractProfessorTableHead(fetch_table) {
    let table_head = [];
    if (Object.keys(fetch_table).length === 0){
        return table_head;
    } else {
        table_head = Object.keys(fetch_table[Object.keys(fetch_table)[0]]);
        return table_head;
    }
}


document.addEventListener('DOMContentLoaded', () => {
    // const prof_table_selector = document.querySelector("#prof-table");
    // prof_table_selector.append(createTable(prof_dict));
    const table_selector = document.querySelector("#render-table");
    if (table_type === "professor") {
        professorTableRenderer(fetch_table);
    }else {
        console.log("gogogogo");
    }
});
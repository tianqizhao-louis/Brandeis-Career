document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("#operation-placeholder").style.display = 'none';

    const breadcrumb_selector = document.querySelector("#breadcrumb-control");
    breadcrumb_selector.appendChild(createBreadCrumb(table_type));

    const table_selector = document.querySelector("#render-table");

    if (table_type === "professor" || table_type === "gender" || table_type === "concentration" ||
        table_type === "job_merged_table" || table_type === "company" || table_type === "alumni") {
        table_selector.appendChild(createTable(table_type, table_columns, table_dict));
    }

    if (table_type === "professor" || table_type === "gender") {
        document.querySelector("#operation-placeholder").style.display = '';
        const insert_button_selector = document.querySelector("#insert-button-placeholder");
        insert_button_selector.appendChild(createInsertButton(table_type));
    }
});

function createInsertButton(table_type) {
    let insertButton = document.createElement('button');
    insertButton.classList.add("button");
    insertButton.classList.add("is-primary");
    insertButton.setAttribute("id", "insert-to-table");
    insertButton.textContent = "Insert A New Record";
    insertButton.addEventListener("click", function () {
        window.location.href = "/admin/table/insert/" + table_type;
    });
    return insertButton;
}

function createTableBody(table_head, table_dict) {
    let tbody = document.createElement('tbody');
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
    table_render.classList.add('table');
    table_render.classList.add('is-bordered');
    table_render.classList.add('is-striped');
    table_render.classList.add('is-narrow');
    table_render.classList.add('is-hoverable');
    table_render.classList.add('is-fullwidth');
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

function createBreadCrumb(table_type) {
    let bc = document.createElement('ul');

    let home_bc = document.createElement('li');
    let home_bc_link = document.createElement('a');
    home_bc_link.setAttribute('href', '/admin');
    home_bc_link.textContent = "Admin Portal";
    home_bc.appendChild(home_bc_link);

    bc.appendChild(home_bc);

    let table_bc = document.createElement('li');
    table_bc.classList.add('is-active');
    let table_bc_link = document.createElement('a');
    table_bc_link.setAttribute('href', '#');
    table_bc_link.setAttribute('aria-current', 'page');
    table_bc_link.textContent = table_type
    table_bc.appendChild(table_bc_link);

    bc.appendChild(table_bc);

    return bc;
}

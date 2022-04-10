document.addEventListener('DOMContentLoaded', () => {
    const property_selector = document.querySelector('#property-placeholder');
    if (table_type === "professor") {
        property_selector.appendChild(createProfessorForm(table_type));
        addProfessorSubmitButtonAction();
    }
});

function createProfessorForm(table_type) {
    let form = document.createElement('form');
    form.setAttribute("id", "professor-form");

    let field = document.createElement('div');
    field.classList.add("field");

    let first_name_label = document.createElement('label');
    first_name_label.classList.add("label");
    first_name_label.setAttribute("for", "firstName")
    first_name_label.textContent = "Professor First Name";
    field.appendChild(first_name_label);

    let first_name_input_div = document.createElement("div");
    first_name_input_div.classList.add("control");
    let first_name_input = document.createElement("input");
    first_name_input.classList.add("input")
    first_name_input.setAttribute("type", "text");
    first_name_input.setAttribute("placeholder", "First Name");
    first_name_input.setAttribute("name", "firstName");
    first_name_input_div.appendChild(first_name_input);
    field.appendChild(first_name_input_div);
    form.appendChild(field);


    field = document.createElement('div');
    field.classList.add("field");
    let last_name_label = document.createElement('label');
    last_name_label.classList.add("label");
    last_name_label.setAttribute("for", "lastName");
    last_name_label.textContent = "Professor Last Name";
    field.appendChild(last_name_label);

    let last_name_input_div = document.createElement("div");
    last_name_input_div.classList.add("control");
    let last_name_input = document.createElement("input");
    last_name_input.classList.add("input")
    last_name_input.setAttribute("type", "text");
    last_name_input.setAttribute("placeholder", "Last Name");
    last_name_input.setAttribute("name", "lastName");
    last_name_input_div.appendChild(last_name_input);
    field.appendChild(last_name_input_div);
    form.appendChild(field);

    field = document.createElement('div');
    field.classList.add("field");
    field.classList.add("is-grouped");
    let submit_button_control = document.createElement("div");
    submit_button_control.classList.add("control");
    let submit_button = document.createElement("button");
    submit_button.classList.add("button");
    submit_button.classList.add("is-link");
    submit_button.setAttribute("type", "submit");
    submit_button.textContent = "Submit";
    submit_button_control.appendChild(submit_button);

    let cancel_button_control = document.createElement("div");
    cancel_button_control.classList.add("control");
    let cancel_button = document.createElement("button");
    cancel_button.classList.add("button");
    cancel_button.classList.add("is-link");
    cancel_button.classList.add("is-light");
    cancel_button.textContent = "Cancel";
    cancel_button_control.appendChild(cancel_button);

    field.appendChild(submit_button_control);
    field.appendChild(cancel_button_control);
    form.appendChild(field)

    return form;
}

function addProfessorSubmitButtonAction() {
    const professorFormSelector = document.querySelector("#professor-form");
    professorFormSelector.addEventListener("submit", function (event) {
        event.preventDefault();

        const formDataTarget = new FormData(event.target);
        const jsonFormData = Object.fromEntries(formDataTarget.entries());
        sendProfessorAjax(jsonFormData);
    });
}

function sendProfessorAjax(jsonFormData) {
    const url = "/admin/table/insert/ajax/professor";

    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonFormData),
        mode: 'cors',
        credentials: 'same-origin',
        cache: 'no-cache'
    };

    fetch(url, requestOptions)
        .then(response => response.json())
        .then(data => {
            window.location.href = "/admin/table/professor";
        })
        .catch((error) => {
            retryFetch(url, requestOptions);
        });
}

function retryFetch(url, requestOptions) {
    fetch(url, requestOptions)
        .then(response => response.json())
        .then(data => {
            window.location.href = "/admin/table/professor";
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

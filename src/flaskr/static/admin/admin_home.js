document.addEventListener('DOMContentLoaded', () => {
    const manage_prof_button = document.querySelector("#professor_table");
    const manage_gender_button = document.querySelector("#gender_table");

    manage_prof_button.addEventListener("click", function () {
        window.location.href="/admin/table/professor";
    })

    manage_gender_button.addEventListener("click", function () {
        window.location.href="/admin/table/gender";
    })
});
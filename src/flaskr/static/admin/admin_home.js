document.addEventListener('DOMContentLoaded', () => {
    const manage_prof_button = document.querySelector("#professor_table");
    const manage_gender_button = document.querySelector("#gender_table");
    const manage_concentration_button = document.querySelector("#concentration_table");
    const manage_job_merged_table_button = document.querySelector("#job_merged_table");
    const manage_company_table_button = document.querySelector("#company_table");
    const manage_master_view = document.querySelector("#master-view");

    manage_prof_button.addEventListener("click", function () {
        window.location.href="/admin/table/professor";
    });

    manage_gender_button.addEventListener("click", function () {
        window.location.href="/admin/table/gender";
    });

    manage_concentration_button.addEventListener("click", function () {
        window.location.href="/admin/table/concentration";
    });

    manage_job_merged_table_button.addEventListener("click", function () {
       window.location.href="/admin/table/job-merged-table";
    });

    manage_company_table_button.addEventListener("click", function () {
       window.location.href="/admin/table/company";
    });

    manage_master_view.addEventListener("click", function () {
       window.location.href="/admin/table/alumni";
    });
});
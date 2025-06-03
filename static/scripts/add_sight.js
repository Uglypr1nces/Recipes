function checkValues() {
    const location = document.getElementById("location-name").value.trim();
    const date = document.getElementById("date").value.trim();
    const sas_amount = Number(document.getElementById("sas-amount").value);
    const description = document.getElementById("description").value.trim();
    const made_by = localStorage.getItem("first_name");

    if (location.length < 1
    ) {
        alert("Location name must be at least 1 character.");
        return false;
    }
    if (sas_amount === "" || isNaN(sas_amount) || Number(sas_amount) <= 1) {
        alert("Sasquatches amount must be a positive number and min.");
        return false;
    }
    if (description.length > 50) {
        alert("Description must be max 50 characters.");
        return false;
    }

    if (!date) {
        alert("Date is required.");
        return false;
    }

    if (!made_by){
        alert("user not logged in");
        window.location.href = "/login"
    }

    console.log("Input valid...");
    return true;

}
function addSight() {
    if (checkValues()) {
        const location = document.getElementById("location-name").value.trim();
        const date = document.getElementById("date").value.trim();
        const sas_amount = Number(document.getElementById("sas-amount").value);
        const description = document.getElementById("description").value.trim();
        const made_by = localStorage.getItem("first_name");

        $.ajax({
            type: "POST",
            url: "import_sight/",
            data: {
                location: location,
                date: date,
                sas_amount: sas_amount,
                description: description,
                made_by: made_by
            },
            success: function (data) {
                console.log("Sighting successfully added:", data);
                window.location.href = "/dashboard/";
            },
            error: function () {
                alert("Failed to add Sight.");
            },
        });
    }
}


function returnHome() {
  window.location.href = "/dashboard/";
}

function logout() {
    window.location.href = "/login/";
}
window.onload = checkLogged;

document.addEventListener("DOMContentLoaded", (event) => {
    const username = document.getElementById("site-username");
    username.textContent = "Welcome, " + localStorage.getItem("first_name");
});

function checkLogged() {
    if (localStorage.getItem("first_name") === null) {
        alert("You cant view the site unless youre logged in.");
        window.location.href = "/login/";

    } else {
        getSights();
    }
}

function getSights() {
    $.ajax({
        type: "GET",
        url: "get_sights/",
        success: function (data) {
            console.log("got sights")
            const tableBody = document.getElementById("sight-table-body");
            tableBody.innerHTML = "";

            data.forEach(sight => {
                const row = document.createElement("tr");

                if (sight.posted_by == localStorage.getItem("first_name")) {
                    row.innerHTML = `
                    <td>${sight.location}</td>
                    <td>${sight.posted_by}</td>
                    <td>${sight.date}</td>
                    <td>${sight.sas_amount}</td>

                    <td>
                        <button onclick="editSight(${sight.id})">Edit</button>
                        <button onclick="deleteSight(${sight.id})">Delete</button>
                    </td>
                `;
                } else{
                    row.innerHTML = `
                    <td>${sight.location}</td>
                    <td>${sight.posted_by}</td>
                    <td>${sight.date}</td>
                    <td>${sight.sas_amount}</td>

                    <td>
                        <button onclick="viewSight(${sight.id})">View</button>
                    </td>

                `;
                }
                tableBody.appendChild(row);
            });
        },
        error: function () {
            alert("Failed to fetch sights.");
        }
    });
}


function viewSight(id) {
    window.location.href = `/view_sight/?id=${encodeURIComponent(id)}`;
    console.log("viewing sights");
}

function editSight(id){
    window.location.href = `/edit_sight/?id=${encodeURIComponent(id)}`;
    console.log("Editing sight");
}

function deleteSight(id){
    $.ajax({
      type: "POST",
      url: "delete_sight",
      id: id,
      success: function () {
        console.log("deleting sight");
      },
      error: function () {
        alert("Failed to delete sight.");
      },
    });
}

function addSight() {
    window.location.href = "/add_sight/";
}

function logout() {
    window.location.href = "/login/";
}
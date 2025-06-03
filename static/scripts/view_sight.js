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
        const params = new URLSearchParams(window.location.search);
        const sightId = params.get('id');
        viewSight(sightId);
    }
}


function viewSight(id){
    $.ajax({
      type: "POST",
      url: "get_specific_sight/",
      data: { id: id },
      success: function (data) {
        document.getElementById("header").textContent = data.location + " & " + data.date;
        document.getElementById("description").textContent = "Description: " + data.description;
        document.getElementById("reported-by").textContent = "Reported by " + data.posted_by;
      },
      error: function () {
        alert("Failed to load sight. Please try again later.");
      },
    });
}

function returnHome() {
  window.location.href = "/dashboard/";
}

function logout() {
    window.location.href = "/login/";
}
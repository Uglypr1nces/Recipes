window.onload = getRecipes;

function addRecipe(){
    window.location.href = "/add_recipe/";
}

function logOut(){
    window.location.href = "/login/";
}

function getRecipes() {
    var title = document.getElementById("title");
    title.textContent = "Hello, " + localStorage.getItem("first_name");
    $.ajax({
        type: "GET",
        url: "/get_recipes/",
        success: function (data) {
            console.log("got data")
            const tableBody = document.getElementById("recipe-table-body");
            tableBody.innerHTML = ""; 

            data.forEach(recipe => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${recipe.name}</td>
                    <td>${recipe.under_30_minute ? "Under 30 min" : "Over 30 min"}</td>
                    <td>${recipe.posted_by}</td>
                    <td>
                        <button onclick="editRecipe(${recipe.id})">Edit</button>
                        <button onclick="deleteRecipe(${recipe.id})">Delete</button>
                    </td>
                `;

                tableBody.appendChild(row);
            });
        },
        error: function () {
            alert("Failed to fetch recipes.");
        }
    });
}


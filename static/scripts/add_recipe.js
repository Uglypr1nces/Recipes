function goBack(){
    window.location.href = "/recipes/";
}

function logOut(){
    window.location.href = "/login/";
}

function addRecipe() {
    const recipe_name = document.getElementById("recipe-name").value.trim();
    const description = document.getElementById("description").value.trim();
    const instructions = document.getElementById("instructions").value.trim();
    const date = document.getElementById("date").value.trim();
    const time_required_elem = document.querySelector('input[name="time_required"]:checked');
    const made_by = localStorage.getItem("first_name");

    if (!recipe_name || !description || !instructions || !date || !time_required_elem || !made_by) {
        alert("Please fill in all fields.");
        return;
    }

    const time_required = time_required_elem.value;
    console.log(made_by);
    $.ajax({
        type: "POST",
        url: "create_recipe/",
        data: {
            recipe_name: recipe_name,
            description: description,
            instructions: instructions,
            date: date,
            time_required: time_required,
            first_name: made_by,
        },
        success: function (data) {
            console.log("Recipe successfully added:", data);
        },
        error: function () {
            alert("Failed to add recipe.");
        },
    });
}

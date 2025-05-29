function signUp(){
    const first_name = document.getElementById("firstname");
    const last_name = document.getElementById("lastname");
    const email = document.getElementById("sign-up-email");
    const password = document.getElementById("sign-up-password");

    if (
        !first_name.value.trim() ||
        !last_name.value.trim() ||
        !email.value.trim() ||
        !password.value.trim()
    ) {
        alert("Please fill in all fields.");
    } else{
        $.ajax({
              type: "POST",
              url: "sign_up/",
              data: {
                first_name: first_name.value,
                last_name: last_name.value,
                email: email.value,
                password: password.value,
              },
              success: function (data) {
                console.log(data)
              },
              error: function () {
                alert("Failed to verify user.");
              },
         });
    }
}

function logIn(){
    const email = document.getElementById("log-in-email");
    const password = document.getElementById("log-in-password");

    if (
        !email.value.trim() ||
        !password.value.trim()
    ) {
        alert("Please fill in all fields.");
    } else{
        $.ajax({
              type: "POST",
              url: "log_in/",
              data: {
                email: email.value,
                password: password.value,
              },
              success: function (data) {
                if (data == "Couldn't find user"){
                    alert("User wasnt found, please try again");
                }else{
                alert("Greetings " + data);
                localStorage.setItem("first_name", data);
                window.location.href = "/recipes/";
                }
              },
              error: function () {
                alert("Failed to verify user.");
              },
         });
    }
}
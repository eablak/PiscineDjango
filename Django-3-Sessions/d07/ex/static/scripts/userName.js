function fetchUserName(){
    fetch("/username_ajax/").then(
        response => response.json()).then(
            data => {
                console.log(data);
                document.getElementById("username").innerText = "Hello " + data.name + "!";
            }).catch(
                error => console.error("Error: ", error));
};

setInterval(fetchUserName, 1000);
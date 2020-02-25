document.querySelector(".apireq")
    .addEventListener("click", function () {
        fetch("http://127.0.0.1:8000/apireservasservicios/", {
            headers: {
                'Content-Type': 'application/json',
            }
        }).then(res => res.json())
            .then(data => {

                data.forEach(element => {
                    let p = document.createElement("p");
                    p.innerHTML = `datos: ${element.servicio} ${element.costo}`
                    document.querySelector("#jsonresp").appendChild(p);
                });
            })
            .catch(error => console.error('Error:', error));
    })

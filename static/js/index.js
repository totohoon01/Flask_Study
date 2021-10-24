const btn = document.getElementById("getName");
const username = document.getElementById("name");

btn.onclick = () =>{
  fetch("/", {
    method: "POST",
    body: {"Name" : "Please"}
  })
  .then((res) => {
    return res.json()
  })
  .then((data) =>{
    username.innerText = data['name'] + "!!";
  });
};
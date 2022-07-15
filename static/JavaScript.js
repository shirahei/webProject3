//print date to log
const d = Date();
console.log(d);

//pull the pathname from window location
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav,
compare each to pathname and mark the one that is active
*/
const links = document.querySelectorAll('nav a').forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');
    }
});

function NewUser() {
    alert('User added successfully')
}

function getUser() {
  var id = document.getElementById("frontend_id").value;
  fetch('https://reqres.in/api/users/' + id.toString())
    .then(result => result.json())
    .then((output) => {
      const myJSON = JSON.stringify(output);
      document.getElementById("userdata").innerHTML = myJSON;
    }).catch(err => console.error(err));
  document.getElementById("userdata").innerHTML = "Cant Find User";



}
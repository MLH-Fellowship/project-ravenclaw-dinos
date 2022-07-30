// POST form data using JavaScript’s Fetch API
const form = document.getElementById('timeline_form');
/* Sending the URL-encoded string as payload using Fetch */
form.addEventListener('submit', function(e) {
    // Prevent default behavior:
    e.preventDefault();

    // Create new FormData object:
    const formData = new FormData(form);
    // Convert formData object to URL-encoded string:
    const payload = new URLSearchParams(formData);

    console.log([...payload]);

    // Post the payload using Fetch:
    fetch('/api/timeline_post', {
        method: 'POST',
        body: payload
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err))
    .finally(function () {
        setTimeout(function(){
            window.location.reload();}, 100);
        })
})

// api url
const api_url = '/api/timeline_post'; 

// Defining async function
async function getapi(url) {

    // Storing response
    const response = await fetch(url);

    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    show(data);
}
// Calling that async function
getapi(api_url);

// Function to define innerHTML for HTML table
function show(data) {
    let tab =
        `<tr>
        <th>Name</th>
        <th>Email</th>
        <th>Content</th>
        </tr>`;
    
    // Loop to access all rows
    for (let r of data.timeline_posts) {
        tab += `<tr>
        <td>${r.name} </td>
        <td>${r.email}</td>
        <td>${r.content}</td>
        </tr>`;
    }

    // Setting innerHTML as tab variable
    document.getElementById("timeline_table").innerHTML = tab;
}
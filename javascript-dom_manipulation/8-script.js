const response = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr').then((response) =>
    response.json().then((data) => updateHeader(data['hello']))
);

function updateHeader(data) {
    const header = document.querySelector('#hello');
    header.innerHTML = data;
}

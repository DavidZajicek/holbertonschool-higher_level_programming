const response = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json').then((response) =>
    response.json().then((data) => populateCharacter(data))
);

function populateCharacter(obj) {
    console.log(obj);
    const character = document.querySelector('#character');
    character.innerHTML = obj.name;
}

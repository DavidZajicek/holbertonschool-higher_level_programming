const header = document.querySelector('header');
const red_id = document.querySelector('#red_header');
red_id.addEventListener('click', () => {
    header.style.color = '#FF0000';
    header.className = 'red';
});

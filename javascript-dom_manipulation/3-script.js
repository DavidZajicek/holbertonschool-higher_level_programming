const toggle_header = document.querySelector('#toggle_header');
toggle_header.addEventListener('click', () => {
    let header = document.querySelector('header');
    if (header.className == 'green') {
        header.className = 'red';
    } else {
        if (header.className == 'red') {
            header.className = 'green';
        }
    }
});

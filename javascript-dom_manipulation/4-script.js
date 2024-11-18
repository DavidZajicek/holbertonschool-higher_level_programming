const add_item = document.querySelector('#add_item');
const list = document.querySelector('.my_list');
add_item.addEventListener('click', () => {
    const child = document.createElement('li');
    child.textContent = 'Item';
    list.appendChild(child);
});

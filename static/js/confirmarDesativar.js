const button = document.getElementsByClassName('right_desactivate-button')[0];

button.addEventListener('click',(e) => {
    let ballon = document.getElementsByClassName('right_confirm')[0];
    console.log(ballon);
    if (ballon.style.display === "none"){
        ballon.style.display = 'block';
    } else {
        ballon.style.display = 'none';
    }
    e.preventDefault();
});

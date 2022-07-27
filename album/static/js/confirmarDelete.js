

const button = document.getElementById('deletarPost')

button.addEventListener('click',(e) => {
    let ballon = document.getElementsByClassName('confirm')[0];
    console.log(ballon);
    ballon.style.display = 'block';
    e.preventDefault();
});

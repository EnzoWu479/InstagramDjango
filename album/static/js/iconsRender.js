import icons from "./icons.js"

for (let key in icons){
    let listIconsContainer = [...document.getElementsByClassName(key)]
    listIconsContainer.forEach(element => {
        if (element.nodeName === "I"){
            element.innerHTML = icons[key];
        };
    });
};
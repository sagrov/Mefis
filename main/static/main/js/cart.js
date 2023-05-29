// let openShopping = document.querySelector('.shopping');
// let closeShopping = document.querySelector('.closeShopping');
// let list = document.querySelector('.list');
// let listCard = document.querySelector('.listCard');
// let body = document.querySelector('body');
// let total = document.querySelector('.total');
// let quantity = document.querySelector('.quantity');
//
// openShopping.addEventListener('click', ()=> {
//     body.classList.add('focus');
// })
//
// closeShopping.addEventListener('click', ()=> {
//     body.classList.remove('active');
// })
//
// let listCards = []
// function addToCard(key) {
//     if(listCards[key] == null) {
//         listCards[key] = products[key];
//         listCards[key].quantity = 1
//     }
//     reloadCard();
// }

function ready() {
    var removeCartButtons = document.getElementsByClassName('delete-button')
    console.log(removeCartButtons)
    for (var i = 0; i < removeCartButtons.length; i++) {
        var button = removeCartButtons[i]
        button.addEventListener('click', removeCartItem);
    }
}

function removeCartItem(event) {
    var buttonCicked = event.target
    buttonCicked.parentElement.remove()
}
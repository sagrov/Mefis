let counter = 1;

const counterValue = document.getElementById('counter-value');
const incrementBtn = document.getElementById('increment-btn');
const decrementBtn = document.getElementById('decrement-btn');

incrementBtn.addEventListener('click', () => {
    counter++;
    counterValue.innerHTML = counter;
});

decrementBtn.addEventListener('click', () => {
    if (counter == 1) {
        return counter = 1;
    }
    else {
        counter--;
    }
    counterValue.innerHTML = counter;
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// let btns = document.querySelectorAll(".btn-primary")
let btns = document.querySelectorAll(".add")

btns.forEach(btn => {
    btn.addEventListener("click", addToCart)
})

function addToCart(e) {
    let product_id = e.target.value
    let url = "/add_to_cart"
    let data = {id: product_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.log(error)
        })
}

let buttons = document.querySelectorAll(".remove")

buttons.forEach(button => {
    button.addEventListener("click", removeFromCart)
})

function removeFromCart(e) {
    let product_id = e.target.value
    let url = "/remove_from_cart"
    let data = {id: product_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.log(error)
        })
}

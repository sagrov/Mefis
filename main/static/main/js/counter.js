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

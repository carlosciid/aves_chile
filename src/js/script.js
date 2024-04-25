var currentCount = 20; // Start showing 20 cards initially
function mostrarMas() {
    var cards = document.getElementsByClassName('card');
    for (var i = currentCount; i < currentCount + 20 && i < cards.length; i++) {
        cards[i].style.display = 'block';
    }
    currentCount += 20;
    if (currentCount >= cards.length) {
        document.querySelector('button').style.display = 'none'; // Hide button if no more cards to show
    }
}

function hoverRightOn() {
    let fillArrow = document.getElementById('next-fill');
    let nofillArrow = document.getElementById('next-nofill');

    fillArrow.classList.toggle('d-none');
    nofillArrow.classList.toggle('d-none');
}

function hoverRightOff() {
    let fillArrow = document.getElementById('next-fill');
    let nofillArrow = document.getElementById('next-nofill');

    fillArrow.classList.toggle('d-none');
    nofillArrow.classList.toggle('d-none');
}


function hoverLeftOn() {
    let fillArrow = document.getElementById('prev-fill');
    let nofillArrow = document.getElementById('prev-nofill');

    fillArrow.classList.toggle('d-none');
    nofillArrow.classList.toggle('d-none');
}

function hoverLeftOff() {
    let fillArrow = document.getElementById('prev-fill');
    let nofillArrow = document.getElementById('prev-nofill');

    fillArrow.classList.toggle('d-none');
    nofillArrow.classList.toggle('d-none');
}

// The Operators

/////////////////////////////////////////////////////////

function xgate() {

    const elem = document.getElementById("myQops");
    let pos3 = 0;

    setInterval(frame, 4);
    setInterval(frame2, 5)

    function frame() {
        if (pos3 < 160) {
            pos3++;
            elem.style.top = pos3 + 'px';
        }
    }
    function frame2() {
        if (pos3 < 190) {
            pos3++;
            elem.style.top = pos3 + 'px';

        }

    }
}

function hadamard() {

    const elem = document.getElementById("myQops2");
    let pos3 = 0;

    setInterval(frame, 1);

    function frame() {
        if (pos3 < 275) {
            pos3++;
            elem.style.top = pos3 + 'px';
        }

    }

}


function newFunct() {
    xgate();
}

function newFunct2() {
    hadamard()
}
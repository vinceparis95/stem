
// The Operators




/////////////////////////////////////////////////////////

function xgate() {

    const elem = document.getElementById("myQops");
    let pos3 = 0;
    let R = 163; let G = 166; let B = 255;

    setInterval(frame, 9);
    setInterval(frame2, 5)

    function frame() {
        if (pos3 < 172) {
            pos3++;
            elem.style.top = pos3 + 'px';
            elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            R = R + 1;
            G = G + 2;
            B = B + 1;
        }

    }
    function frame2() {
        if (pos3 < 169) {
            pos3++;
            elem.style.top = pos3 + 'px';
            elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            R = R + 1;
            G = G + 2;
            B = B + 1;
        }

    }
}

function hadamard() {

    const elem = document.getElementById("myQops2");
    let pos3 = 0;
    let R = 163; let G = 166; let B = 255;


    setInterval(frame, 3);


    function frame() {
        if (pos3 < 314) {
            pos3++;
            elem.style.top = pos3 + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 1;
            // G = G + 2;
            // B = B + 1;
        }

    }

}





function newFunct() {
    xgate();
}

function newFunct2() {
    hadamard()
}
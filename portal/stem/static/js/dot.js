

function myMove() {
    const elem = document.getElementById("myAnimation2");
    let pos3 = 0;
    let pos4 = 0;
    let pos7 = 0;
    let pos8 = 0;
    let R = 163;
    let G = 166;
    let B = 255;

    setInterval(frame, 9);

    function frame() {
        if (pos3 < 180) {
            pos3++;
            elem.style.top = pos3 + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 0.1;
            // G = G + 0.2;
            // B = B + 0.1;
        } else if (pos3 == 180) {
            pos3++
        } else if (pos3 > 180 && pos4 < 180) {
            pos4++;
            elem.style.top = pos4 + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 0.1;
            // G = G + 0.2;
            // B = B + 0.1;
        } else if (pos4 == 180) {
            elem.style.bottom = 0;
            elem.style.left = 180 + 'px';
            pos4++
        } else if (pos4 > 180 && pos7 < 180) {
            pos7++;
            elem.style.top = pos7 + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 0.1;
            // G = G + 0.2;
            // B = B + 0.1;
        } else if (pos7 <= 180 && pos8 < 180) {
            pos8++;
            elem.style.top = pos8 + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 0.1;
            // G = G + 0.1;
            // B = B + 0.1;
        }
    }
}



function myMove2() {
    const elem = document.getElementById("myAnimation");
    let pos = 0; let pos2 = 0; let pos5 = 0; let pos6 = 0;
    let R = 163; let G = 166; let B = 255;

    setInterval(frame, 9);

    function frame() {
        if (pos < 180) {
            pos++;
            elem.style.left = pos + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 0.1; G = G + 0.2; B = B + 0.1;
        } else if (pos == 180) {
            elem.style.top = 180+'px';
            pos++
        } else if (pos > 180 && pos2 < 180) {
            pos2++;
            elem.style.left = pos2 + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 0.1; G = G + 0.2; B = B + 0.1;
        }
        else if (pos2 == 180) {
            pos2++
            elem.style.top = 0 + 'px'
        } else if (pos2 > 180 && pos5 < 180) {
            pos5++;
            elem.style.left = pos5+'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R +0.1; G = G + 0.2; B = B + 0.1;
        }
        else if (pos5 >= 180 && pos6 < 180) {
            pos6++;
            elem.style.top = '180px';
            elem.style.left = pos6 + 'px';
            // elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            // R = R + 0.1; G = G + 0.2; B = B + 0.1;
        }


    }
}

function newFunction() {
    myMove();
    myMove2()
}



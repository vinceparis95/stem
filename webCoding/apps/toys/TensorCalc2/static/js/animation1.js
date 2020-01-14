
function myMove() {

    const elem = document.getElementById("myAnimation");
    let pos = 0;
    let id = setInterval(frame, 5);


    let R = 0;
    let G = 0;
    let B = 90;

    full = 0;


    function frame() {
    // if (pos == 180) {
    //     elem.style.top = 0 + 'px';
    //     elem.style.right = 0;
    //     clearInterval(id);
    //     }
    // else {
    //     pos++;
    //     elem.style.top = pos + 'px';
    //     let rgbColor = "rgb(" + R + ", " + G + ", " + B + ")";
    //     elem.style.backgroundColor = rgbColor;
    //     R = R + 1;
    //     G = G + 2;
    //     B = B + 1;
    //     }

        if (pos <181) {
            pos++;
            elem.style.top = pos + 'px';
            let rgbColor = "rgb(" + R + ", " + G + ", " + B + ")";
            elem.style.backgroundColor = rgbColor;
            R = R + 1;
            G = G + 2;
            B = B + 1;
        }
        else if (pos >=181 && pos < 360) {
            elem.style.right= 0;
            pos++;
            elem.style.top = 0 + 'px';
            let rgbColor = "rgb(" + R + ", " + G + ", " + B + ")";
            elem.style.backgroundColor = rgbColor;
            R = R + 1;
            G = G + 2;
            B = B + 1;
        }
        else if (pos == 360){

            clearInterval(id);
        }


  }
}
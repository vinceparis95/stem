//
// function myMove() {
//
//     const elem = document.getElementById("myAnimation");
//     let pos = 0;
//     let R = 0;
//     let G = 0;
//     let B = 60;
//     setInterval(frame, 5);
//
//     function frame() {
//
//         if (pos < 180) {
//             pos++;
//             elem.style.top = pos + 'px';
//             let rgbColor = "rgb(" + R + ", " + G + ", " + B + ")";
//             elem.style.backgroundColor = rgbColor;
//             R = R + 1;
//             G = G + 2;
//             B = B + 1;
//         }
//     }
// }

//
// function myMove2() {
//
//     const elem = document.getElementById("myAnimation");
//     let pos = 0;
//     let R = 0;
//     let G = 0;
//     let B = 60;
//     setInterval(frame, 5);
//
//     function frame() {
//
//         if (pos < 180) {
//             pos++;
//             elem.style.top = pos + 'px';
//             let rgbColor = "rgb(" + R + ", " + G + ", " + B + ")";
//             elem.style.backgroundColor = rgbColor;
//             R = R + 1;
//             G = G + 2;
//             B = B + 1;
//         }
//     }
// }



function myMove() {
    const elem = document.getElementById("myAnimation");
    let pos = 0;
    let R = 90;
    let G = 95;
    let B = 190;
    let pos2 = 0

    setInterval(frame, 10);

    function frame() {
        if (pos < 180) {
            pos++;
            elem.style.top = pos + 'px';
            elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            R = R + 1;
            G = G + 2;
            B = B + 1;
        } else if (pos == 180) {
            elem.style.right = 0;
            elem.style.top = 0;
            pos++
        } else if (pos > 180 && pos2 < 180) {
            pos2++;
            elem.style.top = pos2 + 'px';
            elem.style.backgroundColor = "rgb(" + R + ", " + G + ", " + B + ")";
            R = R + 1;
            G = G + 2;
            B = B + 1;

        }

    }

}




function newFunction() {
    myMove();

}



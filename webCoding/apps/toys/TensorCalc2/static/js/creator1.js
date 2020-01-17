//
//
//
//
// // Spring drawing constants for top bar
//   let qopsheight = 9,
//       qopsdist = 60,
//       left, right,
//       maxHeight = 300,
//       minHeight = 0,
//       over = false,
//       move = false;
//       move_qops = 0;
//
// // Spring simulation constants
//   let M = 0.8,  // Mass
//       K = 0.3,  // Spring constant
//       D = 0.94, // Damping
//       R = 90;  // Rest position
//
//   let qops = [];
//
//
// /////////////////////////////////////////////////////////
//
//
//   function setup() {
//     create(360, 360);
//     rectMode(CORNERS);
//     co = color('rgb(255,200,252)');
//     fill(co);
//     noStroke();
//     left = width / 2 - 400;
//     right = width / 2 + 400;
//     for (let i = 0; i < 4; ++i) {
//       let psq = R + qopsheight * i;
//       qops.push({psq : psq, vs : 0.0, as : 0, f : 0, R : ps})
//     }
//   }
//
//
// //////////////////////////////////////////////////////////
//
//
//   function draw() {
//
//     updateQops();
//     drawQops();
//
//   }
//
//   function drawQops() {
//     for (let i = 0; i < qops.length; ++i) {
//       let y = qops[i].psq;
//       rect(left, y, right, y+qopsheight);
//     }
//   }
//
//   function updateQops() {
//     // Update the spring position
//     for (let i = 0; i < qops.length; ++i) {
//       let st = qops[i];
//
//       if ( i != move_qops || !move ) {
//         st.f = -K * ( st.psq - st.R ); // f=-ky
//         st.as = st.f / M;             // Set the acceleration, f=ma == a=f/m
//         st.vs = D * (st.vs + st.as);  // Set the velocity
//         st.psq = st.psq + st.vs;        // Updated position
//       }
//
//       if (abs(st.vs) < 0.1) {
//         st.vs = 0.0;
//       }
//     }
//
//     // Test if mouse if over the top bar
//     over = false;
//       for (let i = 0; i < qops.length; ++i) {
//       let y = qops[i].psq
//       if (mouseX > left && mouseX < right && mouseY > y && mouseY < y + springHeight) {
//         over = true;
//         move_qops = i;
//       }
//     }
//
//     // Set and constrain the position of top bar
//     if (move) {
//       qops[move_qops].psq = mouseY - qopsheight / 2;
//       qops[move_qops].psq = constrain(qops[move_qops].psq, minHeight, maxHeight);
//     }
//   }
//
//   function mousePressed() {
//     if (over) {
//       move = true;
//     }
//   }
//
//   function mouseReleased() {
//     move = false;
//   }
//



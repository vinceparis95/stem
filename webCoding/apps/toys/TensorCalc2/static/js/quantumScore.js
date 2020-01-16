////////////////////////////////////////////////////////


// The Wires and the Score board


// Spring drawing constants for top bar
let springHeight = 9,
    springDist = 60,
    left,
    right,
    maxHeight = 300,
    minHeight = 0,
    over = false,
    move = false;
    move_i = 0;


// Spring simulation constants
let M = 0.8,  // Mass
    K = 0.3,  // Spring constant
    D = 0.94, // Damping
    R = 90;  // Rest position

// Spring simulation variables
let strings = [];
// let ps = R,   // Position
//     vs = 0.0, // Velocity
//     as = 0,   // Acceleration
//     f = 0;    // Force


function setup() {
    createCanvas(360, 360);
    rectMode(CORNERS);
    c = color('rgb(193, 255, 130)');
    fill(c);
    noStroke();
    left = width / 2 - 400;
    right = width / 2 + 400;

    for (let i = 0; i < 4; ++i) {
        let ps = R + springDist * i;
        strings.push({ps : ps, vs : 0.0, as : 0, f : 0, R : ps})
    }
}


function draw() {
    background(191, 209, 255);
    updateSpring();
    drawWire();
}

function drawWire() {
    for (let i = 0; i < strings.length; ++i) {
        let y = strings[i].ps;
        rect(left, y, right, y+springHeight);
    }
}

function updateSpring() {
    // Update the spring position
    for (let i = 0; i < strings.length; ++i) {
        let st = strings[i];

        if ( i != move_i || !move ) {
            st.f = -K * ( st.ps - st.R ); // f=-ky
            st.as = st.f / M;             // Set the acceleration, f=ma == a=f/m
            st.vs = D * (st.vs + st.as);  // Set the velocity
            st.ps = st.ps + st.vs;        // Updated position
        }

        if (abs(st.vs) < 0.1) {
            st.vs = 0.0;
        }
    }

    // Test if mouse if over the top bar
    over = false;
    for (let i = 0; i < strings.length; ++i) {
        let y = strings[i].ps
        if (mouseX > left && mouseX < right && mouseY > y && mouseY < y + springHeight) {
            over = true;
            move_i = i;
        }
    }

    // Set and constrain the position of top bar
    if (move) {
        strings[move_i].ps = mouseY - springHeight / 2;
        strings[move_i].ps = constrain(strings[move_i].ps, minHeight, maxHeight);
    }
}

function mousePressed() {
  if (over) {
    move = true;
  }
}

function mouseReleased() {
  move = false;
}
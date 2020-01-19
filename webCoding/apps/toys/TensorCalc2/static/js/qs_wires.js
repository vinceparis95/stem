
///////////////////////////////////////////////////


// The Wires and Ops


// wire constants
let springHeight = 12,
    springDist = 60,
    left, right,
    maxHeight = 300,
    minHeight = 0,
    over = false,
    move = false;
    move_i = 0;

// wire physics constants
let M = 0.7,  // Mass
    K = 0.3,  // Spring constant
    D = 0.94, // Damping
    R = 90;  // Rest position

// empty strings array
let strings = [];




/////////////////////////////////////////////////////////


// the Setup Method
function setup() {
    createCanvas(360, 360);
    rectMode(CORNERS);
    fill(146, 255, 69);
    noStroke();
    left = width / 2 - 400;
    right = width / 2 + 400;
    for (let i = 0; i < 4; ++i) {
        let ps = R + springDist * i;
        strings.push({ps: ps, vs: 0.0, as: 0, f: 0, R: ps})
    }
    x = width / 2;
    y = springHeight;
}

//////////////////////////////////////////////////////////


function draw() {
    background(191, 219, 255);
    updateSpring();
    drawWire(4);
}

function drawWire(input) {
    for (let i = 0; i < input; ++i) {
        let y = strings[i].ps;
        rect(left, y, right, y+springHeight);
    }
}



/////////////////////////////////////////////////////////////



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
    move = true
  }
}

function mouseReleased() {
  move = false;

}

///////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////


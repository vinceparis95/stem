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
    K = 0.2,  // Spring constant
    D = 0.95, // Damping
    R = 100;  // Rest position

// Spring simulation variables
let ps = R,   // Position
    vs = 0.0, // Velocity
    as = 0,   // Acceleration
    f = 0;    // Force

function setup() {
    createCanvas(710, 400);
    rectMode(CORNERS);
    // rectMode(CORNER);
    c = color('rgb(255,233,234)');
    fill(c);
    noStroke();
    left = width / 2 - 400;
    right = width / 2 + 400;
}

function draw() {
    background(102);
    updateSpring();
    drawWires();
}

function drawWires() {
    for (let i = 0; i < 4; ++i) {
        let y = ps + springDist * i;
        rect(left, y, right, y+springHeight);
    }
}

function updateSpring() {
    // Update the spring position
    if ( !move ) {
        f = -K * ( ps - R ); // f=-ky
        as = f / M;          // Set the acceleration, f=ma == a=f/m
        vs = D * (vs + as);  // Set the velocity
        ps = ps + vs;        // Updated position
    }

    if (abs(vs) < 0.1) {
        vs = 0.0;
    }

    // Test if mouse if over the top bar
    over = false;
    for (let i = 0; i < 3; ++i) {
        let y = ps + springDist * i;
        if (mouseX > left && mouseX < right && mouseY > y && mouseY < y + springHeight) {
            over = true;
            move_i = i;
        }
    }

    // Set and constrain the position of top bar
    if (move) {
        ps = mouseY - springHeight / 2 - move_i * springDist;
        ps = constrain(ps, minHeight, maxHeight);
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
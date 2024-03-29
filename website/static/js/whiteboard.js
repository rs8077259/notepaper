// Get the canvas element and its context
const canvas = document.getElementById('whiteboard');
const context = canvas.getContext('2d');
canvas.height = window.height
canvas.width = window.width
// Set the canvas size

        // Set initial drawing style
context.strokeStyle = 'black';
context.lineWidth = 2;
context.lineCap = 'round';

        // Variable to track if the mouse is being pressed
let isDrawing = false;

        // Event listeners for mouse actions
canvas.addEventListener('touchstart', startDrawing);
canvas.addEventListener('touchmove', draw);
canvas.addEventListener('touchend', stopDrawing);
canvas.addEventListener('touchcancel', stopDrawing);

        // Function to start drawing
function startDrawing(e) {
    console.log("holla");
    e.preventDefault()
    isDrawing = true;
    draw(e); // Start drawing from the current mouse position
}

        // Function to draw on the canvas
function draw(e) {
    console.log("holla2");
    e.preventDefault()
    if (!isDrawing) return;
    e.clientX=e.touches[0].clientX;
    e.clientY=e.touches[0].clientY;

    context.lineTo(e.clientX, e.clientY);
    context.stroke();
    context.beginPath();
    context.arc(e.clientX, e.clientY, context.lineWidth / 2, 0, Math.PI * 2);
    context.fill();
    context.beginPath();
    context.moveTo(e.clientX, e.clientY);
}

        // Function to stop drawing
function stopDrawing(e) {
    e.preventDefault()
    isDrawing = false;
    context.beginPath(); // Start a new path when the mouse is released
}

// Resize the canvas when the window is resized
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
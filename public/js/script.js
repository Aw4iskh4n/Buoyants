// Get elements
const navLinks = document.querySelector('.nav-links');
const hamburger = document.getElementById('fries');

// Toggle navigation
hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('nav-active');

    // Hamburger animation
    hamburger.classList.toggle('toggle');
});

window.onload = function() {
    if (window.innerWidth > 620) {
        var rightDiv = document.getElementsByClassName("right-div")[0];
        var image = document.getElementsByClassName("left-div")[0];

        // Set the height of rightDiv to match the height of the image
        rightDiv.style.height = image.offsetHeight + "px";
    }
};




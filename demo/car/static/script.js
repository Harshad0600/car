// const menu = document.getElementById("nav-menu");
// const navLinks = document.getElementById("nav-links")
// const menuIcon = document.querySelector("i")
// menu.addEventListener("click",() => {
//     navLinks.classList.toggle("open")

//     const isOpen =  navLinks.classList.contains("open");
//     menuIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
// });

// navLinks.addEventListener("click", () => {
//     navLinks.classList.remove("open");
//     menuIcon.setAttribute("class", "ri-menu-line");
// });

const header = document.querySelector("header");
window.addEventListener ("scroll", function() {
    header.classList.toggle ("sticky", window.scrollY > 0)
});

document.addEventListener('DOMContentLoaded', function() {
    var messagesContainer = document.querySelector('.messages');
    if (messagesContainer) {
        // Trigger reflow to ensure the transition works
        messagesContainer.offsetHeight;
        
        // Add 'show' class to slide in
        messagesContainer.classList.add('show');

        // Remove the message after 5 seconds
        setTimeout(function() {
            messagesContainer.classList.remove('show');
            // Remove the element from DOM after the transition
            setTimeout(function() {
                messagesContainer.remove();
            }, 500);
        }, 5000);
    }
});
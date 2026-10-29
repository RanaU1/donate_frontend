
(() => {
    const elements = document.querySelectorAll("[data-typing]");

    elements.forEach((element) => {
        const text = element.dataset.typing || element.textContent.trim();

        const speed = Number(element.dataset.typingSpeed) || 65;
        const deleteSpeed = Number(element.dataset.deleteSpeed) || 30;
        const pause = Number(element.dataset.typingPause) || 5000;

        const reducedMotion = window.matchMedia(
            "(prefers-reduced-motion: reduce)"
        ).matches;

        if (reducedMotion) {
            element.textContent = text;
            return;
        }

        element.textContent = "";
        element.classList.add("typing");

        let index = 0;
        let deleting = false;

        function animate() {
            element.textContent = text.slice(0, index);

            if (!deleting) {
                // Type the next character
                if (index < text.length) {
                    index++;
                    setTimeout(animate, speed);
                } else {
                    // Wait before deleting
                    deleting = true;
                    setTimeout(animate, pause);
                }
            } else {
                // Delete one character at a time
                if (index > 0) {
                    index--;
                    setTimeout(animate, deleteSpeed);
                } else {
                    // Start typing again
                    deleting = false;
                    setTimeout(animate, 400);
                }
            }
        }

        animate();
    });
})();

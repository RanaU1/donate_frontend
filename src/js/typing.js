
(() => {
    const elements = document.querySelectorAll("[data-typing]");

    elements.forEach((element) => {
        const text = element.dataset.typing || element.textContent.trim();
        const speed = Number(element.dataset.typingSpeed) || 65;
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

        function typeNext() {
            if (index >= text.length) {
                element.classList.add("typing-done");
                return;
            }

            element.textContent += text.charAt(index);
            index++;
            setTimeout(typeNext, speed);
        }

        typeNext();
    });
})();

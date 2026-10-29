document.querySelectorAll("[data-copy]").forEach((btn) => {
  btn.addEventListener("click", async () => {
    await copyText(btn.dataset.copy);
    btn.classList.add("done");
    btn.textContent = "Copied";
    showToast(btn.dataset.label + " copied");
    setTimeout(() => { btn.classList.remove("done"); btn.textContent = "Copy"; }, 1800);
  });
});

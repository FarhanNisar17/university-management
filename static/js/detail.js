const acc = document.querySelectorAll(".accordion");

acc.forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.classList.toggle("active");

    const panel = btn.nextElementSibling;
    const arrow = btn.querySelector(".arrow");

    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
});

document.querySelectorAll(".panel").forEach((panel) => {
  const select = panel.querySelector(".sort-select");
  const table = panel.querySelector("table");
  if (!select || !table) return;

  select.addEventListener("change", () => {
    const col = Number(select.value);
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));

    const sorted = rows.sort((a, b) => {
      let A = a.children[col].innerText.trim();
      let B = b.children[col].innerText.trim();

      // Convert to numbers if possible
      if (!isNaN(A) && !isNaN(B)) {
        return A - B;
      }

      // Date detection
      if (/^\d{4}-\d{2}-\d{2}$/.test(A) && /^\d{4}-\d{2}-\d{2}$/.test(B)) {
        return new Date(A) - new Date(B);
      }

      // Default → string compare
      return A.localeCompare(B);
    });

    sorted.forEach((row) => tbody.appendChild(row));
  });
});

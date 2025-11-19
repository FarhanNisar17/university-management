// Accordion toggle
document.querySelectorAll(".accordion").forEach((acc) => {
  acc.addEventListener("click", () => {
    acc.classList.toggle("active");
    const panel = acc.nextElementSibling;

    panel.style.display = panel.style.display === "block" ? "none" : "block";

    const arrow = acc.querySelector(".arrow");
    if (arrow)
      arrow.style.transform =
        panel.style.display === "block" ? "rotate(90deg)" : "rotate(0deg)";
  });
});

// Sorting per table
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

      if (!isNaN(A) && !isNaN(B)) return A - B;
      if (/^\d{4}-\d{2}-\d{2}$/.test(A)) return new Date(A) - new Date(B);
      return A.localeCompare(B);
    });

    sorted.forEach((r) => tbody.appendChild(r));
  });
});

// Profile → Edit/Delete popup
document.querySelectorAll(".profile-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const id = btn.dataset.id;

    Swal.fire({
      title: "Student Options",
      showCancelButton: true,
      showDenyButton: true,
      confirmButtonText: "Edit",
      denyButtonText: "Delete",
      cancelButtonText: "Close",
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = `/students/edit/${id}`;
      } else if (result.isDenied) {
        window.location.href = `/students/delete/${id}`;
      }
    });
  });
});

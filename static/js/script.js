const departmentSelect = document.getElementById("select-department");
const courseSelect = document.getElementById("course");

// Define courses for each department
const courses = {
  "Computer Science": [
    "B.Tech in CSE",
    "B.tech in AI / DS",
    "M.tech",
    "B.Sc Computer Science",
  ],
  Botany: ["B.Sc Botany", "M.Sc Botany"],
  English: ["B.A English", "M.A English", "PhD English"],
  MBA: ["MBA Finance", "MBA HR", "MBA Marketing"],
  Others: ["General Studies", "Diploma Programs"],
};

departmentSelect.addEventListener("change", function () {
  const dept = this.value;

  // Clear previous options
  courseSelect.innerHTML = "";

  if (dept === "") {
    courseSelect.disabled = true;
    courseSelect.innerHTML =
      "<option value=''>Select a department first</option>";
    return;
  }

  // Enable dropdown
  courseSelect.disabled = false;

  // Add courses
  courses[dept].forEach((course) => {
    const option = document.createElement("option");
    option.value = course;
    option.textContent = course;
    courseSelect.appendChild(option);
  });
});

form.addEventListener("submit", function (e) {
  if (courseSelect.disabled || courseSelect.value === "") {
    e.preventDefault();
    alert("Please select a course!");
  }
});

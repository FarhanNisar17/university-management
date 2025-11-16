
// Delete confirmation
function confirmDelete(url) {
  Swal.fire({
    title: "Delete this student?",
    text: "This action cannot be undone.",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "Yes, delete",
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = url;
    }
  });
}

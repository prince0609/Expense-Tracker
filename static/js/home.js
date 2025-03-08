function editEntry(id) {
  document.getElementById("editAmount").value = document.getElementById(
    "amount-" + id
  ).innerText;
  document.getElementById("editDescription").value = document.getElementById(
    "description-" + id
  ).innerText;
  document.getElementById("editId").value = id;
}


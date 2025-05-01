// Scroll ke atas jika perlu atau interaksi kecil
window.addEventListener('scroll', () => {
    // contoh interaksi bisa ditambahkan di sini
  });
  // Modal handler
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('hide');
  }
  
  function openModal() {
    document.getElementById("uploadModal").style.display = "block";
  }
  
  function closeModal() {
    document.getElementById("uploadModal").style.display = "none";
  }
  
  document.addEventListener("DOMContentLoaded", function() {
    const resepBtn = document.querySelector(".btn.blue");
    resepBtn.addEventListener("click", openModal);
  
    const uploadForm = document.getElementById("uploadForm");
    uploadForm.addEventListener("submit", function(e) {
      e.preventDefault();
      const fileInput = document.getElementById("fileUpload");
      if (fileInput.files.length > 0) {
        alert("Resep berhasil diupload!");
        closeModal();
        fileInput.value = ""; // reset input
      } else {
        alert("Silakan pilih file terlebih dahulu.");
      }
    });
  });
  
// Mouse Light Effect
document.addEventListener("mousemove", function(e) {
    const light = document.querySelector(".cursor-light");
    light.style.left = e.clientX + "px";
    light.style.top = e.clientY + "px";
});

// Dark/Light Toggle
function toggleMode() {
    document.body.classList.toggle("light");
}

// Drag & Drop
const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    fileInput.files = e.dataTransfer.files;
    showPreview(fileInput.files[0]);
});

fileInput.addEventListener("change", function() {
    showPreview(this.files[0]);
});

function showPreview(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        preview.src = e.target.result;
        preview.style.display = "block";
    };
    reader.readAsDataURL(file);
}

// Loading Animation
document.getElementById("uploadForm").addEventListener("submit", function() {
    document.getElementById("loader").style.display = "block";
});

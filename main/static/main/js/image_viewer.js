const imageViewer = document.getElementById("imageViewer");
const imageToView = document.getElementById("imageToView");

function viewImage(img) {
    imageToView.src = img.src;
    imageViewer.classList.remove('hidden');
}

function hideImage() {
    imageViewer.classList.add('hidden');
}


imageViewer.addEventListener("click", hideImage);
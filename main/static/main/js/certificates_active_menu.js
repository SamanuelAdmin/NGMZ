var certificatesBox = document.getElementById('certificatesBox')
var isCertMenuOpen = false;

function openCloseCertMenu() {
    isCertMenuOpen = !isCertMenuOpen;
    let certificates = document.getElementsByClassName('certificate');

    if (isCertMenuOpen) {
        certificatesBox.style.display = 'flex';
    }

    setTimeout(() => {
        for (var i = 0; i < certificates.length; i++) {
            if (isCertMenuOpen) {
                certificates[i].classList.remove('fade-out');
            } else {
                certificates[i].classList.add('fade-out');
            }
        }

        if (!isCertMenuOpen) {
            setTimeout(
                () => certificatesBox.style.display = 'none', 400
            );
        }
    }, 50);
}
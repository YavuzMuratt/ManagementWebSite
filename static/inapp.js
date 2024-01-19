// inapp.js



// Sayfa yüklendiğinde çalışacak olan kısım
document.addEventListener("DOMContentLoaded", function () {
    // Butona tıklandığında çalışacak olan kısım
    document.getElementById("animateButton").addEventListener("click", function () {
        animateButton();
    });
});

// Buton animasyonunu gerçekleştiren fonksiyon
function animateButton() {
    var button = document.getElementById("animateButton");

    // Rastgele renk oluştur
    var randomColor = getRandomColor();

    // Renk değişim animasyonu
    button.style.transition = "background-color 0.3s";
    button.style.backgroundColor = randomColor;

    // Animasyon sonrasında rengi eski haline getir
    setTimeout(function () {
        button.style.backgroundColor = "";
        button.style.transition = "";
    }, 300);
}

// Rastgele renk oluşturan fonksiyon
function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// inapp.js

document.addEventListener("DOMContentLoaded", function () {
    var buttonContainers = document.querySelectorAll(".button-link-container");

    buttonContainers.forEach(function (container) {
        var button = container.querySelector(".button-link");
        button.addEventListener("click", function () {
            animateButton(container);
        });
    });

    function animateButton(container) {
        // Container'a tıklandığında animasyonu başlat
        container.style.transition = "background-color 0.3s";
        container.style.backgroundColor = "#8B0000"; // Koyu kırmızı renk

        // Belirli bir süre sonra renkleri eski haline getir
        setTimeout(function () {
            container.style.backgroundColor = "";
        }, 500);
    }
});


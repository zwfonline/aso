// title sliding pictures
document.addEventListener('DOMContentLoaded', function () {
    const imageSlider = document.querySelector('.image-slider');
    const images = [
        'pictures/titlePic1.png',
        'pictures/titlePic2.png',
        'pictures/titlePic3.png',
        'pictures/titlePic4.png',
    ];
    let currentIndex = 0;

    function changeImage() {
        currentIndex = (currentIndex + 1) % images.length;
        const currentImage = images[currentIndex];
        imageSlider.querySelector('.titlePicture').src = currentImage;
    }

    const initialImage = images[currentIndex];
    imageSlider.querySelector('.titlePicture').src = initialImage;

    setInterval(changeImage, 5000);

    // Add event listeners to each h3 element
    const homeEvents = document.querySelectorAll('.homeEvents');
    homeEvents.forEach(function (event) {
        event.addEventListener('click', function () {
            const eventType = event.getAttribute('data-event-type');
            openImage(eventType);
        });
    });
});


//home nav page 
function redirectToPage(page) {
    if (page === 'page1') {
        window.location.href = "aboutus.html"; 
    } else if (page === 'page2') {
        window.location.href = "home.html"; 
    }else if (page === 'whatsaso') {
        window.location.href = "whatsaso.html"; 
    }else if (page === 'page3') {
        window.location.href = "coming-events.html"; 
    }else if (page === 'page4') {
        window.location.href = "membership.html"; 
    }
}

function showResources() {
    var menu = document.getElementById("resourcesMenu");
    menu.style.display = "block";
}

function openPage(pageUrl) {
    window.location.href = pageUrl;
}

function openjoin(){
    window.open("https://usasa.sa.edu.au/clubs/join/aviation/")
}

function resource1(){
    window.open("http://www.bom.gov.au/aviation/weather-packages/")
}

function resource2(){
    window.open("https://www.airservicesaustralia.com/")
}

function resource3(){
    window.open("https://vatsim.net/")
}

function resource4(){
    window.open("https://www.flightradar24.com/60,15/6")
}

function resource5(){
    window.open("https://www.liveatc.net/")
}

function openupcomingEvent(){
    window.open("https://usasa.sa.edu.au/events/6091/484/")
}

function contactus1(){
    window.open("https://www.facebook.com/unisaASO/")
}

function contactus2(){
    window.open("https://www.instagram.com/aso_unisa/")
}

function contactus3(){
    window.open("https://www.linkedin.com/company/usasa/?originalSubdomain=au")
}

function contactus4(){
    window.open("https://discord.com/invite/UZqGW4WuME")
}

function contactus5(){
    window.open("https://www.youtube.com/channel/UCEiCIYpCllkD7rDrmBTOArA")
}

function contactus6(){
    window.open("https://www.twitch.tv/USASAadelaide")
}

function openModal() {
    // Show the modal
    document.getElementById('myModal').style.display = 'block';
}

function closeModal() {
    // Hide the modal
    document.getElementById('myModal').style.display = 'none';
}

function showEvent1() {
    var workModal = document.getElementById('Event1');
    workModal.style.display = 'block';
}

function closeEvent1() {
    var workModal = document.getElementById('Event1');
    workModal.style.display = 'none';
}

function showEvent2() {
    var workModal = document.getElementById('Event2');
    workModal.style.display = 'block';
}

function closeEvent2() {
    var workModal = document.getElementById('Event2');
    workModal.style.display = 'none';
}

function showEvent3() {
    var workModal = document.getElementById('Event3');
    workModal.style.display = 'block';
}

function closeEvent3() {
    var workModal = document.getElementById('Event3');
    workModal.style.display = 'none';
}

function showEvent4() {
    var workModal = document.getElementById('Event4');
    workModal.style.display = 'block';
}

function closeEvent4() {
    var workModal = document.getElementById('Event4');
    workModal.style.display = 'none';
}

function showEvent5() {
    var workModal = document.getElementById('Event5');
    workModal.style.display = 'block';
}

function closeEvent5() {
    var workModal = document.getElementById('Event5');
    workModal.style.display = 'none';
}

function showEvent6() {
    var workModal = document.getElementById('Event6');
    workModal.style.display = 'block';
}

function closeEvent6() {
    var workModal = document.getElementById('Event6');
    workModal.style.display = 'none';
}






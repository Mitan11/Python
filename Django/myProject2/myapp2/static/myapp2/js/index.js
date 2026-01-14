// Side Nav Close on click 

function closeSideNav() {
    const navLinks = document.querySelectorAll("#navbarSupportedContent .nav-link");
    navLinks.forEach((link) => {
        link.addEventListener("click", () => {
            // Hide the offcanvas menu
            const offcanvas = document.getElementById("navbarSupportedContent");
            const offcanvasInstance = bootstrap.Offcanvas.getInstance(offcanvas);
            offcanvasInstance.hide();
        });
    });
}

closeSideNav();

// Counters
function counter() {
    $(document).ready(function () {
        $('.counter-value').each(function () {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 3500,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
    });
}

counter();

function reviewCard() {
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 4,
        spaceBetween: 30,
        loop: true,
        centeredSlides: true,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            300: {
                slidesPerView: 1,
                spaceBetween: 20,
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 40,
            },
            1024: {
                slidesPerView: 3,
                spaceBetween: 50,
            },
        },
    });
}

reviewCard();

// scroll reveal

function animation(){
    const sr = ScrollReveal({
        origin: 'top',
        distance: '60px',
        duration: 1000,
        delay: 400,
        reset: true,
    })
    
    sr.reveal(`.heading-1,.bg-img p,.bg-img .gap-1,.services .card,.Partnerships h2 `,{origin: 'top'})
    sr.reveal(`.heading-3 ,.c_fact,.about-right p ,.w-flow .card:nth-child(odd),iframe,.two,.three`,{origin: 'right'})
    sr.reveal(`.swiper-slide `,{origin: 'bottom'})
    sr.reveal(`.heading-2,.connections .list-item,.team-img .heading-3,.team-img .t-des,.w-flow .card:nth-child(even),.p-grid .card ,.d-grid, .needs-validation,.one`,{origin: 'left'})
    sr.reveal(`.team-img img,.i-grid img ,.form-container`,{interval: 100,scale: 0.9,distance: "0",opacity: 0})    
}

animation();
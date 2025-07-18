$(".category-slider").slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: false,
    rtl: true,
    responsive: [{
            breakpoint: 1200,
            settings: {
                slidesToShow: 4
            }
        },
        {
            breakpoint: 768,
            settings: {

                slidesToShow: 3
            }
        },
        {
            breakpoint: 546,
            settings: {

                slidesToShow: 2
            }
        }

    ]

});


// alert-message

setTimeout(function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(flash) {
        const bsAlert = bootstrap.Alert.getOrCreateInstance(flash);
        bsAlert.close();
    });
}, 2000);
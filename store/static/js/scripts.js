$(".category-slider").slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: false,
    loop: true,
    rtl: true,
    responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 6
            }
        },
        {
            breakpoint: 768,
            settings: {

                slidesToShow: 4
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
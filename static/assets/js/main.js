AOS.init({
  duration: 1200,
})

  // Toggle .header-scrolled class to #header when page is scrolled
  $(window).scroll(function() {
    if ($(this).scrollTop() > 40) {
      $('#navbar-main').addClass('header-scrolled');
    } else {
      $('#navbar-main').removeClass('header-scrolled');
    }
  });

  if ($(window).scrollTop() > 40) {
    $('#navbar-main').addClass('header-scrolled');
  }

  // Slider articles
$(document).ready(function(){
  $('#slider-articles').owlCarousel({
        loop:false,
        margin:10,
        nav:true,
        dots: false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:3
            }
        }
    });
});

    // Slider branches
$(document).ready(function(){
  $('#slider-branches').owlCarousel({
        loop:true,
        autoplay: true,
        autoplayHoverPause: true,
        autoplaySpeed: 2000,
        margin:10,
        nav:true,
        dots: false,
        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:4
            }
        }
    });
});

    // Slider important link
$(document).ready(function(){
  $('#slider-important-link').owlCarousel({
        loop:true,
        autoplay: true,
        autoplayHoverPause: true,
        autoplaySpeed: 3000,
        margin:10,
        nav:true,
        dots: false,
        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });
});

    // Slider management
$(document).ready(function(){
  $('#slider-management').owlCarousel({
        loop:true,
        autoplay: true,
        autoplayHoverPause: true,
        autoplaySpeed: 3000,
        margin:10,
        nav:true,
        dots: false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });
});

    // Slider reviews
$(document).ready(function(){
  $('#slider-reviews').owlCarousel({
        loop:true,
        autoplay: true,
        autoplayHoverPause: true,
        autoplaySpeed: 3000,
        margin:10,
        nav:true,
        dots: false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:2
            }
        }
    });
});

    // Slider mm
$(document).ready(function(){
  $('#slider-mm').owlCarousel({
        stagePadding: 200,
        loop:true,
        autoplay: true,
        autoplayHoverPause: true,
        autoplaySpeed: 1000,
        margin:10,
        nav:true,
        navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        dots: false,
        responsive:{
            0:{
                items:2,
                stagePadding: 30,
                nav:false
            },
            600:{
                items:2,
                stagePadding: 30
            },
            1000:{
                items:2,
                stagePadding: 80
            }
        }
    });
});
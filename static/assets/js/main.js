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
    const slider = $("#slider-articles").owlCarousel({
        loop:true,
        margin:10,
        nav:true,
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
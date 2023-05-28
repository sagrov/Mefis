$(function() {
  // Owl Carousel
  var owl = $(".owl-one");
  owl.owlCarousel({
    items: 1,
    margin: 10,
    loop: true,
    nav: true
  });
});

$(function() {
  var owl = $(".owl-two");
  owl.owlCarousel({
    stagePadding: 200,
    items: 1,
    margin: 10,
    loop: true,
    lazyLoad: true,
    nav: true,
    responsive:{
        0:{
            items: 1,
            stagePadding: 60
        },
        600:{
            items:1,
            stagePadding: 100
        },
        1000:{
            items:1,
            stagePadding: 200
        },
        1200:{
            items:1,
            stagePadding: 250
        },
        1400:{
            items:1,
            stagePadding: 300
        },
        1600:{
            items:1,
            stagePadding: 350
        },
        1800:{
            items:1,
            stagePadding: 400
        }
    }
  });
});


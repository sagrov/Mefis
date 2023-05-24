$(function() {
  // Owl Carousel
  var owl = $(".owl-carousel");
  owl.owlCarousel({

    items: checking(),
    margin: 10,
    loop: true,
    nav: true
  });
});
window.dispatchEvent(new Event('resize'));
function checking() {
  if (self.innerWidth <= 450) {
    return items = 1;
  }
  else {
    return items = 3;
  }
}

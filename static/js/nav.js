$('.nav.navbar-nav > li').on('click', function(e) {
  e.preventDefault();
  $('.nav.navbar-nav > li').removeClass('active');
  $(this).addClass('active');
});

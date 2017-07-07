$(document).ready(function() {
  var url = window.location;
  $('.nav.navbar-nav > li a[href="' + url + '"]').parent().addClass('active');
  $('.nav.navbar-nav > li a').filter(function() {
    return this.href == url;
  }).parent().addClass('active');
});

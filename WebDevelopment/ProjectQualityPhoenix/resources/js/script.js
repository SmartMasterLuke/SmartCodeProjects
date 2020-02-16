$(document).ready( function() {

	/* Scroll on buttons */

	$('.js-scroll-on-section-products').click(function(){
		$('html, body').animate({scrollTop: $('.js-section-products').offset().top -100}, 1000)
	});

	$('.js-scroll-on-section-quality').click(function(){
		$('html, body').animate({scrollTop: $('.js-section-quality').offset().top -100}, 1000)
	});

	$('.js-scroll-on-section-features').click(function(){
		$('html, body').animate({scrollTop: $('.js-section-features').offset().top -100}, 1000)
	});

	$('.js-scroll-on-section-cities').click(function(){
		$('html, body').animate({scrollTop: $('.js-section-cities').offset().top -100}, 1000)
	});

	$('.js-scroll-on-section-plans').click(function(){
		$('html, body').animate({scrollTop: $('.js-section-plans').offset().top -100}, 1000)
	});

	/* Navigation scroll */

	$(function() {
	  $('a[href*=#]:not([href=#])').click(function() {
	    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
	      var target = $(this.hash);
	      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
	      if (target.length) {
	        $('html,body').animate({
	          scrollTop: target.offset().top
	        }, 1000);
	        return false;
	      }
	    }
	  });
	});

	/* Animations on scroll */

	$('.arrow-down').addClass('animated fadeIn');

	$('.arrow-down i').addClass('animated bounce');

	$('.hero-text-box').addClass('animated fadeIn');

	/* Button to top */

	var back_to_top_button = ['<a href="#top" class="back-to-top" style="border-bottom: 0px solid #ff3f34;"><i class="fas fa-arrow-circle-up" style="color:#fff; font-size: 30px; margin-bottom: 1px;"></i></a>'].join("");
	$("body").append(back_to_top_button)

	$(".back-to-top").hide();

	$(function () {
		$(window).scroll(function () {
			if ($(this).scrollTop() > 100) { 
				$('.back-to-top').fadeIn();
			} else {
				$('.back-to-top').fadeOut();
			}
		});

		$('.back-to-top').click(function () { 
			$('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});
	});
});

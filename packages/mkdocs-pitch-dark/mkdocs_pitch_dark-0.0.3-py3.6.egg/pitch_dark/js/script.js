var portfolio = window.portfolio || {

    'init': function() {

        // If mobile, hide tagCloud
        this.checkSize();
        this.tagCloud();
        //this.timeline();

        // jQuery for page scrolling feature
        $('body').on('click', '.page-scroll a', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });

        // Highlight the top nav as scrolling occurs
        $('body').scrollspy({
            target: '.navbar-fixed-top'
        });

        // Closes the Responsive Menu on Menu Item Click
        $('.navbar-collapse ul li a').click(function() {
            $('.navbar-toggle:visible').click();
        });

        //this.quote();
        this.helloWorld();
    },

    'quote': function() {
        // Generate Quotes for Landing page
        var quote = document.getElementById("my_quote");
        var number_of_quotes = quotes.length;
        var random_quote = Math.floor((Math.random() * number_of_quotes));
        quote.innerHTML = (quotes[random_quote]);
    },

    'timeline': function() {
        var ready = false;
        if (typeof(TL) !== 'undefined') {
            // Timeline Options
            var additionalOptions = {
                default_bg_color: {
                    r: 6,
                    g: 6,
                    b: 6
                }
            }
            var _timeline = new TL.Timeline('timeline-embed', 'https://docs.google.com/spreadsheets/d/1RnPcX-ORp5U1YX3U3kmb3DNGegL5Qkls17UW8d9uvZE/pubhtml', additionalOptions);
            ready = true;
        } else if (!ready) {
            setTimeout(function() {
                timeline();
            }, 1000);
        }
    },

    'tagCloud': function() {
        // Initializes Tag Canvas
        if (!$('#tagcloud').tagcanvas({
                textColour: '#FFFFFF',
                textHeight: 15,
                outlineMethod: 'none',
                initial: [0.04, -0.2],
                minSpeed: 0.01,
                maxSpeed: 0.05,
                depth: 0.75,
                textOpt: true,
                shuffleTags: true,
                wheelZoom: false
            })) {
            // TagCanvas failed to load
            $('#tags').hide();
        }
    },

    // TODO. Decouple size check from tag canvas for reusability
    'checkSize': function() {
        if ($(".visible-sm").css("display") == "none") {
            this.tagCloud();
        } else {
            if ($("#search").css("display") == "none") {
                $('#tags').css("display", "none");
            } else {
                this.tagCloud();
            }
        }
    },

    'helloWorld': function() {
        // Type Hello World
        var heading = $('.typed').html();
        var user = this.getCookie('user-agent');

        if (user != "") {
			$(".typed").html(
				heading + "<span class=\"typed-cursor\">|</span>"
			);
            //console.log(user);
        } else {
            $(".typed").typed({
                strings: [heading],
                typeSpeed: 100
            });
            user = Math.floor(Math.random() * 10000);
            if (user != "" && user != null) {
                this.setCookie("user-agent", user, 1);
            }
        }
    },

    'setCookie': function(cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    },

    'getCookie': function(cname) {
        // Get HTTP Cookie
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    },
}

$(document).ready(function() {
    portfolio.init();
});

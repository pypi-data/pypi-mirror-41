require([
  'jquery',
  'pat-base',
  'mockup-utils',
  'collective.tiles.sliders.responsiveslides.vendor'
], function($, Base, utils) {
  'use strict';

  var ResponsiveSlides = Base.extend({
    name: 'responsiveslides',
    trigger: '.pat-responsiveslides',
    parser: 'mockup',
    defaults: {
      auto: true,             // Boolean: Animate automatically, true or false
      speed: 500,             // Integer: Speed of the transition, in milliseconds
      timeout: 4000,          // Integer: Time between slide transitions, in milliseconds
      pager: false,           // Boolean: Show pager, true or false
      nav: false,             // Boolean: Show navigation, true or false
      random: false,          // Boolean: Randomize the order of the slides, true or false
      pause: false,           // Boolean: Pause on hover, true or false
      pauseControls: true,    // Boolean: Pause when hovering controls, true or false
      prevText: "Previous",   // String: Text for the "previous" button
      nextText: "Next",       // String: Text for the "next" button
      maxwidth: "",           // Integer: Max-width of the slideshow, in pixels
      navContainer: "",       // Selector: Where controls should be appended to, default is after the 'ul'
      manualControls: "",     // Selector: Declare custom pager navigation
      namespace: "rslides"    // String: Change the default namespace used
    },
    init: function() {
      var that = this;
      that.$el.responsiveSlides({
        auto: utils.bool(that.options.auto),
        speed: that.options.speed,
        timeout: that.options.timeout,
        pager: utils.bool(that.options.pager),
        nav: utils.bool(that.options.nav),
        random: utils.bool(that.options.random),
        pause: utils.bool(that.options.pause),
        pauseControls: utils.bool(that.options.pauseControls),
        prevText: that.options.prevText,
        nextText: that.options.nextText,
        maxwidth: that.options.maxwidth,
        navContainer: that.options.navContainer,
        manualControls: that.options.manualControls,
        namespace: that.options.namespace
      });
    }

  });
  return ResponsiveSlides;

});

define("/Users/iham/sandbox/plone/collective.tiles.sliders/src/collective/tiles/sliders/tiles/responsiveslides/assets/pattern.js", function(){});


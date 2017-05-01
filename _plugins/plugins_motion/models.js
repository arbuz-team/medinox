/**
 * Created by mrskull on 06.01.17.
 */

import {data_controller} from '../arbuz/js/structure'


export let Plugins_Motion_Models = function(config)
{
  let that = this;

  this.settings = {
    container: undefined,
    content: undefined,
    hide: '.hide',

    width: undefined,
    height: undefined,

    can_open_by: undefined,
    can_open_from: undefined,
    can_open_to: undefined,

    direction_open: undefined,
    direction_close: undefined,

    duration_open: undefined,
    duration_close: undefined,
  };

  let load_settings = function()
  {
    if(typeof config !== 'undefined')
    {
    // -- Container
      if(typeof config.container !== 'undefined')
        that.settings.container = config.container;


    // -- Children container
      if(typeof config.content !== 'undefined')
        that.settings.content = config.container +' '+ config.content;


    // -- Witdh & height
      let
        $container = $(that.settings.container);
      that.settings.width = $container.outerWidth();
      that.settings.height = $container.outerHeight();


    // -- Can open
      if(typeof config.can_open_by !== 'undefined')
        that.settings.can_open_by = config.can_open_by;

      if(typeof config.can_open_from !== 'undefined')
        that.settings.can_open_from = config.can_open_from;

      if(typeof config.can_open_to !== 'undefined')
        that.settings.can_open_to = config.can_open_to;


    // -- Duration open & close
      if(typeof config.duration_open !== 'undefined')
        that.settings.duration_open = config.duration_open;

      if(typeof config.duration_close !== 'undefined')
        that.settings.duration_close = config.duration_close;


    // -- Swipe & direction
      if(typeof config.open !== 'undefined')
      {
        switch(config.open)
        {
          case 'right':
            that.settings.swipe_open = 'swiperight';
            that.settings.swipe_close = 'swipeleft';
            that.settings.direction_open = 'right';
            that.settings.direction_close = 'left';
            break;

          case 'left':
            that.settings.swipe_open = 'swipeleft';
            that.settings.swipe_close = 'swiperight';
            that.settings.direction_open = 'left';
            that.settings.direction_close = 'right';
            break;

          case 'up':
            that.settings.swipe_open = 'swipeup';
            that.settings.swipe_close = 'swipedown';
            that.settings.direction_open = 'top';
            that.settings.direction_close = 'bottom';
            break;

          case 'down':
            that.settings.swipe_open = 'swipedown';
            that.settings.swipe_close = 'swipeup';
            that.settings.direction_open = 'bottom';
            that.settings.direction_close = 'top';
            break;
        }
      }
    }
  };

  load_settings();

/////////////////////////

  this.state = {
    is_open: false,
    is_not_set: true,
  };

/////////////////////////

  let

    check_by_sizes = function()
    {
      let
        width_window = $(window).outerWidth(),
        height_window = $(window).outerHeight(),

        posibility = {
          from: that.settings.can_open_from,
          to: that.settings.can_open_to,
        };


      if(that.settings.can_open_by === 'width')
      {
        if(typeof posibility.from !== 'undefined')
          return width_window >= posibility.from;

        else if(typeof posibility.to !== 'undefined')
          return width_window <= posibility.to;
      }

      else if(that.settings.can_open_by === 'height')
      {
        if(typeof posibility.from !== 'undefined')
          return height_window >= posibility.from;

        else if(typeof posibility.to !== 'undefined')
          return height_window <= posibility.to;
      }

      return false;
    },


    check_mobile_by_sizes = function()
    {
      let
        width_window = parseInt($(window).outerWidth()),
        max_mobile_width = 1000;

        return width_window < max_mobile_width;
    };


  this.check_is_open = function()
  {
    return this.state.is_open;
  };


  this.check_is_close = function()
  {
    return !this.state.is_open;
  };


  // this.check_possibility_of_swipe = function()
  // {
  //   return check_mobile_by_sizes();
  // };


  this.check_possibility_of_opening = function()
  {
    if(check_by_sizes())
      if(data_controller.get('can_do_open_plugin'))
        return this.check_is_close();
      else if(this.settings.container === '#CART')
        return this.check_is_close();

    return false;
  };


  this.change_possibility_of_opening = function(bool)
  {
    this.state.is_open = !bool;

    if(this.settings.container !== '#CART')
      data_controller.change('can_do_open_plugin', bool);
  };
};


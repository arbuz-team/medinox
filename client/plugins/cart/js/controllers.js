/**
 * Created by mrskull on 07.01.17.
 */

import {Plugins_Loader_Controllers}     from '../../plugins_loader/controllers'
import {Plugins_Motion_Controllers}     from '../../plugins_motion/controllers'
import {Form_Controllers}               from '../../forms/js/controllers'
import {Post_Button_Controllers}        from '../../forms/js/post_button/controllers'
import {Event_Button_Controllers}       from '../../forms/js/event_button/controllers'


/**
 *    Defining private variables
 */

let

  cart_loader_controllers = new Plugins_Loader_Controllers({
    name: 'cart',
    url: '/cart/',

    container: '#CART .cart',

    auto_first_loading: true,
    load_with_page: false,
  }),

  cart_motion_controllers = new Plugins_Motion_Controllers({
    container: '#CART',
    content: '.cart',
    open: 'left',
    can_open_by: 'width',
    can_open_from: 0,
    duration_open: 200,
    duration_close: 200,
  }),

  post_button_controllers = new Post_Button_Controllers({
    container: '#CART > .cart',
    callback: cart_loader_controllers.reload, ///////////////////////////////////////////////// popraw
  }),

  event_button_controllers = new Event_Button_Controllers({
    container: '#CART'
  }),

  cart_form_controllers = new Form_Controllers(cart_loader_controllers),


  manage_key = function(event)
  {
    if(event.keyCode === 27)
      cart_motion_controllers.plugin_close();

    if(event.ctrlKey && event.shiftKey && event.keyCode === 88)
    {
      event.preventDefault();
      if(cart_motion_controllers.is_open())
        cart_motion_controllers.plugin_close();
      else
        cart_motion_controllers.plugin_open();
    }
  };


/**
 *    Defining public functions
 */

export let

  define = function()
  {
    window.APP.add_own_event('cart_open', cart_motion_controllers.plugin_open);
    window.APP.add_own_event('cart_close', cart_motion_controllers.plugin_close);
    window.APP.add_own_event('cart_open_or_close', open_or_close);

    $('body').keydown(manage_key);

    cart_form_controllers.define();
    cart_motion_controllers.define();
    post_button_controllers.define();
    event_button_controllers.define();
  },


  start = function()
  {
    cart_loader_controllers.define();
    cart_motion_controllers.start();
  },


  plugin_open = cart_motion_controllers.plugin_open,


  plugin_close = cart_motion_controllers.plugin_close,


  open_or_close = function()
  {
    window.APP.throw_event(window.EVENTS.plugins.close_navigation);

    if(cart_motion_controllers.is_open())
      plugin_close();
    else
      plugin_open();
  },


  reload = function()
  {
    cart_motion_controllers.plugin_open();
  };

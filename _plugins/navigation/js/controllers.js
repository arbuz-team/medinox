/**
 * Created by mrskull on 24.11.16.
 */

import {Plugins_Loader_Controllers}     from '../../plugins_loader/controllers'
import {Plugins_Motion_Controllers}     from '../../plugins_motion/controllers'
import {Event_Button_Controllers}       from '../../forms/js/event_button/controllers'


/**
 *    Defining private variables
 */

let
  navigation_loader_controllers,
  config_loader = {
    name: 'navigation',
    url: '/navigation/',

    container: '#NAVIGATION .navigation',

    auto_first_loading: true,
  },

  navigation_motion_controllers,
  config_motion = {
    container: '#NAVIGATION',
    content: '.navigation',
    open: 'down',

    can_open_by: 'width',
    can_open_to: 675,

    duration_open: 300,
    duration_close: 150,
  },

  event_button_controllers = new Event_Button_Controllers({
    container: '#NAVIGATION'
  });


/**
 *    Defining public functions
 */

export let
  define = function()
  {
    window.APP.add_own_event('navigation_close', navigation_motion_controllers.plugin_close);
    window.APP.add_own_event('navigation_open', navigation_motion_controllers.plugin_open);

    navigation_motion_controllers.define();
    event_button_controllers.define();
  },


  start = function()
  {
    // -- Loader configuration
    navigation_loader_controllers = new Plugins_Loader_Controllers(config_loader);
    navigation_loader_controllers.define();


    // -- Motion configuration
    navigation_motion_controllers = new Plugins_Motion_Controllers(config_motion);
    navigation_motion_controllers.start();
  },


  plugin_open = function()
  {
    navigation_motion_controllers.plugin_open();
  };
 


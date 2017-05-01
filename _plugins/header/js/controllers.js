/**
 * Created by mrskull on 08.01.17.
 */

import {Plugins_Loader_Controllers}     from '../../plugins_loader/controllers'
import {Event_Button_Controllers}       from '../../forms/js/event_button/controllers'


/**
 *    Defining private variables
 */

let
  header_loader_events,
  config_loader = {
    name: 'navigation',
    url: '/navigation/',

    container: '#HEADER > .header',

    auto_first_loading: true,
  },

  event_button_controllers = new Event_Button_Controllers({
    container: '#HEADER'
  });


/**
 *    Defining public functions
 */

export let

  define = function()
  {
    event_button_controllers.define();
  },


  start = function()
  {
    header_loader_events = new Plugins_Loader_Controllers(config_loader);
    header_loader_events.define();
  };
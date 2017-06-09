/**
 * Created by mrskull on 07.01.17.
 */

import {Plugins_Loader_Controllers} from '../../plugins_loader/controllers'
import {Plugins_Motion_Controllers} from '../../plugins_motion/controllers'
import {Form_Controllers}  from '../../forms/js/controllers'
import {Post_Button_Controllers}        from '../../forms/js/post_button/controllers'


/**
 *    Defining private variables
 */

let
  searcher_loader_controllers = new Plugins_Loader_Controllers({
    name: 'searcher',
    url: '/searcher/',

    container: '#SEARCHER .searcher',

    auto_first_loading: true,
  }),

  searcher_motion_controllers = new Plugins_Motion_Controllers({
    container: '#SEARCHER',
    content: '.searcher',
    open: 'right',
    can_open_by: 'width',
    can_open_to: 1000,
    duration_open: 200,
    duration_close: 200,
  }),

  post_button_controllers = new Post_Button_Controllers({
    container: '#SEARCHER'
  }),

  searcher_form_controllers = new Form_Controllers(searcher_loader_controllers);


/**
 *    Defining public functions
 */

export let

  define = function()
  {
    window.APP.add_own_event('searcher_open', searcher_motion_controllers.plugin_open);

    searcher_motion_controllers.define();
    searcher_form_controllers.define();
    post_button_controllers.define();
  },


  start = function()
  {
    searcher_loader_controllers.define();
    searcher_motion_controllers.start();
  };


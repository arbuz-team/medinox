/**
 * Created by mrskull on 08.01.17.
 */

import {Plugins_Loader_Controllers}     from '../../plugins_loader/controllers'
import {Form_Controllers}               from '../../forms/js/controllers'
import {Post_Button_Controllers}        from '../../forms/js/post_button/controllers'
import {Event_Button_Controllers}        from '../../forms/js/event_button/controllers'


/**
 *    Defining private variables
 */

let

  config_loader = {
    name: 'ground',

    container: '#GROUND > .ground',
    first_element: '.block_1',

    auto_first_loading: true,
    load_with_page: true,
  },
  ground_loader_controllers = new Plugins_Loader_Controllers(config_loader),

  post_button_controllers = new Post_Button_Controllers({
    container: '#GROUND .ground'
  }),

  event_button_controllers = new Event_Button_Controllers({
    container: '#GROUND .ground'
  }),

  ground_form_controllers = new Form_Controllers(ground_loader_controllers);


/**
 *    Defining private functions
 */

let

  change_url = function(url)
  {
    history.pushState('', url, url);
  },


  go_to_link = function(event)
  {
    let
      url = $(this).attr('href'),
      protocol = url.substring(0, 4);

    if(protocol !== 'http')
      if(event.which === 1)
      {
        event.preventDefault();
        window.APP.throw_event(window.EVENTS.plugins.close);

        change_url(url);

        ground_loader_controllers.load(url);
      }
  },

  redirect = function(event)
  {
    change_url(window.APP.DATA.redirect);
    ground_loader_controllers.redirect(event);
  },


  back_url = function()
  {
    event.preventDefault();
    ground_loader_controllers.load();
  },


  change_height_content = function()
  {
    let
      $container = $(config_loader.container),
      height = {
        window: $('#CONTAINTER').innerHeight(),
        header: $('#HEADER').outerHeight(),
        ground_top: $container.position().top,
      },
      height_container = height.window - height.header - height.ground_top;

    $container.height(height_container);
    change_height_start_banner($container, height_container)
  },


  change_height_start_banner = function($container, height_container)
  {
    let
      width_website = $('#CONTAINTER').innerWidth(),
      height_start_banner = 0;

    if(height_container > 768)
      height_start_banner = height_container - 386;

    if(height_start_banner === 0 || width_website < 1000)
    {
      $('.ground-block.start .block-content-image', $container).hide();
      $('.ground-block.start .block-content-recommended-title', $container).show();
    }
    else
    {
      $('.ground-block.start .block-content-image', $container).show().height(height_start_banner);
      $('.ground-block.start .block-content-recommended-title', $container).hide();
    }
  };


/**
 *    Defining public functions
 */

export let

  define = function()
  {
    change_height_content();

    $('a').click(go_to_link);
    window.APP.add_own_event('redirect', redirect);
    window.APP.add_own_event('popstate', back_url);
    $(window).resize(change_height_content);

    ground_form_controllers.define();
    post_button_controllers.define();
    event_button_controllers.define();
  },


  start = function()
  {
    ground_loader_controllers.define();
  },


  change_content = function(url, post_data)
  {
    ground_loader_controllers.load(url, post_data);
  };
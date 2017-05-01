/**
 * Created by mrskull on 17.12.16.
 */

import {Post_Button_Views} from './views'


export let Post_Button_Controllers = function(config)
{
  if(typeof config === 'undefined' && typeof config.container === 'undefined')
  {
    console.error('Exeption error: invalid container.');
    return {};
  }


  let
    buttons_views = {},


    manage_buttons = function(event)
    {
      event.preventDefault();
      event.stopPropagation();

      let
        button_name = $(this).data('name');

      if(buttons_views[button_name])
        buttons_views[button_name].start();
      else
        console.error('Button "'+ button_name +'" doesn\'t exsist');
    },


    create_button_views = function()
    {
      let
        button_name = $(this).data('name');
      config.button = this;

      config.button_name = button_name;
      config.button_action = $(this).data('action');
      config.button_value = $(this).data('value');
      config.button_reload = $(this).data('reload');
      config.button_redirect = $(this).data('redirect');
      config.button_event = $(this).data('event');
      config.button_url = $(this).data('url');

      if($(this).find('span, i').length)
        config.button_html = $(this).find('span').html();
      else
        config.button_html = $(this).html();

      buttons_views[button_name] = new Post_Button_Views(config);
    };


  this.define = function()
  {
    let $post_buttons = $('.post_button', config.container);

    $post_buttons
      .each(create_button_views);

    $post_buttons
      .click(manage_buttons);
  };
};
/**
 * Created by mrskull on 17.12.16.
 */

import {Event_Button_Views} from './views'


export let Event_Button_Controllers = function(config)
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
      let
        button_name = $(this).data('name'),
        button_prevent = $(this).data('prevent');

      if(button_prevent !== 'false')
        event.preventDefault();

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
      config.button_reload = $(this).data('reload');
      config.button_redirect = $(this).data('redirect');
      config.button_event = $(this).data('event');
      config.button_delay = $(this).data('delay');

      buttons_views[button_name] = new Event_Button_Views(config);
    };


  this.define = function()
  {
    let $buttons = $('.event_button', config.container);

    $buttons
      .each(create_button_views);

    $buttons
      .click(manage_buttons);
  };
};
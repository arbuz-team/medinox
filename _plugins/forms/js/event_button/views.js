/**
 * Created by mrskull on 18.12.16.
 */

import {Event_Button_Models} from './models'


export let Event_Button_Views = function(config)
{

  let
    models = new Event_Button_Models(config);

  this.models = models;


  let

    reload_plugins = function()
    {
      let
        plugins = models.settings.button_reload,
        plugins_array, array_length;

      if(!plugins || typeof plugins !== 'string')
        return false;

      plugins_array = plugins.split(' ');
      array_length = plugins_array.length;

      for(let i = 0; i < array_length; ++i)
        if(plugins_array[i])
        {
          window.APP.DATA.delay = 0;
          window.APP.throw_event(window.EVENTS.plugins['reload_'+ plugins_array[i]]);
        }
    },


    redirect_ground = function()
    {
      let
        url = models.settings.button_redirect;

      if(!url || typeof url !== 'string')
        return false;

      window.APP.DATA.redirect = url;
      window.APP.DATA.delay = 100;
      window.APP.throw_event(window.EVENTS.redirect);
    },


    launch_event = function()
    {
      let
        event = models.settings.button_event,
        split_event,
        ready_event = window.EVENTS;

      if(!event || typeof event !== 'string')
        return false;

      split_event = event.split('.');

      for(let i = 0; split_event.length > i; ++i)
        ready_event = ready_event[split_event[i]];

      if(ready_event.constructor === Event)
      {
        if(models.settings.button_delay >= 0)
          window.APP.DATA.delay = models.settings.button_delay;

        window.APP.throw_event(ready_event); // example plugins.close_cart
      }
      else
        console.error('Event error: This event doesn\' exist');
    };


  this.start = function()
  {
    reload_plugins();
    redirect_ground();
    launch_event();
  };

};
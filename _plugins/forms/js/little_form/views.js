/**
 * Created by mrskull on 18.12.16.
 */

import {Little_Form_Models} from './models'


export let Little_Form_Views = function(form_config)
{
  let
    models = new Little_Form_Models(form_config);

  this.models = models;


  let

    reload_plugins = function()
    {
      let
        plugins = models.settings.reload,
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
        url = models.settings.redirect;

      if(!url || typeof url !== 'string')
        return false;

      window.APP.DATA.redirect = url;
      window.APP.DATA.delay = 100;
      window.APP.throw_event(window.EVENTS.redirect);
    },


    launch_event = function()
    {
      let
        event = models.settings.event,
        split_event,
        ready_event = window.EVENTS;

      if(!event || typeof event !== 'string')
        return false;

      split_event = event.split('.');

      for(let i = 0; split_event.length > i; ++i)
        ready_event = ready_event[split_event[i]];

      if(ready_event.constructor === Event)
      {
        window.APP.DATA.delay = 100;
        window.APP.throw_event(ready_event); // example plugins.close_cart
      }
    },


    end_loading = function(JSON_response, status)
    {
      models.set_state_loading(false);

      if(models.is_error(JSON_response, status))
      {
        models.set_state_error(true);
        console.error('Little form error: response is wrong.');
        return false;
      }

      reload_plugins();
      redirect_ground();
      launch_event();
    };


  this.start = function(value)
  {
    if(models.get_state_loading())
      return false;

    models.set_state_loading(true);

    models.settings.value = value;
    models.send_post(end_loading);
  };

};
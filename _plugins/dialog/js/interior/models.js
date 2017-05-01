/**
 * Created by mrskull on 21.01.17.
 */

import {Plugins_Loader_Controllers} from '../../../plugins_loader/controllers'


let

  dialog_loader_controllers = new Plugins_Loader_Controllers({
    name: 'dialog',

    container: '#DIALOG > .dialog',

    duration: {
      show: 0,
      hide: 0,
    },
  });


///////////////////////////////////////

export let

  selectors = {
    container: '#DIALOG',
    buttons: '#DIALOG .dialog-content-button',
  },

  variables = {},

  reset_variables = (function()
  {
    let define = function()
    {
      variables = {
        type: '',
        name: '',
        value: '',
        post_data: undefined,
      };
    };
    define();

    return define;
  })(),


  is_error = function(response, status)
  {
    if(status !== 'success')
      return true;

    if(response !== '{"__form__": "true"}')
      return true;

    return false;
  },


  prepare_post_data = function(post_data)
  {
    if(post_data) // if is form
      variables.post_data = post_data;

    else // if is normal dialog
    {
      if(!variables.post_data)
        variables.post_data = {};

      variables.post_data['dialog_type'] = variables.type;
      variables.post_data['dialog_name'] = variables.name;

      if(variables.value)
        variables.post_data['dialog_value'] = variables.value;
    }
  },


  load = function(url, post_data, callback)
  {
    prepare_post_data(post_data);

    dialog_loader_controllers.load(url, variables.post_data, callback);
  },


  reload = function(callback)
  {
    dialog_loader_controllers.load(undefined, variables.post_data, callback);
  };
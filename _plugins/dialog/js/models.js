/**
 * Created by mrskull on 29.12.16.
 */

import * as interior_dialog_controllers     from './interior/controllers'
import * as interior_dialog_models          from './interior/models'


export let

  selectors = interior_dialog_models.selectors,


  save_type_and_name = function(dialog_data)
  {
    let
      type = dialog_data.type,
      name = dialog_data.name,
      value = dialog_data.value;

    if(!type || !name)
    {
      console.error('Dialog error: Type or name is invalid.');
      return false;
    }

    interior_dialog_models.reset_variables();

    interior_dialog_models.variables.type = type;
    interior_dialog_models.variables.name = name;
    interior_dialog_models.variables.value = value;
  },


  prepare_post_data = function(additional_data)
  {
    let
      post_data = {},
      isset = 0;

    for(let data in additional_data)
    {
      if(additional_data.hasOwnProperty(data))
        if(additional_data[data])
          post_data[data] = additional_data[data];
        else
          post_data[data] = '';

      ++isset;
    }

    if(isset > 0)
      interior_dialog_models.variables.post_data = post_data;
    else
      interior_dialog_models.variables.post_data = undefined;
  },


  open = function(dialog_data, additional_data, callback)
  {
    if(save_type_and_name(dialog_data) === false)
      return false;

    if(prepare_post_data(additional_data) === false)
      return false;

    interior_dialog_controllers.load(undefined, undefined, callback);
  },


  reload = function(callback)
  {
      interior_dialog_controllers.reload(callback);
  };


selectors.window =              selectors.container +   ' > .dialog';
selectors.header =              selectors.window +      ' > .dialog-header';
selectors.content =             selectors.window +      ' > .dialog-content';
selectors.external_buttons =                            '.dialog_button';
/**
 * Created by mrskull on 21.01.17.
 */

import * as interior_dialog_models from './models'


let
  hide_if_error = function(response, status)
  {
    if(interior_dialog_models.is_error(response, status) === false)
      $(interior_dialog_models.selectors.container)
        .hide();
  };


export let

  models = interior_dialog_models,
  container = models.selectors.container,


  load = function(url, post_data, callback)
  {
    if(!callback)
      callback = hide_if_error;

    interior_dialog_models.load(url, post_data, callback);
  },


  reload = interior_dialog_models.reload;
/**
 * Created by mrskull on 29.12.16.
 */

import * as dialog_models from './models'


/**
 *    Defining public variables
 */

export let
  selectors = dialog_models.selectors;

/**
 *    Defining private functions
 */

let

  show = function()
  {
    $(selectors.container)
      .css('opacity', '')
      .fadeIn(200);
  },


  hide = function()
  {
    console.log('hide');
    $(selectors.container)
      .animate({opacity: 0}, 200, function()
      {
		  $(selectors.container).hide();
	  });
  },


  dim = function(callback)
  {
    console.log('dim');
    $(selectors.container)
      .animate({ opacity: .8 }, 200, callback);
  },


  lighten = function()
  {
    $(selectors.container)
      .animate({ opacity: 1 }, 300);
  };


/**
 *    Defining public functions
 */

export let

  open = function(dialog_data, additional_data)
  {
    dialog_models.open(dialog_data, additional_data, show);
  },


  reload = function()
  {
    dim(function(){
      dialog_models.reload(lighten);
    });
  },


  close = function()
  {
    hide();
  };
/**
 * Created by mrskull on 02.01.17.
 */

import * as models from './models'


/**
 *    Defining public functions
 */

export let define = function()
{
  $(models.selectors.language_fields).change(change_language);
};


/**
 *    Defining events functions
 */

let
  change_language = function()
  {
    window.location = $(this).val();
  };
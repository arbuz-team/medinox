/**
 * Created by mrskull on 21.01.17.
 */

import * as interior_dialog_views   from './views'
import {close as dialog_close}      from '../controllers'
import {Form_Controllers}           from '../../../../form/js/controllers'
import {Post_Button_Controllers}    from '../../../../form/plugin/post_button/controllers'
import {Event_Button_Controllers}    from '../../../../form/plugin/event_button/controllers'
import {Little_Form_Controllers}    from '../../../../form/plugin/little_form/controllers'


/////////////////////////////

export let

  load = interior_dialog_views.load,
  reload = interior_dialog_views.reload;


let

  selectors = interior_dialog_views.models.selectors,

  post_button_controllers = new Post_Button_Controllers({
    container: '#DIALOG > .dialog'
  }),

  event_button_controllers = new Event_Button_Controllers({
      container: '#DIALOG > .dialog'
  }),

  little_form_controllers = new Little_Form_Controllers({
    container: '#DIALOG > .dialog'
  }),

  dialog_form_controllers = new Form_Controllers(interior_dialog_views);


export let

  recognize_button = function()
  {
    let
      $button = $(this),
      name = $button.data('dialog-button');

    if( name === 'send')
      $('form.dialog_form', selectors.container).submit();

    else
      console.error('Dialog error: Don\'t recognize button "'+ name +'".');
  },


  define = function()
  {
    $(selectors.buttons).click(recognize_button);

    post_button_controllers.define();
    event_button_controllers.define();
    little_form_controllers.define();
    dialog_form_controllers.define();
  };
/**
 * Created by mrskull on 17.01.17.
 */

import * as form from './views'


/**
 *    Defining events
 */

export let define = function($container)
{
  let $otoczka_pola = $('.hide_form > .otoczka_pola', $container);

  $otoczka_pola.children('div')
    .click(edit_field);

  $otoczka_pola.children('button')
    .click(save_or_edit);

};


/**
 *    Defining private event functions
 */

let edit_field = function()
{
  let
    $div = $(this),
    $field = $div.parent().children('input'),
    $button = $div.parent().children('button');

  // Change words to input
  $div.fadeOut(100, function(){
    $field.fadeIn(100, function(){
      $(this).focus();
    });
    $button.html('Save');
  });
};


let save_or_edit = function()
{
  let
    $button = $(this),
    data_button = $button.data('type'),
    $div = $button.parent().children('div'),
    $field = $button.parent().children('input');


  let save_data = function(html, status)
  {
    if(status === 'success')
      // Change input to words
      $field.fadeOut(100, function(){
        $div.html($field.val());
        $div.fadeIn(100);
        $button.change_data('type', 'edit').html('Edit');
      });
    else
      $button.html('Save: error');
  };


  if(data_button === 'edit')
    // Change words to input
    $div.fadeOut(100, function(){
      $field.fadeIn(100, function(){
        $(this).focus();
      });
      $button.change_data('type', 'save').html('Save');
    });

  else if(data_button === 'save')
    form.send(this, save_data);
};

import {Constructor_Validator} from './checkers'

let Validators = {};

window.Validators = Validators;

export let define = function($container)
{

	$('form[data-test=yes]', $container).each(function(){
		let name = $(this).data('name'),
      type = $(this).data('type');
		if(name || type)
    {
      Validators[name] = new Constructor_Validator(name, type);

      // Sprawdzanie wszystkich pól by odblokować guzik w razie ich poprawnego wypełnienia
      let fields_of_form = Validators[name].hasErrors();
      for( let key in fields_of_form )
        if(fields_of_form.hasOwnProperty( key ))
        {
          let $field = $('form[data-name=' + name + '] *[name=' + key + ']');

          if($field.val())
            validate($field);
        }
    }
    else
      console.error( 'Validation Error: Incorrect or empty form name/type.' );
	});


  $('form[data-test=yes] .test')
    .keyup(catch_event_validate)
    .change(catch_event_validate);


  $('.show_password').change(function(){
    if($(this).is(':checked'))
      show_password(this);
    else
      hide_password(this);
  });

};



//////////////////////////////   VIEWS VALIDATOR   ///////////////////////////////////

let running_validator = false,
  form_name,
  $form,
  Validator,
  field,
  field_name,
  field_value;


let catch_event_validate = function()
{
  validate(this);
};


let validate = function(response_field)
{
  if(running_validator === false)
  {
    running_validator = true;

    field = response_field;

    form_name = $(field).parents('form').data('name');
    $form = $('form[data-name='+ form_name +']');
    Validator = Validators[form_name];
    field_name = $(field).attr('name');
    field_value = $(field).val();

    // Sprawdzanie pojedynczego pola poprzez checker przypisany do jego nazwy
    Validator.field(field_name, field_value, show_status);
  }
};


let show_status = function(result)
{
  if(result)
  {
    let $field = $(field),
      $status = $field.parent().find('.status');

    let bool = result.bool,
      message = result.message,
      correction = result.correction;

    Validator.change_status_field(field_name, bool);

    // Sprawdź czy istnieje poprawiona wartość poli i jeśli tak to przypisz do tego pola.
    if($field.val() != correction && typeof correction !== 'undefined' && correction !== '')
      $field.val(correction);

    if(bool)
    {
      $field.removeClass('form_error');
      $status.html('').fadeOut(200);
    }
    else if(typeof message === 'undefined')
    {
      $field.addClass('form_error');
      $status.html('').fadeOut(200);
    }
    else
    {
      $field.addClass('form_error');
      $status.html(message).fadeIn(200);
    }
  }

  let test_form = Validator.check_list_field();
  change_status_blockade(test_form);

  running_validator = false;
};


let change_status_blockade = function(test_form)
{
  if(typeof test_form === 'boolean')
  {
    let $button = $form.find('*[type=submit]');

    if(test_form)
      $button.prop('disabled', false);
    else
      $button.prop('disabled', true);
  }
};


//////////////////////////////   VIEWS - SHOW/HIDE PASSWORD   ///////////////////////////////////

let show_password = function(checker)
{
  let $checker = $(checker),
    $field = $checker.parent().find('input[name=password]');
  $field.attr('type', 'text');
};


let hide_password = function(checker)
{
  let $checker = $(checker),
    $field = $checker.parent().find('input[name=password]');
  $field.attr('type', 'password');
};
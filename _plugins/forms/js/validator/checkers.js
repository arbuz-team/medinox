
import {Constructor_Validator, checker} from './views'

export {Constructor_Validator} from './views'

/////////////////////////////  Prepare checkers  ///////////////////////////////

Constructor_Validator.prototype.types = {};

/////////////////////////////  Checkers  ///////////////////////////////

checker.create_checker('email', function(value, callback)
{
	let result = checker.create_result(),
	  re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	if(checker.check_condition( re.test(value) ))
    result = checker.create_error('It\'s not email.');

  callback(result);
});


checker.create_checker('email_not_in_db', function(value, callback)
{
  let result = checker.create_result(),
    re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if(checker.check_condition( re.test(value) ))
  {
    result = checker.create_error('It\'s not email.');
    callback(result);
  }
  else
  {
    checker.exist_in_db('email', value, callback, 'Someone already has that email. Try another?');
  }
});


checker.create_checker('password', function(value, callback)
{
  let result = checker.create_result();

  if(checker.check_condition( value.length >= 8 ))
    result = checker.create_error('Short passwords are easy to guess. Try one with at least 8 characters.');

  callback(result);
});


checker.create_checker('proper_name', function(value, callback)
{
  value = value.charAt(0).toUpperCase() + value.slice(1);

  let result = checker.create_result(value);

  if(checker.check_condition( value.length >= 3 ))
    result = checker.create_error('The name is too short.', value);

  callback(result);
});


checker.create_checker('number', function(value, callback)
{
  value = value.replace(/\s/g, '');

  let result = checker.create_result(value);

  if(checker.check_condition( value.length === 9 ))
    result = checker.create_error('Number length is 9 digits.', value);

  if(checker.check_condition( !isNaN(value) ))
    result = checker.create_error('The number must consist of digits.', value);

  callback(result);
});


checker.create_checker('full_name', function(value, callback)
{
  value = value.replace(/\w\S*/g, function(txt){
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
  value = value.replace('  ', ' ');

  let result = checker.create_result(value),
    split = value.split(' ');

  if(checker.check_condition( split.length >= 2 && split[0] !== '' && split[1] !== '' ))
    result = checker.create_error('Full name consists of minimum 2 word.', value);

  callback(result);
});


checker.create_checker('no_empty', function(value, callback)
{
  let result = checker.create_result();

  if(checker.check_condition( value !== '' ))
    result = checker.create_error("You can't leave this empty.", value);

  callback(result);
});

////////////////      LENGTH      ///////////////////

checker.create_checker('length_3', function(value, callback)
{
  let result = checker.create_result();

  if(checker.check_condition( value.length >= 3 ))
    result = checker.create_error('It\'s too short.', value);

  callback(result);
});

////////////////////////////////////////////
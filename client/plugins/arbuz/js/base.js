/*    JavaScript    */

import {Dictionary} from '../../dictionary/base';

/*---------------- Interfejs funkcji standardowych ----------------*/

/**
 *    Defining global veriables
 */

window.APP = {};
window.APP.DATA = {};
window.APP.dictionary = new Dictionary();


/**
 *    Defining global functions
 */

APP.add_own_event = function add_own_event(name, callback)
{
  window.removeEventListener(name, callback, false);
  window.addEventListener(name, callback, false);
};

APP.throw_event = function throw_event(event)
{
  window.dispatchEvent(event);
};


$.prototype.add_data = function add_data(name, value)
{
  $(this).attr('data-'+ name, value);
  $(this).data(name, value);
  return this;
};

$.prototype.change_data = function change_data(name, value)
{
  $(this).add_data(name, value);
  return this;
};


$.prototype.delete_data = function delete_data(name)
{
  $(this).removeAttr('data-'+ name);
  $(this).removeData(name);
  return this;
};


$.prototype.serialize_object = function()
{
  let
    fields = $(this).serializeArray(),
    form_object = {};

  // Appending normal fields to array
  $.each( fields , function( i, field )
  {
    form_object[ field.name ] = field.value;
  });

  return form_object;
};






Array.prototype.delete_empty = function delete_empty()
{
  let url_array = [];
  
  for(let j = 0, i = 0; this.length > i; i++)
  {
    if(this[ i ])
    {
      url_array[ j ] = this[ i ];
      j++;
    }
  }
  return url_array;
};



if (!String.prototype.splice)
{
  /**
   * {JSDoc}
   *
   * The splice() method changes the content of a string by removing a range of
   * characters and/or adding new characters.
   *
   * @this {String}
   * @param {number} start Index at which to start changing the string.
   * @param {number} delCount An integer indicating the number of old chars to remove.
   * @param {string} newSubStr The String that is spliced in.
   * @return {string} A new string with the spliced substring.
   */
  String.prototype.splice = function(start, delCount, newSubStr) {
    return this.slice(0, start) + newSubStr + this.slice(start + Math.abs(delCount));
  };
}


window.APP.add_if_isset = function(from, to, from_what, to_what)
{
  if(typeof from[from_what] !== 'undefined')
    if(from_what && to_what)
      to[to_what] = from[from_what];
    else if(from_what)
      to[from_what] = from[from_what];
};
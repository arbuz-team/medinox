/**
 * Created by mrskull on 20.02.17.
 */


export let Dictionary = function()
{
  let
    dictionary = window.DATA.dictionary;

  if(!dictionary)
    dictionary = {};


  this.add_word = function(word, translated_word)
  {
    if(typeof dictionary[word] === 'undefined')
    {
      dictionary[word] = translated_word;
      return true;
    }

    console.error('Error in Dictionary: This word is using now.');
    return false;
  };


  this.get_word = function(word)
  {
    if(typeof dictionary[word] !== 'undefined')
      return dictionary[word];

    console.error('Error in Dictionary: This word is not exist.');
    return false;
  };


  this.show_all = function()
  {
    console.log(dictionary);
  };
};


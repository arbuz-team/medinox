/**
 * Created by mrskull on 24.11.16.
 */

import * as searcher_controllers       from '../../searcher/js/controllers'
import * as cart_controllers         from '../../cart/js/controllers'
import * as navigation_controllers   from '../../navigation/js/controllers'
import * as header_controllers       from '../../header/js/controllers'
import * as dialog_controllers         from '../../dialog/js/controllers'

import * as ground_controllers       from '../../ground/js/controllers'


/*---------------- Wydarzenia na stronie ----------------*/

let

  reload_sign_in = function(permissions)
  {
    return function()
    {
      let
        delay = window.APP.DATA.delay,

        reload = function()
        {
          window.APP.throw_event(window.EVENTS.plugins.reload_navigation);

          if(permissions === 'root')
            window.APP.throw_event(window.EVENTS.plugins.reload_searcher);

          if(permissions === 'user')
            window.APP.throw_event(window.EVENTS.plugins.reload_cart);
        };

      if(delay)
        setTimeout(reload, delay);
      else
        reload();
    };
  },

  reload_website = function()
  {
    if(!window.APP.DATA.delay)
      window.APP.DATA.delay = 0;

    setTimeout(window.location.reload, window.APP.DATA.delay);
  },


  define = function()
  {
    // Usuń wszystkie wydarzenia ze wszystkich elementów
    $( '*' ).off();

    searcher_controllers.define();
    cart_controllers.define();
    navigation_controllers.define();
    header_controllers.define();
    dialog_controllers.define();
    ground_controllers.define();
  };


export let start = function()
{
  window.addEventListener('define', define, false);
  window.APP.add_own_event('reload_website', reload_website);
  window.APP.add_own_event('reload_user_sign_in', reload_sign_in('user'));
  window.APP.add_own_event('reload_root_sign_in', reload_sign_in('root'));

  searcher_controllers.start();
  cart_controllers.start();
  navigation_controllers.start();
  header_controllers.start();
  ground_controllers.start();

  define();
};
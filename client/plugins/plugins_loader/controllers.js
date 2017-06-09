/**
 * Created by mrskull on 24.11.16.
 */

import {data_controller} from '../arbuz/js/structure'
import {Plugins_Loader_Views} from './views'


export let Plugins_Loader_Controllers = function(config)
{
  let
    plugin_loader_views = new Plugins_Loader_Views(config);

  this.load = plugin_loader_views.change_content;
  this.container = plugin_loader_views.models.settings.container;

  /**
   *    Defining private functions
   */


  this.redirect = function()
  {
    let
      url = data_controller.get('path'),
      delay = 0,
      variables = plugin_loader_views.models.variables;

    if(typeof APP !== 'undefined' && typeof APP.DATA !== 'undefined')
    {
      if(typeof APP.DATA.redirect !== 'undefined')
        url = APP.DATA.redirect;

      if(typeof APP.DATA.delay !== 'undefined')
      {
        delay = APP.DATA.delay;
        APP.DATA.delay = undefined;
      }
    }

    variables.can_do_redirect = true;
    clearTimeout(variables.redirect_time_out);

    variables.redirect_time_out = setTimeout(() =>
    {
      if(plugin_loader_views.models.variables.can_do_redirect === true)
        this.load(url);
    }, delay);
  };


  this.reload = function()
  {
    let delay = window.APP.DATA.delay;
    APP.DATA.delay = undefined;

    if(typeof delay !== 'number')
      delay = 0;

    setTimeout(plugin_loader_views.change_content, delay);
  };


  /**
   *    Defining public functions
   */

  this.define = function()
  {
    let
      plugin_name = plugin_loader_views.models.settings.name,
      auto_first_loading = plugin_loader_views.models.settings.auto_first_loading;

    window.APP.add_own_event(''+ plugin_name +'_reload', this.reload);


    if(auto_first_loading)
      window.APP.add_own_event('load', () => {
        plugin_loader_views.change_content();
      });
  };
};


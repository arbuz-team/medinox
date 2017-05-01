/**
 * Created by mrskull on 26.12.16.
 */

import {data_controller} from '../arbuz/js/structure'


export let Plugins_Loader_Models = function(config)
{
  let that = this;

  this.data_controller = data_controller;


/**
 *    Plugin settings
 */

  this.settings = {
    name: undefined,
    url: undefined,

    container: undefined,
    first_element: '*',

    auto_first_loading: false,
    load_with_page: false,

    duration: {
      show: 150,
      hide: 100,
    },

    opacity: {
      show: 1,
      hide: 0.4,
    },
  };


  // -- Load settings
  (function()
  {
    if(typeof config !== 'undefined')
    {
    // -- Name
      if(typeof config.name !== 'undefined')
        that.settings.name = config.name;

    // -- URL
      if(typeof config.url !== 'undefined')
        that.settings.url = window.APP.dictionary.get_word(config.url);


    // -- Container
      if(typeof config.load_with_page !== 'undefined')
        that.settings.load_with_page = config.load_with_page;


    // -- Container
      if(typeof config.auto_first_loading !== 'undefined')
        that.settings.auto_first_loading = config.auto_first_loading;


    // -- Load with page
      if(typeof config.container !== 'undefined')
        that.settings.container = config.container;

    // -- Duration
      if(typeof config.duration !== 'undefined')
      {
        let duration = config.duration;

        if(typeof duration.show !== 'undefined')
          that.settings.duration.show = duration.show;

        if(typeof duration.hide !== 'undefined')
          that.settings.duration.hide = duration.hide;
      }


    // -- Opacity
      if(typeof config.opacity !== 'undefined')
      {
        let opacity = config.opacity;

        if(typeof opacity.show !== 'undefined')
          that.settings.opacity.show = opacity.show;

        if(typeof opacity.hide !== 'undefined')
          that.settings.opacity.hide = opacity.hide;
      }
    }
  })();


/**
 *    Plugin variables
 */

  this.variables = {
    url: undefined,
    post_data: undefined,

    error: undefined,
    external_callback: undefined,

    can_do_load: true,
    can_do_redirect: true,
    redirect_time_out: undefined,
  };


/**
 *    Defining prepare functions
 */

  this.prepare_url = function(response_url)
  {
    if(!response_url)
      if(typeof this.settings.url !== 'undefined')
        response_url = this.settings.url;
      else
        response_url = data_controller.get('path');

    this.variables.url = response_url;
  };


  this.prepare_post_data = function(post_data)
  {
    if(!post_data)
      post_data = {};

    if( typeof post_data.__form__ === 'undefined')
      if( typeof post_data.__content__ === 'undefined')
        post_data['__content__'] = this.settings.name;


    this.variables.post_data = post_data;
  };


/**
 *    Defining refresh functions
 */

  this.refresh_data = function()
  {
    data_controller.reset();
  };


  this.refresh_events = function()
  {
    APP.throw_event( window.EVENTS.define );
  };


  this.refresh_scroll = function()
  {
    $(this.settings.container)
      .parent().scrollTop(0);
  };


/**
 *    Defining download functions
 */

  this.download_content = function(url, callback)
  {
    this.prepare_url(url);
    window.APP.http_request(this.variables.url, this.variables.post_data, callback);
  };
};




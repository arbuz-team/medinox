/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;
/******/
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	__webpack_require__(1);
	
	window.viewability = function () {
	  return __webpack_require__(5);
	}();

/***/ },
/* 1 */
/***/ function(module, exports) {

	// removed by extract-text-webpack-plugin

/***/ },
/* 2 */,
/* 3 */,
/* 4 */,
/* 5 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	__webpack_require__(6);
	
	__webpack_require__(8);
	
	var _controllers = __webpack_require__(11);
	
	var page_controller = _interopRequireWildcard(_controllers);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	window.APP.add_own_event('load', function () {
	  page_controller.start();
	});

/***/ },
/* 6 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _base = __webpack_require__(7);
	
	window.APP = {};
	APP.DATA = {};
	APP.dictionary = new _base.Dictionary();
	
	APP.add_own_event = function add_own_event(name, callback) {
	  window.removeEventListener(name, callback, false);
	  window.addEventListener(name, callback, false);
	};
	
	APP.throw_event = function throw_event(event) {
	  window.dispatchEvent(event);
	};
	
	$.prototype.add_data = function add_data(name, value) {
	  $(this).attr('data-' + name, value);
	  $(this).data(name, value);
	  return this;
	};
	
	$.prototype.change_data = function change_data(name, value) {
	  $(this).add_data(name, value);
	  return this;
	};
	
	$.prototype.delete_data = function delete_data(name) {
	  $(this).removeAttr('data-' + name);
	  $(this).removeData(name);
	  return this;
	};
	
	$.prototype.serialize_object = function () {
	  var fields = $(this).serializeArray(),
	      form_object = {};
	
	  $.each(fields, function (i, field) {
	    form_object[field.name] = field.value;
	  });
	
	  return form_object;
	};
	
	Array.prototype.delete_empty = function delete_empty() {
	  var url_array = [];
	
	  for (var j = 0, i = 0; this.length > i; i++) {
	    if (this[i]) {
	      url_array[j] = this[i];
	      j++;
	    }
	  }
	  return url_array;
	};
	
	if (!String.prototype.splice) {
	  String.prototype.splice = function (start, delCount, newSubStr) {
	    return this.slice(0, start) + newSubStr + this.slice(start + Math.abs(delCount));
	  };
	}
	
	APP.add_if_isset = function (from, to, from_what, to_what) {
	  if (typeof from[from_what] !== 'undefined') if (from_what && to_what) to[to_what] = from[from_what];else if (from_what) to[from_what] = from[from_what];
	};

/***/ },
/* 7 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	var Dictionary = exports.Dictionary = function Dictionary() {
	  var dictionary = window.DATA.dictionary;
	
	  if (!dictionary) dictionary = {};
	
	  this.add_word = function (word, translated_word) {
	    if (typeof dictionary[word] === 'undefined') {
	      dictionary[word] = translated_word;
	      return true;
	    }
	
	    console.error('Error in Dictionary: This word is using now.');
	    return false;
	  };
	
	  this.get_word = function (word) {
	    if (typeof dictionary[word] !== 'undefined') return dictionary[word];
	
	    console.error('Error in Dictionary: This word is not exist.');
	    return false;
	  };
	
	  this.show_all = function () {
	    console.log(dictionary);
	  };
	};

/***/ },
/* 8 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _structure = __webpack_require__(9);
	
	var send_post_preprocess_url = function send_post_preprocess_url(response_url) {
	  if (response_url && response_url.substring && response_url.substring(0, 1) === '/') return response_url;else return _structure.data_controller.get('path');
	},
	    send_post_prepare = function send_post_prepare(post_data) {
	  if (!post_data) post_data = {};
	
	  post_data[_structure.data_controller.get_crsf('name')] = _structure.data_controller.get_crsf('value');
	
	  return post_data;
	},
	    create_callback = function create_callback(callback) {
	  return function (response, status) {
	    var html = response.responseText,
	        code = response.status;
	
	    callback(html, status, code);
	  };
	};
	
	APP.http_request = function (url, post_data, callback) {
	  url = send_post_preprocess_url(url);
	  post_data = send_post_prepare(post_data);
	
	  $.ajax({
	    type: 'POST',
	    url: url,
	    data: post_data,
	    complete: create_callback(callback)
	  });
	};

/***/ },
/* 9 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.data_controller = undefined;
	
	__webpack_require__(10);
	
	var data_controller = exports.data_controller = new function Data_Controler() {
	  var private_data = void 0,
	      public_data = void 0;
	
	  this.reset = function () {
	    private_data = {
	      path: location.pathname,
	      all_url: location.href,
	      history: [],
	      csrf_token: $('input[ name=csrfmiddlewaretoken ]').val() || ''
	    };
	
	    public_data = {
	      can_do_redirect: false,
	      can_do_open_plugin: true,
	      page_name: 'Spasungate',
	      title: 'Loading... - Spasungate',
	      description: 'This page is shop, which is ownership Spasungate.',
	      statement_content: 'Empty statement.'
	    };
	  };
	
	  this.reset();
	
	  this.get = function (name) {
	    if (typeof private_data[name] !== 'undefined') return private_data[name];else if (typeof public_data[name] !== 'undefined') return public_data[name];else {
	      console.error('Data structure error: Wrong call! Veriable with this name doesn\'t exist: "' + name + '".');
	    }
	  };
	
	  this.get_crsf = function (what) {
	    if (what === 'name') return 'csrfmiddlewaretoken';else if (what === 'value') return private_data.csrf_token;else console.error('Data structure error: Wrong call! Veriable with this name doesn\'t exist (crsf).');
	  };
	
	  this.change = function (name, wartosc) {
	    if (typeof public_data[name] !== 'undefined') public_data[name] = wartosc;else console.error('Data structure error: Wrong call! Veriable with this name doesn\'t exist: "' + name + '".');
	  };
	
	  this.change_much = function (object) {
	    for (var name in object) {
	      if (object.hasOwnProperty(name)) {
	        if (name === 'title') {
	          if (object[name] !== '') this.change(name, object[name] + ' - ' + public_data.page_name);else this.change(name, public_data.page_name);
	        } else this.change(name, object[name]);
	      }
	    }
	  };
	}();

/***/ },
/* 10 */
/***/ function(module, exports) {

	'use strict';
	
	window.EVENTS = {
		send_request: new Event('send_request'),
		define: new Event('define'),
		redirect: new Event('redirect'),
		reload_website: new Event('reload_website'),
	
		part: {
			open_cart: new Event('cart_open'),
			open_navigation: new Event('navigation_open'),
			open_searcher: new Event('searcher_open'),
	
			open_or_close_cart: new Event('cart_open_or_close'),
	
			close: new Event('plugins_close'),
			close_cart: new Event('cart_close'),
			close_navigation: new Event('navigation_close'),
			close_dialog: new Event('dialog_close'),
	
			reload_root_sign_in: new Event('reload_root_sign_in'),
			reload_user_sign_in: new Event('reload_user_sign_in'),
	
			reload_navigation: new Event('navigation_reload'),
			reload_header: new Event('header_reload'),
			reload_cart: new Event('cart_reload'),
			reload_searcher: new Event('searcher_reload'),
			reload_ground: new Event('ground_reload'),
			reload_dialog: new Event('dialog_reload')
		}
	};

/***/ },
/* 11 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.start = undefined;
	
	var _controllers = __webpack_require__(12);
	
	var searcher_controllers = _interopRequireWildcard(_controllers);
	
	var _controllers2 = __webpack_require__(44);
	
	var cart_controllers = _interopRequireWildcard(_controllers2);
	
	var _controllers3 = __webpack_require__(48);
	
	var navigation_controllers = _interopRequireWildcard(_controllers3);
	
	var _controllers4 = __webpack_require__(49);
	
	var header_controllers = _interopRequireWildcard(_controllers4);
	
	var _controller = __webpack_require__(50);
	
	var dialog_controllers = _interopRequireWildcard(_controller);
	
	var _controllers5 = __webpack_require__(62);
	
	var ground_controllers = _interopRequireWildcard(_controllers5);
	
	var _part = __webpack_require__(15);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var reload_sign_in = function reload_sign_in(permissions) {
		return function () {
			var delay = APP.DATA.delay,
			    reload = function reload() {
				APP.throw_event(EVENTS.part.reload_header);
				APP.throw_event(EVENTS.part.reload_navigation);
	
				if (permissions === 'root') APP.throw_event(EVENTS.part.reload_searcher);
	
				if (permissions === 'user') APP.throw_event(EVENTS.part.reload_cart);
			};
	
			if (delay) setTimeout(reload, delay);else reload();
		};
	},
	    reload_website = function reload_website() {
		var delay = void 0;
	
		if (APP.DATA.delay) delay = APP.DATA.delay;else delay = 0;
	
		setTimeout(function () {
			window.location.reload();
		}, delay);
	},
	    define = function define() {
		$('*').off();
	
		searcher_controllers.define();
		cart_controllers.define();
		navigation_controllers.define();
		header_controllers.define();
		dialog_controllers.define();
		ground_controllers.define();
	};
	
	var start = exports.start = function start() {
		var request_manager = new _part.Request_Manager_Part();
	
		APP.add_own_event('define', define);
		APP.add_own_event('reload_website', reload_website);
		APP.add_own_event('reload_user_sign_in', reload_sign_in('user'));
		APP.add_own_event('reload_root_sign_in', reload_sign_in('root'));
	
		searcher_controllers.get_content();
		cart_controllers.get_content();
		navigation_controllers.get_content();
		header_controllers.get_content();
		ground_controllers.get_content();
	
		request_manager.send_list();
	
		define();
	};

/***/ },
/* 12 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.get_content = exports.define = undefined;
	
	var _part = __webpack_require__(13);
	
	var _controllers = __webpack_require__(22);
	
	var _controllers2 = __webpack_require__(25);
	
	var _controllers3 = __webpack_require__(41);
	
	var container = '.searcher',
	    config_loader = {
		name: 'searcher',
		container: container
	},
	    searcher_loader = new _part.Part_Loader_Part(config_loader),
	    searcher_motion_controllers = new _controllers.Plugins_Motion_Controllers({
		container: '#SEARCHER',
		content: container,
		open: 'right',
		can_open_by: 'width',
		can_open_to: 1000,
		duration_open: 200,
		duration_close: 200
	}),
	    post_button_controllers = new _controllers3.Post_Button_Controllers({
		container: '#SEARCHER'
	}),
	    searcher_form_controllers = new _controllers2.Form_Controllers(config_loader);
	
	var define = exports.define = function define() {
		APP.add_own_event('searcher_open', searcher_motion_controllers.plugin_open);
	
		searcher_motion_controllers.define();
		searcher_form_controllers.define();
		post_button_controllers.define();
	},
	    get_content = exports.get_content = function get_content() {
		searcher_loader.define();
		searcher_loader.load_content();
	
		searcher_motion_controllers.set_start_position();
	};

/***/ },
/* 13 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Part_Loader_Part = Part_Loader_Part;
	
	var _structure = __webpack_require__(9);
	
	var _data = __webpack_require__(14);
	
	var _part = __webpack_require__(15);
	
	var _controller = __webpack_require__(17);
	
	function Part_Loader_Part(config) {
		_controller.Part_Loader.call(this, config);
	
		this.settings.load_meta_tags = false;
	
		(0, _data.add_to_settings)(config, this, 'load_meta_tags');
	}
	
	Part_Loader_Part.prototype = Object.create(_controller.Part_Loader.prototype);
	
	Part_Loader_Part.prototype.prepare_post_data = function (post_data) {
		if (!post_data) post_data = {};
	
		if (typeof post_data.__content__ === 'undefined') post_data['__content__'] = this.settings.name;
	
		this.variables.post_data = post_data;
	};
	
	Part_Loader_Part.prototype.send_request = function (actually_url) {
		var post_data = this.variables.post_data,
		    request_manager = new _part.Request_Manager_Part();
	
		this.response = request_manager.next(actually_url, post_data);
	};
	
	Part_Loader_Part.prototype.load_header_page = function (object) {
		_structure.data_controller.change_much({
			title: object.title,
			description: object.description
		});
	
		$('title').html(_structure.data_controller.get('title'));
		$('meta[ name="description" ]').attr('content', _structure.data_controller.get('description'));
	};
	
	Part_Loader_Part.prototype.after_show_content = function (data) {
		if (this.external_callback) this.external_callback(data.html, data.status, data.code);
	
		if (this.settings.load_meta_tags && APP.DATA) this.load_header_page(APP.DATA);
	};
	
	Part_Loader_Part.prototype.receive_response = function () {
		var _this = this;
	
		return new Promise(function (resolve) {
			_this.response.then(function (response) {
				var data = response[_this.settings.name],
				    precise_data = {
					html: data.html,
					status: 'success',
					code: data.status
				};
	
				resolve(precise_data);
			});
		});
	};
	
	Part_Loader_Part.prototype.load_simple_content = function (url, post_data, callback) {
		var request_manager = new _part.Request_Manager_Part();
	
		this.load_content(url, post_data, callback);
		request_manager.send_list();
	};

/***/ },
/* 14 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var is_undefined = exports.is_undefined = function is_undefined(object) {
		return typeof object === 'undefined';
	},
	    is_not_undefined = exports.is_not_undefined = function is_not_undefined(object) {
		return typeof object !== 'undefined';
	},
	    add_to_object = exports.add_to_object = function add_to_object(from, to, from_what, to_what) {
		if (is_undefined(from[from_what])) return false;
	
		if (from_what && to_what) to[to_what] = from[from_what];else if (from_what) to[from_what] = from[from_what];
	},
	    add_to_settings = exports.add_to_settings = function add_to_settings(from, to, from_what, to_what) {
		if (is_undefined(to) && is_undefined(to.settings)) {
			console.error('Data Utilities error: Invalid object.');
			return false;
		}
	
		add_to_object(from, to.settings, from_what, to_what);
	};

/***/ },
/* 15 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Request_Manager_Part = Request_Manager_Part;
	
	var _structure = __webpack_require__(9);
	
	var _init = __webpack_require__(16);
	
	function Request_Manager_Part() {
		if (_typeof(Request_Manager_Part.instance) === 'object') return Request_Manager_Part.instance;
	
		_init.Request_Manager.call(this);
	
		Request_Manager_Part.instance = this;
	}
	
	Request_Manager_Part.prototype = Object.create(_init.Request_Manager.prototype);
	
	Request_Manager_Part.prototype.add_request = function (url, post_data) {
		if (this.sending === undefined) this.clear_request();
	
		if (this.requests.url === undefined) this.requests.url = url;
	
		this.requests.list.push(post_data);
	};
	
	Request_Manager_Part.prototype.clear_request = function () {
		this.requests = {
			url: undefined,
			list: []
		};
	
		this.sending = false;
	};
	
	Request_Manager_Part.prototype.post_data_prepare = function () {
		var post_data = {
			__content__: ''
		};
	
		if (this.requests.list.length) {
			this.requests.list.forEach(function (element) {
				if (element.__content__) {
					post_data.__content__ += element.__content__ + ' ';
	
					delete element.__content__;
					Object.assign(post_data, element);
				} else return false;
			});
	
			post_data[_structure.data_controller.get_crsf('name')] = _structure.data_controller.get_crsf('value');
	
			return post_data;
		}
	
		return false;
	};
	
	Request_Manager_Part.prototype.run_sending = function () {
		var _this = this;
	
		if (this.sending === false) this.sending = new Promise(function (resolve, reject) {
			var timer = setTimeout(function () {
				_this.catch_timeout_error();
			}, 3000),
			    send_and_wait = function send_and_wait() {
				clearTimeout(timer);
	
				if (_this.sending === false) reject('Request Manager error: Promise doesn\'t exist.');else _this.send_request().then(function (response) {
					window.removeEventListener('send_request', send_and_wait, false);
					resolve(response);
				});
			};
	
			window.addEventListener('send_request', send_and_wait, false);
		});
	
		return this.sending;
	};
	
	Request_Manager_Part.prototype.next = function (url, post_data) {
		var _this2 = this;
	
		this.add_request(url, post_data);
	
		return new Promise(function (resolve) {
			_this2.run_sending().then(function (response) {
				_this2.clear_request();
	
				var data = response.__content__;
	
				resolve(data);
			});
		});
	};
	
	Request_Manager_Part.prototype.send_list = function () {
		APP.throw_event(window.EVENTS.send_request);
	};

/***/ },
/* 16 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Request_Manager = Request_Manager;
	
	var _structure = __webpack_require__(9);
	
	function Request_Manager() {
		this.requests = undefined;
		this.sending = undefined;
	}
	
	Request_Manager.prototype.add_request = function (url, post_data) {
		if (this.sending === undefined) this.clear_request();
	
		if (this.requests.url === undefined) this.requests.url = url || '';
	
		this.requests.data = post_data || {};
	};
	
	Request_Manager.prototype.clear_request = function () {
		this.requests = {
			url: undefined,
			data: {}
		};
	
		this.sending = false;
	};
	
	Request_Manager.prototype.preprocess_url = function () {
		var url = this.requests.url;
	
		if (url && url.substring && url.substring(0, 1) === '/') return url;else return _structure.data_controller.get('path');
	};
	
	Request_Manager.prototype.post_data_prepare = function () {
		if (this.requests.data) {
			var post_data = this.requests.data;
	
			post_data[_structure.data_controller.get_crsf('name')] = _structure.data_controller.get_crsf('value');
	
			return post_data;
		}
	
		return false;
	};
	
	Request_Manager.prototype.send_request = function () {
		var _this = this;
	
		return new Promise(function (resolve, reject) {
			var url = _this.preprocess_url(),
			    post_data = _this.post_data_prepare();
	
			if (post_data) $.ajax({
				type: 'POST',
				url: url,
				data: post_data,
				complete: resolve
			});else reject('Request Manager error: Invalid post data.');
		});
	};
	
	Request_Manager.prototype.catch_timeout_error = function () {
		console.error('Request Manager error: Request Timeout. ' + 'Run `send` in Request Manager.');
	
		this.clear_request();
	};
	
	Request_Manager.prototype.send = function (url, post_data) {
		var _this2 = this;
	
		this.add_request(url, post_data);
	
		return new Promise(function (resolve) {
			_this2.send_request().then(function (data) {
				_this2.clear_request();
	
				resolve(data);
			});
		});
	};

/***/ },
/* 17 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Part_Loader = undefined;
	
	var _init = __webpack_require__(18);
	
	Object.defineProperty(exports, 'Part_Loader', {
		enumerable: true,
		get: function get() {
			return _init.Part_Loader;
		}
	});
	
	var _structure = __webpack_require__(9);
	
	__webpack_require__(19);
	
	__webpack_require__(20);
	
	_init.Part_Loader.prototype.redirect = function () {
		var _this = this;
	
		var url = _structure.data_controller.get('path'),
		    delay = 0,
		    variables = this.variables;
	
		if (typeof APP.DATA.redirect !== 'undefined') url = APP.DATA.redirect;
	
		if (typeof APP.DATA.delay !== 'undefined') {
			delay = APP.DATA.delay;
			APP.DATA.delay = undefined;
		}
	
		variables.can_do_redirect = true;
		clearTimeout(variables.redirect_time_out);
	
		variables.redirect_time_out = setTimeout(function () {
			if (_this.variables.can_do_redirect === true) _this.load_content(url);
		}, delay);
	};
	
	_init.Part_Loader.prototype.reload = function () {
		var delay = 0;
	
		if (typeof APP.DATA.delay !== 'undefined') {
			delay = APP.DATA.delay;
			APP.DATA.delay = undefined;
		}
	
		setTimeout(function () {}, delay);
	};
	
	_init.Part_Loader.prototype.define = function () {
		var _this2 = this;
	
		var part_name = this.settings.name;
	
		APP.add_own_event(part_name + '_reload', function () {
			_this2.reload();
		});
	};

/***/ },
/* 18 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Part_Loader = Part_Loader;
	
	var _data = __webpack_require__(14);
	
	function Part_Loader(config) {
	
		if (typeof config === 'undefined') {
			console.error('Part Loader error: Invalid configuration.');
			return {};
		}
	
		this.settings = {
			name: undefined,
			url: undefined,
	
			container: undefined,
	
			duration_show: 150,
			duration_hide: 100,
	
			opacity_show: 1,
			opacity_hide: 0.4
		};
	
		(0, _data.add_to_settings)(config, this, 'name');
		(0, _data.add_to_settings)(config, this, 'container');
	
		(0, _data.add_to_settings)(config, this, 'duration_show');
		(0, _data.add_to_settings)(config, this, 'duration_hide');
	
		(0, _data.add_to_settings)(config, this, 'opacity_show');
		(0, _data.add_to_settings)(config, this, 'opacity_hide');
	
		this.variables = {
			url: undefined,
			post_data: undefined,
			reload: false,
	
			error: undefined,
			external_callback: undefined,
	
			can_do_load: true,
			can_do_redirect: true,
			redirect_time_out: undefined
		};
	}

/***/ },
/* 19 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _structure = __webpack_require__(9);
	
	var _part = __webpack_require__(15);
	
	var _init = __webpack_require__(18);
	
	_init.Part_Loader.prototype.if_reload = function (url) {
		var old_url = _structure.data_controller.get('path'),
		    new_url = url;
	
		return old_url === new_url || !new_url;
	};
	
	_init.Part_Loader.prototype.refresh_data = function () {
		_structure.data_controller.reset();
	};
	
	_init.Part_Loader.prototype.refresh_events = function () {
		APP.throw_event(EVENTS.define);
	};
	
	_init.Part_Loader.prototype.check_for_errors = function (status, code) {
		var _this = this;
	
		var $container = $(this.settings.container),
		    error = this.variables.error;
	
		if (status !== 'success') if (error === true) $container.html('An error has occurred while connecting to server. ' + 'Please, refresh website or check your connect with network.');else {
			this.variables.error = true;
	
			this.prepare_post_data({ __content__: 'ground' });
			this.send_request('/statement/' + code + '/');
			this.receive_response().then(function () {
				_this.show_content();
			});
	
			return true;
		}
		return false;
	};
	
	_init.Part_Loader.prototype.prepare_content_to_change = function (url, post_data) {
		this.variables.can_do_redirect = false;
		this.variables.reload = this.if_reload(url);
	
		this.refresh_data();
		this.prepare_post_data(post_data);
	};
	
	_init.Part_Loader.prototype.prepare_post_data = function (post_data) {
		if (!post_data) post_data = {};
	
		if (typeof post_data.__form__ === 'undefined') if (typeof post_data.__content__ === 'undefined') post_data['__content__'] = this.settings.name;
	
		this.variables.post_data = post_data;
	};
	
	_init.Part_Loader.prototype.send_request = function (actually_url) {
		var post_data = this.variables.post_data,
		    request_manager = new _part.Request_Manager_Part();
	
		this.response = request_manager.send(actually_url, post_data);
	};
	
	_init.Part_Loader.prototype.receive_response = function () {
		var _this2 = this;
	
		return new Promise(function (resolve) {
			_this2.response.then(function (response) {
				var data = response.__content__[_this2.settings.name],
				    precise_data = {
					html: data.html,
					code: data.status
				};
	
				if (200 <= data.status < 300) precise_data.status = 'success';else if (400 <= data.status < 600) precise_data.status = 'error';
	
				resolve(precise_data);
			});
		});
	};

/***/ },
/* 20 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _img_loader = __webpack_require__(21);
	
	var img_loader = _interopRequireWildcard(_img_loader);
	
	var _init = __webpack_require__(18);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	_init.Part_Loader.prototype.hide_content = function () {
		var _this = this;
	
		return new Promise(function (resolve) {
			var container = _this.settings.container,
			    opacity = _this.settings.opacity_hide,
			    duration = _this.settings.duration_hide;
	
			$(container).animate({ opacity: opacity }, duration, resolve);
		});
	};
	
	_init.Part_Loader.prototype.prepare_content_to_show = function (data) {
		var $container = $(this.settings.container),
		    error = this.variables.error;
	
		if (this.variables.reload === false) $container.scrollTop(0);
	
		if (this.check_for_errors(data.status, data.code)) return false;
	
		if (error !== true || status === 'success') $container.html(data.html);
	
		this.variables.error = false;
		this.variables.url = '';
	
		this.refresh_events();
		img_loader.define();
	};
	
	_init.Part_Loader.prototype.show_content = function () {
		var _this2 = this;
	
		return new Promise(function (resolve) {
			var container = _this2.settings.container,
			    opacity = _this2.settings.opacity_show,
			    duration = _this2.settings.duration_show;
	
			$(container).animate({ opacity: opacity }, duration, resolve);
		});
	};
	
	_init.Part_Loader.prototype.after_show_content = function (data) {
		if (this.external_callback) this.external_callback(data.html, data.status, data.code);
	};
	
	_init.Part_Loader.prototype.load_content = function (url, post_data, callback) {
		var _this3 = this;
	
		this.variables.url = url;
		this.external_callback = callback;
	
		this.prepare_content_to_change(url, post_data);
	
		this.send_request(url);
	
		this.hide_content().then(function () {
			_this3.receive_response().then(function (data) {
				_this3.prepare_content_to_show(data);
	
				_this3.show_content().then(function () {
					_this3.after_show_content(data);
				});
			});
		});
	};

/***/ },
/* 21 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	
	var $query = function $query(css_query) {
	  return document.querySelectorAll(css_query);
	};
	
	var attr = function attr(elem, name) {
	  return elem.getAttribute(name);
	};
	
	var define = exports.define = function define() {
	  var $images = $query('img'),
	      default_src = '/static/img/puzzle_256.png',
	      image = new Image();
	
	  function download_img($imgs, i) {
	    if (!$imgs[i]) return false;
	
	    var downloadingImage = new Image(),
	        data_src = attr($imgs[i], 'data-src');
	
	    downloadingImage.onload = function () {
	      $imgs[i].src = this.src;
	      setTimeout(function () {
	        $imgs[i].style = 'opacity: 1;';
	        download_img($images, i + 1);
	      }, 100);
	    };
	
	    downloadingImage.onerror = function () {
	      $imgs[i].src = default_src;
	      $imgs[i].alt = 'Sorry, an error has occurred.';
	      setTimeout(function () {
	        $imgs[i].style = 'opacity: 1;';
	        $imgs[i].setAttribute('class', 'error');
	        download_img($images, i + 1);
	      }, 100);
	    };
	
	    downloadingImage.src = data_src;
	  }
	
	  image.onload = function () {
	    download_img($images, 0);
	  };
	
	  image.src = default_src;
	};

/***/ },
/* 22 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Plugins_Motion_Controllers = undefined;
	
	var _views = __webpack_require__(23);
	
	var Plugins_Motion_Controllers = exports.Plugins_Motion_Controllers = function Plugins_Motion_Controllers(config) {
		var plugin_motion_views = new _views.Plugins_Motion_Views(config),
		    settings = plugin_motion_views.models.settings;
	
		this.views = plugin_motion_views;
	
		var pre_plugin_close = function pre_plugin_close() {
			var container = settings.container,
			    $container = $(container),
			    $window = $(window);
	
			if (container !== '#CART') plugin_motion_views.plugin_close();else if ($container.outerWidth() === $window.width()) plugin_motion_views.plugin_close();
		},
		    if_horizontal_resize = function if_horizontal_resize(callback) {
			var window_width = void 0,
			    set_window_width = function set_window_width() {
				window_width = window.innerWidth;
			};
	
			set_window_width();
	
			return function () {
				var new_window_width = window.innerWidth;
	
				if (window_width != new_window_width) {
					set_window_width();
					callback();
				}
			};
		},
		    stop_propagation = function stop_propagation(event) {
			event.stopPropagation();
		};
	
		this.set_start_position = function () {
			var $container = $(settings.container),
			    position = void 0,
			    width = $container.outerWidth(),
			    direction_open = settings.direction_open,
			    direction_close = settings.direction_close;
	
			settings.height = '100%';
			settings.width = width;
	
			if (direction_open === 'top' || direction_open === 'bottom') position = -settings.height;else if (direction_open === 'left' || direction_open === 'right') position = -width;
	
			if (position) $($container).css(direction_close, position);
		};
	
		this.define = function () {
			var $window = $(window),
			    $body = $('body'),
			    $container = $(settings.container),
			    $content = $(settings.content),
			    $hide = $(settings.container + ' > ' + settings.hide);
	
			if (settings.container !== '#CART' && settings.container !== '#NAVIGATION') {
				$body.click(plugin_motion_views.plugin_close);
				$hide.click(plugin_motion_views.plugin_close);
				$container.click(stop_propagation);
				this.set_start_position();
			} else if (settings.container === '#NAVIGATION') {
				$container.click(plugin_motion_views.plugin_close);
				$content.click(stop_propagation);
				this.set_start_position();
			} else if ($container.outerWidth() === $window.width()) this.set_start_position();
	
			$window.resize(if_horizontal_resize(this.set_start_position));
			$window.resize(if_horizontal_resize(plugin_motion_views.plugin_close));
	
			APP.add_own_event('plugins_close', pre_plugin_close);
			APP.throw_event(EVENTS.part.close);
		};
	
		this.plugin_open = plugin_motion_views.plugin_open;
		this.plugin_close = plugin_motion_views.plugin_close;
		this.is_open = plugin_motion_views.is_open;
	};

/***/ },
/* 23 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Plugins_Motion_Views = undefined;
	
	var _models = __webpack_require__(24);
	
	var Plugins_Motion_Views = exports.Plugins_Motion_Views = function Plugins_Motion_Views(config) {
	  var models = new _models.Plugins_Motion_Models(config),
	      css = {};
	
	  this.models = models;
	  this.is_open = function () {
	    return models.check_is_open();
	  };
	
	  this.plugin_open = function (event) {
	    if (models.check_possibility_of_opening()) {
	      var container = models.settings.container,
	          hide = models.settings.hide,
	          direction_close = models.settings.direction_close,
	          duration_open = models.settings.duration_open;
	
	      css[direction_close] = 0;
	
	      $(container).stop().animate(css, duration_open, function () {
	        models.change_possibility_of_opening(false);
	      }).children(hide).fadeIn(duration_open);
	
	      var width = $(container).outerWidth();
	
	      if (container === '#CART') $('#GROUND .ground').addClass('smaller').stop().animate({ 'margin-right': width }, duration_open);
	    }
	  };
	
	  this.plugin_close = function () {
	    if (models.check_is_open()) {
	      var container = models.settings.container,
	          hide = models.settings.hide,
	          direction_open = models.settings.direction_open,
	          direction_close = models.settings.direction_close,
	          duration_close = models.settings.duration_close,
	          width = models.settings.width,
	          height = models.settings.height;
	
	      if (direction_open === 'top' || direction_open === 'bottom') css[direction_close] = '-' + height;else if (direction_open === 'right' || direction_open === 'left') css[direction_close] = -width;
	
	      $(container).stop().animate(css, duration_close, function () {
	        models.change_possibility_of_opening(true);
	      }).children(hide).fadeOut(duration_close);
	
	      if (container === '#CART') $('#GROUND .ground').removeClass('smaller').stop().animate({ 'margin-right': 0 }, duration_close);
	    }
	  };
	};

/***/ },
/* 24 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Plugins_Motion_Models = undefined;
	
	var _structure = __webpack_require__(9);
	
	var Plugins_Motion_Models = exports.Plugins_Motion_Models = function Plugins_Motion_Models(config) {
	  var that = this;
	
	  this.settings = {
	    container: undefined,
	    content: undefined,
	    hide: '.part-hide',
	
	    width: undefined,
	    height: undefined,
	
	    can_open_by: undefined,
	    can_open_from: undefined,
	    can_open_to: undefined,
	
	    direction_open: undefined,
	    direction_close: undefined,
	
	    duration_open: undefined,
	    duration_close: undefined
	  };
	
	  var load_settings = function load_settings() {
	    if (typeof config !== 'undefined') {
	      if (typeof config.container !== 'undefined') that.settings.container = config.container;
	
	      if (typeof config.content !== 'undefined') that.settings.content = config.container + ' ' + config.content;
	
	      var $container = $(that.settings.container);
	      that.settings.width = $container.outerWidth();
	      that.settings.height = $container.outerHeight();
	
	      if (typeof config.can_open_by !== 'undefined') that.settings.can_open_by = config.can_open_by;
	
	      if (typeof config.can_open_from !== 'undefined') that.settings.can_open_from = config.can_open_from;
	
	      if (typeof config.can_open_to !== 'undefined') that.settings.can_open_to = config.can_open_to;
	
	      if (typeof config.duration_open !== 'undefined') that.settings.duration_open = config.duration_open;
	
	      if (typeof config.duration_close !== 'undefined') that.settings.duration_close = config.duration_close;
	
	      if (typeof config.open !== 'undefined') {
	        switch (config.open) {
	          case 'right':
	            that.settings.swipe_open = 'swiperight';
	            that.settings.swipe_close = 'swipeleft';
	            that.settings.direction_open = 'right';
	            that.settings.direction_close = 'left';
	            break;
	
	          case 'left':
	            that.settings.swipe_open = 'swipeleft';
	            that.settings.swipe_close = 'swiperight';
	            that.settings.direction_open = 'left';
	            that.settings.direction_close = 'right';
	            break;
	
	          case 'up':
	            that.settings.swipe_open = 'swipeup';
	            that.settings.swipe_close = 'swipedown';
	            that.settings.direction_open = 'top';
	            that.settings.direction_close = 'bottom';
	            break;
	
	          case 'down':
	            that.settings.swipe_open = 'swipedown';
	            that.settings.swipe_close = 'swipeup';
	            that.settings.direction_open = 'bottom';
	            that.settings.direction_close = 'top';
	            break;
	        }
	      }
	    }
	  };
	
	  load_settings();
	
	  this.state = {
	    is_open: false,
	    is_not_set: true
	  };
	
	  var check_by_sizes = function check_by_sizes() {
	    var width_window = $(window).outerWidth(),
	        height_window = $(window).outerHeight(),
	        posibility = {
	      from: that.settings.can_open_from,
	      to: that.settings.can_open_to
	    };
	
	    if (that.settings.can_open_by === 'width') {
	      if (typeof posibility.from !== 'undefined') return width_window >= posibility.from;else if (typeof posibility.to !== 'undefined') return width_window <= posibility.to;
	    } else if (that.settings.can_open_by === 'height') {
	      if (typeof posibility.from !== 'undefined') return height_window >= posibility.from;else if (typeof posibility.to !== 'undefined') return height_window <= posibility.to;
	    }
	
	    return false;
	  },
	      check_mobile_by_sizes = function check_mobile_by_sizes() {
	    var width_window = parseInt($(window).outerWidth()),
	        max_mobile_width = 1000;
	
	    return width_window < max_mobile_width;
	  };
	
	  this.check_is_open = function () {
	    return this.state.is_open;
	  };
	
	  this.check_is_close = function () {
	    return !this.state.is_open;
	  };
	
	  this.check_possibility_of_opening = function () {
	    if (check_by_sizes()) if (_structure.data_controller.get('can_do_open_plugin')) return this.check_is_close();else if (this.settings.container === '#CART') return this.check_is_close();
	
	    return false;
	  };
	
	  this.change_possibility_of_opening = function (bool) {
	    this.state.is_open = !bool;
	
	    if (this.settings.container !== '#CART') _structure.data_controller.change('can_do_open_plugin', bool);
	  };
	};

/***/ },
/* 25 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Form_Controllers = undefined;
	
	var _models = __webpack_require__(26);
	
	var _controllers = __webpack_require__(30);
	
	var validator = _interopRequireWildcard(_controllers);
	
	var _controllers2 = __webpack_require__(34);
	
	var auto_form = _interopRequireWildcard(_controllers2);
	
	var _controllers3 = __webpack_require__(37);
	
	var selected_form = _interopRequireWildcard(_controllers3);
	
	var _controllers4 = __webpack_require__(38);
	
	var file_converter = _interopRequireWildcard(_controllers4);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var Form_Controllers = exports.Form_Controllers = function Form_Controllers(content_loader_controllers) {
		var form_models = new _models.Form_Models(content_loader_controllers),
		    variables = form_models.variables;
	
		var prepare_form_to_send = function prepare_form_to_send(event) {
			var form_action = $(this).attr('action'),
			    protocol = void 0;
	
			if (typeof form_action === 'string') protocol = form_action.substring(0, 4);
	
			if (protocol !== 'http') {
				event.preventDefault();
	
				var form_name = $(this).data('name'),
				    url = $(this).attr('action'),
				    form_object = $(this).serialize_object();
	
				variables.reload = $(this).data('reload');
				variables.redirect = $(this).data('redirect');
				variables.event = $(this).data('event');
				variables.delay = $(this).data('delay');
	
				form_models.send(form_name, url, form_object);
			}
		};
	
		this.define = function () {
			var $container = $(content_loader_controllers.container);
	
			$('form', $container).submit(prepare_form_to_send);
	
			validator.define($container);
			auto_form.define($container);
			selected_form.define($container);
			file_converter.define($container);
		};
	};

/***/ },
/* 26 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Form_Models = undefined;
	
	var _utilities = __webpack_require__(27);
	
	var utilities = _interopRequireWildcard(_utilities);
	
	var _form = __webpack_require__(28);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var Form_Models = exports.Form_Models = function Form_Models(config) {
		var that = this,
		    form_loader = new _form.Part_Loader_Form(config);
	
		this.variables = {
			name: undefined,
			reload: undefined,
			redirect: undefined,
			event: undefined,
			delay: undefined
		};
	
		var prepare_post_data = function prepare_post_data(form_name, post_data) {
			if (!post_data) post_data = {};
	
			post_data.__form__ = form_name;
	
			return post_data;
		},
		    end_loading = function end_loading(HTML_response, status) {
			if (utilities.html_is_error(HTML_response, status)) return false;
	
			var events = {
				reload: that.variables.reload,
				redirect: that.variables.redirect,
				events: that.variables.event,
				delay: that.variables.delay
			};
	
			utilities.reload_plugins(events);
			utilities.redirect_ground(events);
			utilities.launch_event(events);
		};
	
		this.send = function (form_name, url, post_data) {
			post_data = prepare_post_data(form_name, post_data);
	
			form_loader.load_simple_content(url, post_data, end_loading);
		};
	};

/***/ },
/* 27 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var html_is_error = exports.html_is_error = function html_is_error(HTML_response, status) {
		if (status !== 'success') return true;
	
		if (HTML_response === '') return true;
	
		return false;
	},
	    json_is_error = exports.json_is_error = function json_is_error(JSON_response, status) {
		if (status !== 'success') return true;
	
		var response = JSON.parse(JSON_response);
	
		if (response.__button__ !== 'true') return true;
	
		return false;
	},
	    prepare_delay = exports.prepare_delay = function prepare_delay(data) {
		var delay = data.delay;
	
		if (delay >= 0) APP.DATA.delay = delay;else APP.DATA.delay = 0;
	},
	    reload_plugins = exports.reload_plugins = function reload_plugins(data) {
		var plugins = data.reload,
		    plugins_array = void 0,
		    array_length = void 0;
	
		if (!plugins || typeof plugins !== 'string') return false;
	
		plugins_array = plugins.split(' ');
		array_length = plugins_array.length;
	
		for (var i = 0; i < array_length; ++i) {
			if (plugins_array[i]) {
				prepare_delay(data);
				APP.throw_event(EVENTS.part['reload_' + plugins_array[i]]);
			}
		}
	},
	    redirect_ground = exports.redirect_ground = function redirect_ground(data) {
		var url = data.redirect;
	
		if (!url || typeof url !== 'string') return false;
	
		APP.DATA.redirect = url;
		prepare_delay(data);
		APP.throw_event(EVENTS.redirect);
	},
	    launch_event = exports.launch_event = function launch_event(data) {
		var events = data.events,
		    events_array = void 0,
		    array_length = void 0;
	
		if (!events || typeof events !== 'string') return false;
	
		events_array = events.split(' ');
		array_length = events_array.length;
	
		for (var i = 0; i < array_length; ++i) {
			if (events_array[i]) {
				var select_event = events_array[i],
				    split_event = void 0,
				    ready_event = EVENTS;
	
				split_event = select_event.split('.');
	
				for (var _i = 0; split_event.length > _i; ++_i) {
					if (typeof ready_event[split_event[_i]] === 'undefined') console.error('Launch Event error: Event doesn\'t exist.');else ready_event = ready_event[split_event[_i]];
				}if (ready_event.constructor === Event) {
					prepare_delay(data);
					APP.throw_event(ready_event);
				} else console.error('Event error: This event doesn\'t exist');
			}
		}
	};

/***/ },
/* 28 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Part_Loader_Form = Part_Loader_Form;
	
	var _form = __webpack_require__(29);
	
	var _part = __webpack_require__(13);
	
	function Part_Loader_Form(config) {
		_part.Part_Loader_Part.call(this, config);
	}
	
	Part_Loader_Form.prototype = Object.create(_part.Part_Loader_Part.prototype);
	
	Part_Loader_Form.prototype.send_request = function (actually_url) {
		var post_data = this.variables.post_data,
		    request_manager = new _form.Request_Manager_Form();
	
		this.response = request_manager.send(actually_url, post_data);
	};
	
	Part_Loader_Form.prototype.prepare_post_data = function (post_data) {
		if (!post_data) post_data = {};
	
		post_data._direct_ = this.settings.name;
	
		this.variables.post_data = post_data;
	};
	
	Part_Loader_Form.prototype.receive_response = function () {
		var _this = this;
	
		return new Promise(function (resolve) {
			_this.response.then(function (response) {
	
				var precise_data = {
					html: response,
					status: 'success',
					code: 200
				};
	
				resolve(precise_data);
			});
		});
	};
	
	Part_Loader_Form.prototype.load_simple_content = function (url, post_data, callback) {
		this.load_content(url, post_data, callback);
	};

/***/ },
/* 29 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Request_Manager_Form = Request_Manager_Form;
	
	var _init = __webpack_require__(16);
	
	function Request_Manager_Form() {
	  _init.Request_Manager.call(this);
	}
	
	Request_Manager_Form.prototype = Object.create(_init.Request_Manager.prototype);

/***/ },
/* 30 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define = undefined;
	
	var _checkers = __webpack_require__(31);
	
	var Validators = {};
	
	window.Validators = Validators;
	
	var define = exports.define = function define($container) {
	
		$('form[data-test=yes]', $container).each(function () {
			var name = $(this).data('name'),
			    type = $(this).data('type');
			if (name || type) {
				Validators[name] = new _checkers.Constructor_Validator(name, type);
	
				var fields_of_form = Validators[name].hasErrors();
				for (var key in fields_of_form) {
					if (fields_of_form.hasOwnProperty(key)) {
						var $field = $('form[data-name=' + name + '] *[name=' + key + ']');
	
						if ($field.val()) validate($field);
					}
				}
			} else console.error('Validation Error: Incorrect or empty form name/type.');
		});
	
		$('form[data-test=yes] .test', $container).keyup(catch_event_validate).change(catch_event_validate);
	
		$('.show_password-checkbox', $container).change(function () {
			if ($(this).is(':checked')) show_password(this);else hide_password(this);
		});
	};
	
	var running_validator = false,
	    form_name = void 0,
	    $form = void 0,
	    Validator = void 0,
	    field = void 0,
	    field_name = void 0,
	    field_value = void 0;
	
	var catch_event_validate = function catch_event_validate() {
		validate(this);
	};
	
	var validate = function validate(response_field) {
		if (running_validator === false) {
			running_validator = true;
	
			field = response_field;
	
			form_name = $(field).parents('form').data('name');
			$form = $('form[data-name=' + form_name + ']');
			Validator = Validators[form_name];
			field_name = $(field).attr('name');
			field_value = $(field).val();
	
			Validator.field(field_name, field_value, show_status);
		}
	};
	
	var show_status = function show_status(result) {
		if (result) {
			var $field = $(field),
			    $status = $field.parent().find('.status');
	
			var bool = result.bool,
			    message = result.message,
			    correction = result.correction;
	
			Validator.change_status_field(field_name, bool);
	
			if ($field.val() != correction && typeof correction !== 'undefined' && correction !== '') $field.val(correction);
	
			if (bool) {
				$field.removeClass('form_error');
				$status.html('').fadeOut(200);
			} else if (typeof message === 'undefined') {
				$field.addClass('form_error');
				$status.html('').fadeOut(200);
			} else {
				$field.addClass('form_error');
				$status.html(message).fadeIn(200);
			}
		}
	
		var test_form = Validator.check_list_field();
		change_status_blockade(test_form);
	
		running_validator = false;
	};
	
	var change_status_blockade = function change_status_blockade(test_form) {
		if (typeof test_form === 'boolean') {
			var $button = $form.find('*[type=submit]');
	
			if (test_form) $button.prop('disabled', false);else $button.prop('disabled', true);
		}
	};
	
	var show_password = function show_password(checker) {
		var $checker = $(checker),
		    $field = $checker.parent().find('.input[type=password]');
	
		$field.attr('type', 'text');
	};
	
	var hide_password = function hide_password(checker) {
		var $checker = $(checker),
		    $field = $checker.parent().find('.input[type=text]');
	
		$field.attr('type', 'password');
	};

/***/ },
/* 31 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Constructor_Validator = undefined;
	
	var _views = __webpack_require__(32);
	
	Object.defineProperty(exports, 'Constructor_Validator', {
	  enumerable: true,
	  get: function get() {
	    return _views.Constructor_Validator;
	  }
	});
	
	
	_views.Constructor_Validator.prototype.types = {};
	
	_views.checker.create_checker('email', function (value, callback) {
	  var result = _views.checker.create_result(),
	      re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	
	  if (_views.checker.check_condition(re.test(value))) result = _views.checker.create_error('It\'s not email.');
	
	  callback(result);
	});
	
	_views.checker.create_checker('email_not_in_db', function (value, callback) {
	  var result = _views.checker.create_result(),
	      re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	
	  if (_views.checker.check_condition(re.test(value))) {
	    result = _views.checker.create_error('It\'s not email.');
	    callback(result);
	  } else {
	    _views.checker.exist_in_db('email', value, callback, 'Someone already has that email. Try another?');
	  }
	});
	
	_views.checker.create_checker('password', function (value, callback) {
	  var result = _views.checker.create_result();
	
	  if (_views.checker.check_condition(value.length >= 8)) result = _views.checker.create_error('Short passwords are easy to guess. Try one with at least 8 characters.');
	
	  callback(result);
	});
	
	_views.checker.create_checker('proper_name', function (value, callback) {
	  value = value.charAt(0).toUpperCase() + value.slice(1);
	
	  var result = _views.checker.create_result(value);
	
	  if (_views.checker.check_condition(value.length >= 3)) result = _views.checker.create_error('The name is too short.', value);
	
	  callback(result);
	});
	
	_views.checker.create_checker('number', function (value, callback) {
	  value = value.replace(/\s/g, '');
	
	  var result = _views.checker.create_result(value);
	
	  if (_views.checker.check_condition(value.length === 9)) result = _views.checker.create_error('Number length is 9 digits.', value);
	
	  if (_views.checker.check_condition(!isNaN(value))) result = _views.checker.create_error('The number must consist of digits.', value);
	
	  callback(result);
	});
	
	_views.checker.create_checker('full_name', function (value, callback) {
	  value = value.replace(/\w\S*/g, function (txt) {
	    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
	  });
	  value = value.replace('  ', ' ');
	
	  var result = _views.checker.create_result(value),
	      split = value.split(' ');
	
	  if (_views.checker.check_condition(split.length >= 2 && split[0] !== '' && split[1] !== '')) result = _views.checker.create_error('Full name consists of minimum 2 word.', value);
	
	  callback(result);
	});
	
	_views.checker.create_checker('no_empty', function (value, callback) {
	  var result = _views.checker.create_result();
	
	  if (_views.checker.check_condition(value !== '')) result = _views.checker.create_error("You can't leave this empty.", value);
	
	  callback(result);
	});
	
	_views.checker.create_checker('length_3', function (value, callback) {
	  var result = _views.checker.create_result();
	
	  if (_views.checker.check_condition(value.length >= 3)) result = _views.checker.create_error('It\'s too short.', value);
	
	  callback(result);
	});

/***/ },
/* 32 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Constructor_Validator = exports.checker = undefined;
	
	var _config = __webpack_require__(33);
	
	var _structure = __webpack_require__(9);
	
	var checker = exports.checker = {
	
	  create_checker: function create_checker(name, callback) {
	    Constructor_Validator.prototype.types[name] = {
	      validate: callback
	    };
	  },
	
	  check_condition: function check_condition(condition) {
	    return !condition;
	  },
	
	  create_result: function create_result(correction) {
	    var result = {
	      bool: true
	    };
	
	    if (typeof correction !== 'undefined') result.correction = correction;
	
	    return result;
	  },
	
	  create_error: function create_error(message, correction) {
	    var result = {
	      bool: false
	    };
	
	    if (typeof message !== 'undefined') result.message = message;
	
	    if (typeof correction !== 'undefined') result.correction = correction;
	
	    return result;
	  },
	
	  exist_in_db: function exist_in_db(name, value, callback, message) {
	    if (name && value) {
	      var post_data = {
	        __exist__: name,
	        value: value,
	        csrfmiddlewaretoken: _structure.data_controller.get('csrf_token')
	      };
	
	      $.post('', post_data).done(function (data) {
	        if (data.__exist__ !== 'undefined') if (data.__exist__ === 'true') callback(checker.create_error(message));else if (data.__exist__ === 'false') callback(checker.create_result());
	      }).fail(function () {
	        console.error('Something is wrong.');
	        callback(checker.create_error('Validator, don\' work. Please, refresh website.'));
	      });
	    }
	  }
	};
	
	var Constructor_Validator = exports.Constructor_Validator = function Constructor_Validator(form_name, form_type) {
	
	  var fields_of_form = void 0,
	      $form = $('form[data-name=' + form_name + ']');
	  this.types = Constructor_Validator.prototype.types;
	  this.config = _config.list_configs[form_type];
	
	  if (!this.config) console.error('Validation Error: Invalid form type of list configs.');
	
	  this.change_status_field = function (name, value) {
	    if (typeof fields_of_form[name] === 'boolean') {
	      if (typeof value === 'boolean') fields_of_form[name] = value;else console.error('Validation Error: Invalid value in the field ' + value + '.');
	    } else console.error('Validation Error: No manual for the field ' + name + '.');
	  };
	
	  this.check_list_field = function () {
	    for (var key in fields_of_form) {
	      if (fields_of_form.hasOwnProperty(key)) if (fields_of_form[key] === false) return false;
	    }return true;
	  };
	
	  var prepare_list_fields = function prepare_list_fields() {
	    var fields = $form.serializeArray(),
	        obj = {},
	        i = void 0,
	        length = fields.length;
	
	    for (i = 0; i < length; ++i) {
	      if ($form.find('*[name=' + fields[i].name + ']').hasClass('test')) obj[fields[i].name] = false;
	    }return obj;
	  };
	
	  fields_of_form = prepare_list_fields();
	
	  this.field = function (name, value, callback) {
	    if (name && value) {
	      var type = void 0,
	          _checker = void 0;
	
	      type = this.config[name];
	      _checker = this.types[type];
	
	      if (!_checker) {
	        console.error('Validation Error: No manual for the key ' + name + '.');
	        return false;
	      }
	
	      _checker.validate(value, callback);
	    } else if (value !== '') {
	      var result = checker.create_error('Incorrect value ' + name);
	      callback(result);
	    } else callback(checker.create_error());
	  };
	
	  this.hasErrors = function () {
	    return fields_of_form;
	  };
	};

/***/ },
/* 33 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	var list_configs = exports.list_configs = {};
	
	list_configs.register = {
	  new_username: 'length_3',
	  new_password: 'password',
	  new_email: 'email_not_in_db'
	};
	
	list_configs.login = {
	  email: 'email',
	  password: 'password'
	};
	
	list_configs.user_address = {
	  full_name: 'full_name',
	  address_line: 'no_empty',
	  city: 'proper_name',
	  region: 'proper_name',
	  postcode: 'no_empty',
	  country: 'proper_name'
	};
	
	list_configs.root_address = {
	  full_name: 'full_name',
	  address_line: 'no_empty',
	  city: 'proper_name',
	  region: 'proper_name',
	  postcode: 'no_empty',
	  country: 'proper_name',
	  email: 'email'
	};
	
	list_configs.forgot_password = {
	  email: 'email'
	};
	
	list_configs.email_contact = {
	  client: 'proper_name',
	  email: 'email',
	  message: 'no_empty'
	};

/***/ },
/* 34 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.define = undefined;
	
	var _views = __webpack_require__(35);
	
	var add_event_on_fields = function add_event_on_fields(auto_form_views) {
	  var settings = auto_form_views.models.settings,
	      $field = void 0;
	
	  settings.fields.each(function () {
	    $field = $(this);
	
	    if ($field.is(':checkbox')) $field.change(auto_form_views.send_checkbox);else if ($field.is(':text')) {
	      if ($field.hasClass('only_enter')) $field.keydown(auto_form_views.send_on_enter);else {
	        if ($field.hasClass('always')) $field.keyup(auto_form_views.send_if_number_only);
	
	        if ($field.hasClass('only_number_3')) $field.keydown(auto_form_views.try_press_number_max_3);
	
	        $field.change(auto_form_views.send_default).keydown(auto_form_views.send_on_enter);
	      }
	    } else $field.change(auto_form_views.send_default);
	  });
	},
	    do_nothing = function do_nothing(event) {
	  event.preventDefault();
	  return false;
	};
	
	var define = exports.define = function define($container) {
	  var $forms = $('form.auto_form, .auto_form form', $container);
	
	  $forms.each(function () {
	    var $form = $(this),
	        config = {
	      form: $form,
	      fields: $('.auto_field', $form)
	    },
	        auto_form_views = new _views.Auto_Form_Views(config);
	
	    $form.submit(do_nothing);
	    add_event_on_fields(auto_form_views);
	  });
	};

/***/ },
/* 35 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Auto_Form_Views = undefined;
	
	var _models = __webpack_require__(36);
	
	var Auto_Form_Views = exports.Auto_Form_Views = function Auto_Form_Views(config) {
	  var models = new _models.Auto_Form_Models(config),
	      that = this,
	      sent_http_request = setTimeout(function () {}, 0);
	
	  this.models = models;
	
	  var check_is_number = function check_is_number(event) {
	    var keycode = event.keyCode,
	        valid = keycode === 8 || keycode === 46 || keycode > 47 && keycode < 58 || keycode > 95 && keycode < 112;
	
	    return valid;
	  };
	
	  var check_is_not_number_or_functionaly = function check_is_not_number_or_functionaly(event) {
	    var keycode = event.keyCode,
	        valid = keycode === 32 || keycode === 13 || keycode > 64 && keycode < 91 || keycode > 185 && keycode < 193 || keycode > 218 && keycode < 223 || keycode == 16 || event.ctrlKey || event.shiftKey || keycode > 105 && keycode < 110 || keycode == 111;
	
	    return valid;
	  };
	
	  var check_is_not_functionaly = function check_is_not_functionaly(event) {
	    var keycode = event.keyCode,
	        valid = keycode > 47 && keycode < 58 || keycode === 32 || keycode === 13 || keycode > 64 && keycode < 91 || keycode > 95 && keycode < 112 || keycode > 185 && keycode < 193 || keycode > 218 && keycode < 223 || keycode == 16 || event.ctrlKey || event.shiftKey || keycode > 105 && keycode < 110 || keycode == 111;
	
	    return valid;
	  };
	
	  this.try_press_number_max_3 = function (event) {
	
	    if (check_is_not_number_or_functionaly(event)) {
	      event.preventDefault();
	    } else {
	      var length = $(this).val().length;
	      if (length > 2 && check_is_not_functionaly(event)) event.preventDefault();
	    }
	  };
	
	  this.send_if_number_only = function (event) {
	    if (check_is_number(event)) {
	      var $field = $(this),
	          name = $field.data('name'),
	          value = $field.val();
	
	      that.send_default(name, value);
	    }
	  };
	
	  var check_is_key_code_enter = function check_is_key_code_enter(event) {
	    return event.keyCode === 13;
	  };
	
	  this.send_checkbox = function () {
	    var $field = $(this),
	        post_data = {};
	
	    post_data['__' + models.settings.origin + '__'] = $field.data('name');
	    post_data['name'] = $field.attr('name');
	
	    if ($field.is(':checked')) post_data['action'] = 'append';else post_data['action'] = 'delete';
	
	    send(post_data);
	  };
	
	  this.send_default = function (name, value) {
	    var $field = void 0,
	        post_data = {};
	
	    if (name && value) {
	      post_data['__' + models.settings.origin + '__'] = name;
	      post_data['value'] = value;
	    } else {
	      $field = $(this);
	
	      post_data['__' + models.settings.origin + '__'] = $field.data('name');
	      post_data['value'] = $field.val();
	    }
	
	    send(post_data);
	  };
	
	  this.send_on_enter = function (event) {
	    if (check_is_key_code_enter(event)) {
	      event.preventDefault();
	      var $field = $(this),
	          post_data = {};
	
	      post_data['__' + models.settings.origin + '__'] = $field.data('name');
	      post_data['value'] = $field.val();
	
	      send(post_data);
	    }
	  };
	
	  var show_changes = function show_changes() {
	    var delay = void 0,
	        function_for_setTimeout = function function_for_setTimeout() {
	      if (models.get_state_response() && models.get_state_error() === false) {
	        APP.DATA.delay = delay;
	
	        if (models.settings.redirect) {
	          APP.DATA.redirect = models.settings.redirect;
	
	          APP.throw_event(EVENTS.redirect);
	        } else if (models.settings.reload) {
	          APP.throw_event(EVENTS.part['reload_' + models.settings.reload]);
	        }
	      } else if (models.get_state_error()) return false;else sent_http_request = setTimeout(function_for_setTimeout, 100);
	    };
	
	    if (typeof models.settings.delay !== 'undefined') delay = models.settings.delay;else delay = 0;
	
	    clearTimeout(sent_http_request);
	    sent_http_request = setTimeout(function_for_setTimeout, delay);
	  },
	      is_error = function is_error(status) {
	    return status !== 'success';
	  },
	      set_response = function set_response(JSON_response, status) {
	    if (is_error(status)) {
	      models.set_state_error(true);
	      models.set_state_response(false);
	      return false;
	    }
	
	    models.set_state_error(false);
	    models.set_state_response(true);
	  },
	      send = function send(post_data) {
	    models.set_state_response(false);
	    APP.http_request(models.settings.action, post_data, set_response);
	    show_changes();
	  };
	};

/***/ },
/* 36 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	var Auto_Form_Models = exports.Auto_Form_Models = function Auto_Form_Models(config) {
	  var that = this;
	
	  this.settings = {
	    form: undefined,
	    fields: undefined,
	
	    action: undefined,
	    origin: undefined,
	    redirect: undefined,
	    reload: undefined,
	    delay: undefined
	  };
	
	  var load_settings = function load_settings() {
	    if (typeof config !== 'undefined') {
	      if (typeof config.form !== 'undefined') {
	        that.settings.form = config.form;
	
	        var $form = that.settings.form;
	        that.settings.action = $form.attr('action');
	        that.settings.origin = $form.data('origin');
	        that.settings.redirect = $form.data('redirect');
	        that.settings.reload = $form.data('reload');
	        that.settings.delay = $form.data('delay');
	      }
	
	      if (typeof config.fields !== 'undefined') that.settings.fields = config.fields;
	    }
	  };
	
	  load_settings();
	
	  var state = {
	    response: false,
	    error: false
	  };
	
	  this.get_state_response = function () {
	    if (state.response) return true;else return false;
	  };
	
	  this.set_state_response = function (setter) {
	    if (setter) state.response = true;else state.response = false;
	  };
	
	  this.get_state_error = function () {
	    if (state.error) return true;else return false;
	  };
	
	  this.set_state_error = function (setter) {
	    if (setter) state.error = true;else state.error = false;
	  };
	};

/***/ },
/* 37 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	
	
	var change_fields = function change_fields(select_choice) {
	  var important_fields = $(select_choice).data('important_fields'),
	      fields_to_hide = $(select_choice).val();
	
	  var hidden_fields = function hidden_fields(list, type) {
	    var array = void 0,
	        array_length = void 0;
	
	    if (!list || typeof list !== 'string') return false;
	
	    array = list.split(' ');
	    array_length = array.length;
	
	    for (var i = 0; i < array_length; ++i) {
	      if (array[i]) if ($('#id_' + array[i]).length) $('#id_' + array[i]).attr('hidden', type);
	    }
	  };
	
	  hidden_fields(important_fields, false);
	  hidden_fields(fields_to_hide, true);
	},
	    change_form = function change_form(event) {
	  event.preventDefault();
	  event.stopPropagation();
	
	  var $select_choice = $(this),
	      $title_field = $('#id_title'),
	      $options = $select_choice.children('option'),
	      form_title = $title_field.val();
	
	  $options.each(function () {
	    if ($(this).is(':selected')) form_title = $(this).text();
	  });
	
	  $title_field.attr('value', form_title);
	
	  change_fields($select_choice);
	};
	
	var define = exports.define = function define($container) {
	  $('.selected_form-choice', $container).change(change_form);
	};

/***/ },
/* 38 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.define = undefined;
	
	var _views = __webpack_require__(39);
	
	var image_convert_views = _interopRequireWildcard(_views);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var define = exports.define = function define($container) {
	  var views = image_convert_views,
	      settings = views.models.settings,
	      $forms = $(settings.form, $container),
	      $file_fields = $(settings.input_file, $forms);
	
	  $file_fields.each(function (i, field) {
	    $(field).change(function () {
	      if (field.files[0]) {
	        var callback = new views.Callback_Functions(field);
	
	        views.get_base64(field.files[0], callback);
	      }
	    }).parent().children(settings.button_shell).click(function () {
	      $(field).click();
	    });
	  });
	};

/***/ },
/* 39 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Callback_Functions = exports.get_base64 = exports.settings = exports.models = undefined;
	
	var _models = __webpack_require__(40);
	
	var image_convert_models = _interopRequireWildcard(_models);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var models = exports.models = image_convert_models,
	    settings = exports.settings = models.settings,
	    get_base64 = exports.get_base64 = function get_base64(file, callback) {
		callback.loading();
	
		var reader = new FileReader();
		reader.readAsDataURL(file);
	
		reader.onload = function () {
			callback.done(file.name, reader.result);
		};
	
		reader.onerror = function (error) {
			callback.error(error);
		};
	},
	    Callback_Functions = exports.Callback_Functions = function Callback_Functions(field) {
		var $field = $(field),
		    $parent_field = $field.parent(),
		    $button_shell = $parent_field.children(settings.button_shell);
	
		this.loading = function () {
			$button_shell.html('Coverting...');
		};
	
		this.done = function (name, result) {
			var hidden_input_base64 = settings.input_hidden.start + field.name + settings.input_hidden.end_base64,
			    hidden_input_name = settings.input_hidden.start + field.name + settings.input_hidden.end_name;
	
			$(hidden_input_base64).val(result);
			$(hidden_input_name).val(name);
			setTimeout(function () {
				$button_shell.html('Is ready / change');
			}, 500);
		};
	
		this.error = function () {
			setTimeout(function () {
				$button_shell.html('Error / select again');
			}, 500);
		};
	};

/***/ },
/* 40 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var settings = exports.settings = {
		form: 'form',
		input_file: 'input[type=file]',
		button_shell: '.file_shell button',
		input_hidden: {
			start: 'input[name=',
			end_base64: '_base64]',
			end_name: '_name]'
		}
	};

/***/ },
/* 41 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Post_Button_Controllers = undefined;
	
	var _views = __webpack_require__(42);
	
	var Post_Button_Controllers = exports.Post_Button_Controllers = function Post_Button_Controllers(config) {
		if (typeof config === 'undefined' && typeof config.container === 'undefined') {
			console.error('Exeption error: invalid container.');
			return {};
		}
	
		var buttons_views = {},
		    manage_buttons = function manage_buttons(event) {
			event.preventDefault();
			event.stopPropagation();
	
			var button_name = $(this).data('name');
	
			if (buttons_views[button_name]) buttons_views[button_name].start();else console.error('Button "' + button_name + '" doesn\'t exsist');
		},
		    create_button_views = function create_button_views() {
			var button_name = $(this).data('name');
			config.button = this;
	
			config.button_name = button_name;
			config.button_action = $(this).data('action');
			config.button_value = $(this).data('value');
			config.button_other_1 = $(this).data('other_1');
			config.button_other_2 = $(this).data('other_2');
			config.button_other_3 = $(this).data('other_3');
			config.button_reload = $(this).data('reload');
			config.button_redirect = $(this).data('redirect');
			config.button_event = $(this).data('event');
			config.button_url = $(this).data('url');
	
			if ($(this).hasClass('is-text_icon')) config.button_html = $(this).find('.button-text').html();else config.button_html = $(this).html();
	
			buttons_views[button_name] = new _views.Post_Button_Views(config);
		};
	
		this.define = function () {
			var $post_buttons = $('.post_button', config.container);
	
			$post_buttons.each(create_button_views);
	
			$post_buttons.click(manage_buttons);
		};
	};

/***/ },
/* 42 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Post_Button_Views = undefined;
	
	var _models = __webpack_require__(43);
	
	var _utilities = __webpack_require__(27);
	
	var utilities = _interopRequireWildcard(_utilities);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var Post_Button_Views = exports.Post_Button_Views = function Post_Button_Views(config) {
		var models = new _models.Post_Button_Models(config),
		    set_text = {
	
			insert: function insert(text) {
				var $button = $(models.settings.button);
	
				if (set_text.if_is_not_text()) return false;
	
				if ($button.hasClass('is-text_icon')) $button.find('.button-text').html(text);else $button.html(text);
			},
	
			if_is_not_text: function if_is_not_text() {
				return $(models.settings.button).hasClass('is-icon');
			},
	
			sending: function sending() {
				if (set_text.if_is_not_text()) return false;
	
				clearTimeout(set_text.set_waiting);
				clearTimeout(set_text.set_standard);
	
				set_text.insert(models.settings.text_sending);
			},
	
			set_waiting: undefined,
			waiting: function waiting() {
				if (set_text.if_is_not_text()) return false;
	
				set_text.set_waiting = setTimeout(function () {
					set_text.insert(models.settings.text_waiting);
				}, models.settings.delay_text_waiting);
			},
	
			done: function done() {
				if (set_text.if_is_not_text()) return false;
	
				clearTimeout(set_text.set_waiting);
				set_text.insert(models.settings.text_done);
			},
	
			set_standard: undefined,
			standard: function standard() {
				if (set_text.if_is_not_text()) return false;
	
				set_text.set_standard = setTimeout(function () {
					set_text.insert(models.settings.text_standard);
				}, models.settings.delay_text_standard);
			},
	
			error: function error() {
				if (set_text.if_is_not_text()) return false;
	
				clearTimeout(set_text.set_waiting);
				clearTimeout(set_text.set_standard);
	
				set_text.insert(models.settings.text_error);
			}
		},
		    start_loading = function start_loading() {
			models.state.is_loading = true;
			set_text.sending();
			set_text.waiting();
		},
		    is_error = function is_error(JSON_response, status) {
			if (status !== 'success') {
				set_text.error();
				return true;
			}
	
			var response = JSON.parse(JSON_response);
	
			if (response.__button__ !== 'true') {
				set_text.error();
				return true;
			}
	
			return false;
		},
		    end_loading = function end_loading(JSON_response, status) {
			var events = void 0;
	
			models.state.is_loading = false;
	
			if (is_error(JSON_response, status)) return false;
	
			set_text.done();
	
			events = {
				reload: models.settings.button_reload,
				redirect: models.settings.button_redirect,
				events: models.settings.button_event,
				delay: models.settings.button_delay
			};
	
			utilities.reload_plugins(events);
			utilities.redirect_ground(events);
			utilities.launch_event(events);
	
			set_text.standard();
		};
	
		this.start = function () {
			if (models.is_loading()) return false;
	
			start_loading();
			models.send_post(end_loading);
		};
	
		this.models = models;
	};

/***/ },
/* 43 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var Post_Button_Models = exports.Post_Button_Models = function Post_Button_Models(config) {
		var that = this,
		    dictionary = APP.dictionary;
	
		this.settings = {
			container: undefined,
			button: undefined,
	
			button_name: undefined,
			button_action: undefined,
			button_value: undefined,
			button_other_1: undefined,
			button_other_2: undefined,
			button_other_3: undefined,
			button_reload: undefined,
			button_redirect: undefined,
			button_event: undefined,
			button_url: undefined,
	
			callback: undefined,
	
			text_sending: dictionary.get_word('Sending...'),
			text_waiting: dictionary.get_word('Waiting...'),
			text_done: dictionary.get_word("It's done!"),
			text_error: dictionary.get_word('Error / Resend'),
			text_standard: undefined,
	
			delay_text_waiting: 500,
			delay_text_standard: 1000
		};
	
		var load_settings = function load_settings() {
			if (typeof config !== 'undefined') {
				APP.add_if_isset(config, that.settings, 'container');
	
				APP.add_if_isset(config, that.settings, 'callback');
	
				APP.add_if_isset(config, that.settings, 'button');
	
				APP.add_if_isset(config, that.settings, 'button_name');
				APP.add_if_isset(config, that.settings, 'button_action');
				APP.add_if_isset(config, that.settings, 'button_value');
				APP.add_if_isset(config, that.settings, 'button_other_1');
				APP.add_if_isset(config, that.settings, 'button_other_2');
				APP.add_if_isset(config, that.settings, 'button_other_3');
				APP.add_if_isset(config, that.settings, 'button_reload');
				APP.add_if_isset(config, that.settings, 'button_redirect');
				APP.add_if_isset(config, that.settings, 'button_event');
				APP.add_if_isset(config, that.settings, 'button_url');
	
				APP.add_if_isset(config, that.settings, 'button_html', 'text_standard');
			}
		};
	
		load_settings();
	
		this.state = {
			is_loading: false
		};
	
		this.is_loading = function () {
			return that.state.is_loading;
		};
	
		var prepare_post_data = function prepare_post_data() {
			var obj = { __button__: that.settings.button_action },
			    value = that.settings.button_value;
	
			if (value) obj.value = value;
	
			obj.other_1 = that.settings.button_other_1 || '';
			obj.other_2 = that.settings.button_other_2 || '';
			obj.other_3 = that.settings.button_other_3 || '';
	
			return obj;
		};
	
		this.send_post = function (callback) {
			setTimeout(function () {
				var url = that.settings.button_url,
				    post_data = prepare_post_data();
	
				APP.http_request(url, post_data, callback);
			}, 200);
		};
	};

/***/ },
/* 44 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.reload = exports.open_or_close = exports.plugin_close = exports.plugin_open = exports.get_content = exports.define = undefined;
	
	var _part = __webpack_require__(13);
	
	var _controllers = __webpack_require__(22);
	
	var _controllers2 = __webpack_require__(25);
	
	var _controllers3 = __webpack_require__(41);
	
	var _controllers4 = __webpack_require__(45);
	
	var container = '.cart',
	    config_loader = {
		name: 'cart',
		container: container,
		load_meta_tags: true
	},
	    cart_loader = new _part.Part_Loader_Part(config_loader),
	    cart_motion_controllers = new _controllers.Plugins_Motion_Controllers({
		container: '#CART',
		content: container,
		open: 'left',
		can_open_by: 'width',
		can_open_from: 0,
		duration_open: 200,
		duration_close: 200
	}),
	    post_button_controllers = new _controllers3.Post_Button_Controllers({
		container: '#CART > ' + container
	}),
	    event_button_controllers = new _controllers4.Event_Button_Controllers({
		container: '#CART'
	}),
	    cart_form_controllers = new _controllers2.Form_Controllers(config_loader),
	    manage_key = function manage_key(event) {
		if (event.keyCode === 27) cart_motion_controllers.plugin_close();
	
		if (event.ctrlKey && event.shiftKey && event.keyCode === 88) {
			event.preventDefault();
			if (cart_motion_controllers.is_open()) cart_motion_controllers.plugin_close();else cart_motion_controllers.plugin_open();
		}
	};
	
	var define = exports.define = function define() {
		APP.add_own_event('cart_open', cart_motion_controllers.plugin_open);
		APP.add_own_event('cart_close', cart_motion_controllers.plugin_close);
		APP.add_own_event('cart_open_or_close', open_or_close);
	
		$('body').keydown(manage_key);
	
		cart_form_controllers.define();
		cart_motion_controllers.define();
		post_button_controllers.define();
		event_button_controllers.define();
	},
	    get_content = exports.get_content = function get_content() {
		cart_loader.define();
		cart_loader.load_content();
		cart_motion_controllers.set_start_position();
	},
	    plugin_open = exports.plugin_open = cart_motion_controllers.plugin_open,
	    plugin_close = exports.plugin_close = cart_motion_controllers.plugin_close,
	    open_or_close = exports.open_or_close = function open_or_close() {
		APP.throw_event(EVENTS.part.close_navigation);
	
		if (cart_motion_controllers.is_open()) plugin_close();else plugin_open();
	},
	    reload = exports.reload = function reload() {
		cart_motion_controllers.plugin_open();
	};

/***/ },
/* 45 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Event_Button_Controllers = undefined;
	
	var _views = __webpack_require__(46);
	
	var Event_Button_Controllers = exports.Event_Button_Controllers = function Event_Button_Controllers(config) {
	  if (typeof config === 'undefined' && typeof config.container === 'undefined') {
	    console.error('Exeption error: invalid container.');
	    return {};
	  }
	
	  var buttons_views = {},
	      manage_buttons = function manage_buttons(event) {
	    var button_name = $(this).data('name'),
	        button_prevent = $(this).data('prevent');
	
	    if (button_prevent !== 'false') event.preventDefault();
	
	    if (buttons_views[button_name]) buttons_views[button_name].start();else console.error('Button "' + button_name + '" doesn\'t exsist');
	  },
	      create_button_views = function create_button_views() {
	    var button_name = $(this).data('name');
	    config.button = this;
	
	    config.button_name = button_name;
	    config.button_reload = $(this).data('reload');
	    config.button_redirect = $(this).data('redirect');
	    config.button_event = $(this).data('event');
	    config.button_delay = $(this).data('delay');
	
	    buttons_views[button_name] = new _views.Event_Button_Views(config);
	  };
	
	  this.define = function () {
	    var $buttons = $('.event_button', config.container);
	
	    $buttons.each(create_button_views);
	
	    $buttons.click(manage_buttons);
	  };
	};

/***/ },
/* 46 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Event_Button_Views = undefined;
	
	var _models = __webpack_require__(47);
	
	var _utilities = __webpack_require__(27);
	
	var utilities = _interopRequireWildcard(_utilities);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var Event_Button_Views = exports.Event_Button_Views = function Event_Button_Views(config) {
	
		var models = new _models.Event_Button_Models(config);
	
		this.models = models;
	
		this.start = function () {
			var events = {
				reload: models.settings.button_reload,
				redirect: models.settings.button_redirect,
				events: models.settings.button_event,
				delay: models.settings.button_delay
			};
	
			utilities.reload_plugins(events);
			utilities.redirect_ground(events);
			utilities.launch_event(events);
		};
	};

/***/ },
/* 47 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var Event_Button_Models = exports.Event_Button_Models = function Event_Button_Models(config) {
		var that = this;
	
		this.settings = {
			container: undefined,
			button: undefined,
	
			button_name: undefined,
			button_reload: undefined,
			button_redirect: undefined,
			button_event: undefined,
			button_delay: undefined
		};
	
		(function load_settings() {
			if (typeof config !== 'undefined') {
				APP.add_if_isset(config, that.settings, 'container');
	
				APP.add_if_isset(config, that.settings, 'button');
	
				APP.add_if_isset(config, that.settings, 'button_name');
				APP.add_if_isset(config, that.settings, 'button_reload');
				APP.add_if_isset(config, that.settings, 'button_redirect');
				APP.add_if_isset(config, that.settings, 'button_event');
				APP.add_if_isset(config, that.settings, 'button_delay');
			}
		})();
	};

/***/ },
/* 48 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.plugin_open = exports.get_content = exports.define = undefined;
	
	var _part = __webpack_require__(13);
	
	var _controllers = __webpack_require__(22);
	
	var _controllers2 = __webpack_require__(45);
	
	var navigation_loader = new _part.Part_Loader_Part({
		name: 'navigation',
		url: '/navigation/',
	
		container: '#NAVIGATION .navigation',
	
		auto_first_loading: true
	}),
	    navigation_motion_controllers = new _controllers.Plugins_Motion_Controllers({
		container: '#NAVIGATION',
		content: '.navigation',
		open: 'down',
	
		can_open_by: 'width',
		can_open_to: 675,
	
		duration_open: 300,
		duration_close: 150
	}),
	    event_button_controllers = new _controllers2.Event_Button_Controllers({
		container: '#NAVIGATION'
	});
	
	var define = exports.define = function define() {
		APP.add_own_event('navigation_close', navigation_motion_controllers.plugin_close);
		APP.add_own_event('navigation_open', navigation_motion_controllers.plugin_open);
	
		navigation_motion_controllers.define();
		event_button_controllers.define();
	},
	    get_content = exports.get_content = function get_content() {
		navigation_loader.define();
		navigation_loader.load_content();
	
		navigation_motion_controllers.set_start_position();
	},
	    plugin_open = exports.plugin_open = function plugin_open() {
		navigation_motion_controllers.plugin_open();
	};

/***/ },
/* 49 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.get_content = exports.define = undefined;
	
	var _part = __webpack_require__(13);
	
	var _controllers = __webpack_require__(45);
	
	var header_loader = new _part.Part_Loader_Part({
		name: 'header',
		url: '/navigation/',
	
		container: '#HEADER > .header',
	
		auto_first_loading: true
	}),
	    event_button_controllers = new _controllers.Event_Button_Controllers({
		container: '#HEADER'
	});
	
	var define = exports.define = function define() {
		event_button_controllers.define();
	},
	    get_content = exports.get_content = function get_content() {
		header_loader.define();
		header_loader.load_content();
	};

/***/ },
/* 50 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define = undefined;
	
	var _controller = __webpack_require__(51);
	
	var _controller2 = __webpack_require__(54);
	
	var config = {
		name: 'dialog',
		html_id: '#DIALOG',
		container: '.dialog',
		internal_button: '.dialog_send',
		external_button: '.dialog_button',
		form: '.dialog_form',
	
		duration_show: 0,
		duration_hide: 0
	},
	    designer = new _controller.Dialog_Designer_Controller(config),
	    loader = new _controller2.Dialog_Loader_Controller(config),
	    reload = function reload() {
		var loading = loader.reload_content(this);
		designer.set_loading().then(function () {
			loading.then(designer.unset_loading);
		});
	},
	    close = function close() {
		designer.close().then(function () {
			loader.define();
		});
	},
	    open = function open() {
		var loading = loader.get_content(this);
	
		designer.open().then(function () {
			loading.then(loader.define);
		});
	};
	
	var define = exports.define = function define() {
		designer.define();
	
		$(config.external_button).click(open);
		APP.add_own_event('dialog_close', close);
	};

/***/ },
/* 51 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Designer_Controller = Dialog_Designer_Controller;
	
	var _standard = __webpack_require__(52);
	
	var _view = __webpack_require__(53);
	
	function Dialog_Designer_Controller(config) {
		var _this = this;
	
		var view = new _view.Dialog_Designer_View(config),
		    cancel_event = function cancel_event(event) {
			event.stopPropagation();
		},
		    close_with_cancel_event = function close_with_cancel_event(event) {
			cancel_event(event);
			_this.close();
		},
		    close_with_delay = function close_with_delay() {
			return new Promise(function (resolve) {
				var delay = 0;
	
				if (APP.DATA.delay >= 0) delay = APP.DATA.delay;else delay = 2000;
	
				(0, _standard.timeout_promise)(delay).then(function () {
					_this.close().then(resolve);
				});
			});
		};
	
		this.set_loading = function () {
			return view.dim();
		};
	
		this.unset_loading = function () {
			return view.lighten();
		};
	
		this.close = function () {
			return view.hide();
		};
	
		this.open = function () {
			return view.show();
		};
	
		this.define = function () {
			$(view.selector.html_id).click(close_with_cancel_event);
			$(view.selector.window).click(cancel_event);
		};
	}

/***/ },
/* 52 */
/***/ function(module, exports) {

	"use strict";
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var timeout_promise = exports.timeout_promise = function timeout_promise(delay) {
		return new Promise(function (resolve, reject) {
			setTimeout(function () {
				reject();
			}, delay);
		});
	};

/***/ },
/* 53 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Designer_View = Dialog_Designer_View;
	function Dialog_Designer_View(config) {
		this.selector = {
			html_id: config.html_id,
			window: config.container,
			header: config.container + '-header',
			content: config.container + '-content'
		};
	
		this.show = function () {
			var _this = this;
	
			return new Promise(function (resolve) {
				$(_this.selector.html_id).css('opacity', '').fadeIn(200, resolve);
			});
		};
	
		this.hide = function () {
			var _this2 = this;
	
			return new Promise(function (resolve) {
				$(_this2.selector.html_id).animate({ opacity: 0 }, 200, function () {
					$(_this2.selector.html_id).hide();
					resolve();
				});
			});
		};
	
		this.dim = function () {
			var _this3 = this;
	
			return new Promise(function (resolve) {
				$(_this3.selector.html_id).animate({ opacity: .8 }, 200, resolve);
			});
		};
	
		this.lighten = function () {
			var _this4 = this;
	
			return new Promise(function (resolve) {
				$(_this4.selector.html_id).animate({ opacity: 1 }, 300, resolve);
			});
		};
	}

/***/ },
/* 54 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Loader_Controller = Dialog_Loader_Controller;
	
	var _controllers = __webpack_require__(25);
	
	var _controllers2 = __webpack_require__(41);
	
	var _controllers3 = __webpack_require__(45);
	
	var _controllers4 = __webpack_require__(55);
	
	var _view = __webpack_require__(58);
	
	function Dialog_Loader_Controller(config) {
		var config_loader = {
			name: config.name,
			container: config.container
		},
		    view = new _view.Dialog_Loader_View(config_loader),
		    form_controller = new _controllers.Form_Controllers(config_loader),
		    post_button_controller = new _controllers2.Post_Button_Controllers(config_loader),
		    event_button_controller = new _controllers3.Event_Button_Controllers(config_loader),
		    little_form_controller = new _controllers4.Little_Form_Controllers(config_loader),
		    send_form = function send_form() {
			$(config.form, config.container).submit();
		};
	
		this.reload_content = function () {
			return view.send_request();
		};
	
		this.get_content = function (button) {
			return new Promise(function (resolve) {
				view.collect_data(button);
	
				view.send_request().then(resolve);
			});
		};
	
		this.set_loading = function () {};
	
		this.define = function () {
			form_controller.define();
			post_button_controller.define();
			event_button_controller.define();
			little_form_controller.define();
			$(config.internal_button, config.container).click(send_form);
		};
	}

/***/ },
/* 55 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Little_Form_Controllers = undefined;
	
	var _views = __webpack_require__(56);
	
	var Little_Form_Controllers = exports.Little_Form_Controllers = function Little_Form_Controllers(form_config) {
	  if (typeof form_config === 'undefined' && typeof form_config.container === 'undefined') {
	    console.error('Exeption error: invalid container.');
	    return {};
	  }
	
	  var little_form_views = {},
	      manage_form = function manage_form(event) {
	    event.preventDefault();
	    event.stopPropagation();
	
	    var form_name = $(this).parent().find('input').data('name'),
	        value = $(this).parent().find('input').val();
	
	    if (little_form_views[form_name]) little_form_views[form_name].start(value);else console.error('Form "' + form_name + '" doesn\'t exsist');
	  },
	      create_form_views = function create_form_views() {
	    form_config.this = this;
	
	    form_config.action = $(this).data('action');
	    form_config.origin = $(this).data('origin');
	    form_config.name = $(this).find('input').data('name');
	    form_config.value = $(this).find('input').val();
	
	    form_config.reload = $(this).data('reload');
	    form_config.redirect = $(this).data('redirect');
	    form_config.event = $(this).data('event');
	
	    little_form_views[form_config.name] = new _views.Little_Form_Views(form_config);
	  };
	
	  this.define = function () {
	    var $form = $('.little_form', form_config.container);
	
	    $form.each(create_form_views);
	
	    $form.find('button').click(manage_form);
	  };
	};

/***/ },
/* 56 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Little_Form_Views = undefined;
	
	var _models = __webpack_require__(57);
	
	var Little_Form_Views = exports.Little_Form_Views = function Little_Form_Views(form_config) {
	  var models = new _models.Little_Form_Models(form_config);
	
	  this.models = models;
	
	  var reload_plugins = function reload_plugins() {
	    var plugins = models.settings.reload,
	        plugins_array = void 0,
	        array_length = void 0;
	
	    if (!plugins || typeof plugins !== 'string') return false;
	
	    plugins_array = plugins.split(' ');
	    array_length = plugins_array.length;
	
	    for (var i = 0; i < array_length; ++i) {
	      if (plugins_array[i]) {
	        APP.DATA.delay = 0;
	        APP.throw_event(EVENTS.part['reload_' + plugins_array[i]]);
	      }
	    }
	  },
	      redirect_ground = function redirect_ground() {
	    var url = models.settings.redirect;
	
	    if (!url || typeof url !== 'string') return false;
	
	    APP.DATA.redirect = url;
	    APP.DATA.delay = 100;
	    APP.throw_event(EVENTS.redirect);
	  },
	      launch_event = function launch_event() {
	    var event = models.settings.event,
	        split_event = void 0,
	        ready_event = EVENTS;
	
	    if (!event || typeof event !== 'string') return false;
	
	    split_event = event.split('.');
	
	    for (var i = 0; split_event.length > i; ++i) {
	      ready_event = ready_event[split_event[i]];
	    }if (ready_event.constructor === Event) {
	      APP.DATA.delay = 100;
	      APP.throw_event(ready_event);
	    }
	  },
	      end_loading = function end_loading(JSON_response, status) {
	    models.set_state_loading(false);
	
	    if (models.is_error(JSON_response, status)) {
	      models.set_state_error(true);
	      console.error('Little form error: response is wrong.');
	      return false;
	    }
	
	    reload_plugins();
	    redirect_ground();
	    launch_event();
	  };
	
	  this.start = function (value) {
	    if (models.get_state_loading()) return false;
	
	    models.set_state_loading(true);
	
	    models.settings.value = value;
	    models.send_post(end_loading);
	  };
	};

/***/ },
/* 57 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	var Little_Form_Models = exports.Little_Form_Models = function Little_Form_Models(form_config) {
	  var that = this;
	
	  this.settings = {
	    container: undefined,
	    this: undefined,
	
	    action: undefined,
	    origin: undefined,
	    name: undefined,
	    value: undefined,
	
	    reload: undefined,
	    redirect: undefined,
	    event: undefined
	  };
	
	  (function load_settings() {
	    APP.add_if_isset(form_config, that.settings, 'container');
	    APP.add_if_isset(form_config, that.settings, 'this');
	
	    APP.add_if_isset(form_config, that.settings, 'action');
	    APP.add_if_isset(form_config, that.settings, 'origin');
	    APP.add_if_isset(form_config, that.settings, 'name');
	    APP.add_if_isset(form_config, that.settings, 'value');
	
	    APP.add_if_isset(form_config, that.settings, 'reload');
	    APP.add_if_isset(form_config, that.settings, 'redirect');
	    APP.add_if_isset(form_config, that.settings, 'event');
	  })();
	
	  var state = {
	    loading: false,
	    error: false
	  };
	
	  this.get_state_loading = function () {
	    if (state.response) return true;else return false;
	  };
	
	  this.set_state_loading = function (setter) {
	    if (setter) state.response = true;else state.response = false;
	  };
	
	  this.get_state_error = function () {
	    if (state.error) return true;else return false;
	  };
	
	  this.set_state_error = function (setter) {
	    if (setter) state.error = true;else state.error = false;
	  };
	
	  var prepare_post_data = function prepare_post_data(name, value) {
	    var post_data = {};
	
	    if (that.settings.origin && typeof that.settings.origin === 'string') post_data['__' + that.settings.origin + '__'] = name;
	
	    if (value) post_data.value = value;else post_data.value = '';
	
	    return post_data;
	  };
	
	  this.is_error = function (JSON_response, status) {
	    var response = JSON.parse(JSON_response);
	
	    if (status !== 'success') return true;
	
	    if (response['__' + that.settings.origin + '__'] !== 'true') return true;
	
	    return false;
	  };
	
	  this.send_post = function (callback) {
	    setTimeout(function () {
	      var name = that.settings.name,
	          action = that.settings.action,
	          value = that.settings.value,
	          post_data = prepare_post_data(name, value);
	
	      APP.http_request(action, post_data, callback);
	    }, 200);
	  };
	};

/***/ },
/* 58 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Loader_View = Dialog_Loader_View;
	
	var _model = __webpack_require__(59);
	
	function Dialog_Loader_View(config) {
		var model = new _model.Dialog_Loader_Model(config);
	
		this.collect_data = function (button) {
			var $button = $(button);
	
			model.variable.post_data = {
				dialog_type: $button.data('type'),
				dialog_name: $button.data('name'),
				dialog_value: $button.data('value'),
				dialog_other_1: $button.data('other_1'),
				dialog_other_2: $button.data('other_2'),
				dialog_other_3: $button.data('other_3'),
	
				additional_name: $button.data('dialog-name'),
				additional_action: $button.data('dialog-action'),
				additional_value: $button.data('dialog-value'),
				additional_reload: $button.data('dialog-reload'),
				additional_redirect: $button.data('dialog-redirect'),
				additional_event: $button.data('dialog-event'),
				additional_url: $button.data('dialog-url'),
	
				additional_other_1: $button.data('dialog-other_1'),
				additional_other_2: $button.data('dialog-other_2'),
				additional_other_3: $button.data('dialog-other_3')
			};
		};
	
		this.send_request = function () {
			model.prepare_post_data();
	
			return model.send_request();
		};
	}

/***/ },
/* 59 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Loader_Model = Dialog_Loader_Model;
	
	var _dialog = __webpack_require__(60);
	
	function Dialog_Loader_Model(config) {
	
		var part_dialog_loader = new _dialog.Part_Loader_Dialog(config);
	
		this.variable = {
			post_data: undefined,
			response: undefined
		};
	
		this.prepare_post_data = function () {
			var new_post_data = {},
			    post_data = this.variable.post_data;
	
			for (var data in post_data) {
				if (post_data.hasOwnProperty(data)) new_post_data[data] = post_data[data] || '';
			}new_post_data.__content__ = 'dialog';
	
			this.variable.post_data = new_post_data;
		};
	
		this.send_request = function () {
			console.log(this.variable.post_data);
			return part_dialog_loader.load_content(undefined, this.variable.post_data);
		};
	}

/***/ },
/* 60 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Part_Loader_Dialog = Part_Loader_Dialog;
	
	var _dialog = __webpack_require__(61);
	
	var _controller = __webpack_require__(17);
	
	function Part_Loader_Dialog(config) {
		_controller.Part_Loader.call(this, config);
	}
	
	Part_Loader_Dialog.prototype = Object.create(_controller.Part_Loader.prototype);
	
	Part_Loader_Dialog.prototype.send_request = function (actually_url) {
		var post_data = this.variables.post_data,
		    request_manager = new _dialog.Request_Manager_Dialog();
	
		this.response = request_manager.send(actually_url, post_data);
	};
	
	Part_Loader_Dialog.prototype.close_dialog_if_json = function (response, status) {
		if (status !== 'success') return false;
	
		if (response === '{"__form__": "true"}') {
			APP.DATA.delay = 0;
			APP.throw_event(EVENTS.part.close_dialog);
			return true;
		}
	
		return false;
	};
	
	Part_Loader_Dialog.prototype.load_content = function (url, post_data) {
		var _this = this;
	
		return new Promise(function (resolve) {
			_this.variables.url = url;
	
			_this.prepare_content_to_change(url, post_data);
	
			_this.send_request(url);
	
			_this.hide_content().then(function () {
				_this.receive_response().then(function (data) {
					if (_this.close_dialog_if_json(data)) return false;
	
					_this.prepare_content_to_show(data);
	
					_this.show_content().then(resolve);
				});
			});
		});
	};

/***/ },
/* 61 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Request_Manager_Dialog = Request_Manager_Dialog;
	
	var _init = __webpack_require__(16);
	
	function Request_Manager_Dialog() {
	  _init.Request_Manager.call(this);
	}
	
	Request_Manager_Dialog.prototype = Object.create(_init.Request_Manager.prototype);

/***/ },
/* 62 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.get_content = exports.define = undefined;
	
	var _part = __webpack_require__(13);
	
	var _controllers = __webpack_require__(25);
	
	var _controllers2 = __webpack_require__(41);
	
	var _controllers3 = __webpack_require__(45);
	
	var container = '.ground',
	    config_loader = {
		name: 'ground',
		container: container,
		load_meta_tags: true
	},
	    ground_loader = new _part.Part_Loader_Part(config_loader),
	    post_button_controllers = new _controllers2.Post_Button_Controllers({
		container: container
	}),
	    event_button_controllers = new _controllers3.Event_Button_Controllers({
		container: container
	}),
	    ground_form_controllers = new _controllers.Form_Controllers(config_loader);
	
	var change_url = function change_url(url) {
		history.pushState('', url, url);
	},
	    go_to_link = function go_to_link(event) {
		var url = $(this).attr('href'),
		    protocol = url.substring(0, 4);
	
		if (protocol !== 'http') if (event.which === 1) {
			event.preventDefault();
			APP.throw_event(EVENTS.part.close);
	
			change_url(url);
	
			ground_loader.load_simple_content(url);
		}
	},
	    redirect = function redirect(event) {
		change_url(APP.DATA.redirect);
		ground_loader.redirect(event);
	},
	    back_url = function back_url() {
		event.preventDefault();
		ground_loader.load();
	},
	    change_height_content = function change_height_content() {
		var $container = $(container),
		    height = {
			window: $('#CONTAINTER').innerHeight(),
			header: $('#HEADER').outerHeight(),
			ground_top: $container.position().top
		},
		    height_container = height.window - height.header - height.ground_top;
	
		$container.height(height_container);
		change_height_start_banner($container, height_container);
	},
	    change_height_start_banner = function change_height_start_banner($container, height_container) {
		var width_website = $('#CONTAINTER').innerWidth(),
		    height_start_banner = 0;
	
		if (height_container > 768) height_start_banner = height_container - 386;
	
		if (height_start_banner === 0 || width_website < 1000) {
			$('.ground-block.start .block-content-image', $container).hide();
			$('.ground-block.start .block-content-recommended-title', $container).show();
		} else {
			$('.ground-block.start .block-content-image', $container).show().height(height_start_banner);
			$('.ground-block.start .block-content-recommended-title', $container).hide();
		}
	},
	    change_to_long_or_short = function change_to_long_or_short(event) {
		var $element = $(this).parents('.change_length');
		event.stopPropagation();
	
		if ($element.hasClass('is-long')) $element.removeClass('is-long');else $element.addClass('is-long');
	},
	    change_to_long = function change_to_long(event) {
		event.stopPropagation();
	
		$(this).addClass('is-long');
	};
	
	var define = exports.define = function define() {
		change_height_content();
	
		$('a').click(go_to_link);
		APP.add_own_event('redirect', redirect);
		APP.add_own_event('popstate', back_url);
		$(window).resize(change_height_content);
	
		var $container = $(container);
	
		$('.change_length', $container).click(change_to_long);
		$('.change_length .change_length-button', $container).click(change_to_long_or_short);
	
		ground_form_controllers.define();
		post_button_controllers.define();
		event_button_controllers.define();
	},
	    get_content = exports.get_content = function get_content() {
		ground_loader.define();
		ground_loader.load_content();
	};

/***/ }
/******/ ]);
//# sourceMappingURL=bundle.js.map
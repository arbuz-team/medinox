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
	
	var _controllers = __webpack_require__(6);
	
	var page_controller = new _controllers.Page_Controller();
	
	window.APP.add_own_event('load', function () {
	  page_controller.start();
	});

/***/ },
/* 6 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Page_Controller = Page_Controller;
	
	__webpack_require__(7);
	
	__webpack_require__(9);
	
	var _controller = __webpack_require__(11);
	
	var _controller2 = __webpack_require__(70);
	
	var _controller3 = __webpack_require__(71);
	
	var _controller4 = __webpack_require__(35);
	
	var _controller5 = __webpack_require__(72);
	
	var _controller6 = __webpack_require__(32);
	
	var _block = __webpack_require__(13);
	
	function Page_Controller() {
	
		if (_typeof(Page_Controller.instance) === 'object') return Page_Controller.instance;
	
		var searcher_controller = new _controller.Search_Controller(),
		    cart_controller = new _controller2.Cart_Controller(),
		    menu_mobile_controller = new _controller3.Menu_Mobile_Controller(),
		    menu_controller = new _controller4.Menu_Controller(),
		    dialog_controller = new _controller5.Dialog_Controller(),
		    ground_controller = new _controller6.Ground_Controller(),
		    reload_sign_in = function reload_sign_in(permissions) {
			return function () {
				var request_manager = new _block.Request_Manager_Block(),
				    delay = APP.DATA.delay,
				    reload = function reload() {
					menu_mobile_controller.get_content();
					menu_controller.get_content();
	
					if (permissions === 'root') searcher_controller.get_content();
	
					if (permissions === 'user') cart_controller.get_content();
	
					request_manager.send_list();
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
		    redirect_website = function redirect_website(event) {
			var args = event.detail;
	
			if (args.url) window.location = args.url;
		},
		    define = function define() {
			var $textarea = $('textarea');
	
			$('*').off();
	
			window.autosize.destroy($textarea);
			window.autosize($textarea);
			searcher_controller.define();
			cart_controller.define();
			menu_mobile_controller.define();
			menu_controller.define();
			dialog_controller.define();
			ground_controller.define();
		};
	
		APP.add_own_event('define', define);
		APP.add_own_event('reload_website', reload_website);
		APP.add_own_event('redirect_website', redirect_website);
		APP.add_own_event('reload_user_sign_in', reload_sign_in('user'));
		APP.add_own_event('reload_root_sign_in', reload_sign_in('root'));
	
		this.get_height = function () {
			return $('#CONTAINER').innerHeight();
		};
	
		this.start = function () {
			define();
			var request_manager = new _block.Request_Manager_Block();
	
			searcher_controller.get_content();
			cart_controller.get_content();
			menu_mobile_controller.get_content();
			menu_controller.get_content();
			ground_controller.get_content();
	
			request_manager.send_list();
		};
	}

/***/ },
/* 7 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _base = __webpack_require__(8);
	
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
	
	$.prototype.serialize_object = function () {
		var fields = $(this).serializeArray(),
		    form_object = {};
	
		$.each(fields, function (i, field) {
			form_object[field.name] = field.value;
		});
	
		return form_object;
	};
	
	APP.add_if_isset = function (from, to, from_what, to_what) {
		if (typeof from[from_what] !== 'undefined') if (from_what && to_what) to[to_what] = from[from_what];else if (from_what) to[from_what] = from[from_what];
	};

/***/ },
/* 8 */
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
	};

/***/ },
/* 9 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _event = __webpack_require__(10);
	
	window.EVENTS = {
		send_request: new Event('send_request'),
		define: new Event('define'),
		redirect: new Event('redirect'),
		redirect_website: (0, _event.event_creator)('redirect_website'),
		reload_website: new Event('reload_website'),
	
		part: {
			open_cart: new Event('cart_open'),
			open_menu_mobile: new Event('menu_mobile_open'),
			open_searcher: new Event('searcher_open'),
	
			open_or_close_cart: new Event('cart_open_or_close'),
	
			close: new Event('part_close'),
			close_cart: new Event('cart_close'),
			close_menu_mobile: new Event('menu_mobile_close'),
			close_dialog: new Event('dialog_close'),
	
			reload_root_sign_in: new Event('reload_root_sign_in'),
			reload_user_sign_in: new Event('reload_user_sign_in'),
	
			reload_menu_mobile: new Event('menu_mobile_reload'),
			reload_menu: new Event('menu_reload'),
			reload_cart: new Event('cart_reload'),
			reload_searcher: new Event('searcher_reload'),
			reload_ground: new Event('ground_reload'),
			reload_dialog: new Event('dialog_reload')
		}
	};

/***/ },
/* 10 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var event_creator = exports.event_creator = function event_creator(name) {
		return function (args) {
			return new CustomEvent(name, {
				'detail': args
			});
		};
	},
	    event_broker = exports.event_broker = function event_broker(fun) {
		return function (event) {
			fun(this, event);
		};
	};

/***/ },
/* 11 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Search_Controller = Search_Controller;
	
	var _block = __webpack_require__(12);
	
	var _controller = __webpack_require__(25);
	
	var _controller2 = __webpack_require__(28);
	
	var _define = __webpack_require__(68);
	
	var _define2 = __webpack_require__(41);
	
	function Search_Controller() {
		if (_typeof(Search_Controller.instance) === 'object') return Search_Controller.instance;
	
		Search_Controller.instance = this;
	
		var container = '.searcher',
		    config_loader = {
			part_name: 'searcher',
			container: container
		},
		    searcher_loader = new _block.Block_Loader_Part(config_loader),
		    searcher_motion_controller = new _controller.Block_Motion_Controllers({
			container: '#SEARCHER',
			content: container,
			open: 'right',
			can_open_by: 'width',
			can_open_to: 1000,
			duration_open: 200,
			duration_close: 200
		}),
		    searcher_form_controller = new _controller2.Form_Controllers(config_loader);
	
		this.define = function () {
			APP.add_own_event('searcher_open', searcher_motion_controller.plugin_open);
	
			searcher_motion_controller.define();
			searcher_form_controller.define();
	
			(0, _define.define_directory_tree)(config_loader);
			(0, _define2.define_post_button)({
				container: '#SEARCHER',
				part_name: 'searcher'
			});
		};
	
		this.get_content = function () {
			searcher_loader.define();
			searcher_loader.load_content();
	
			searcher_motion_controller.set_start_position();
		};
	}

/***/ },
/* 12 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Loader_Part = Block_Loader_Part;
	
	var _block = __webpack_require__(13);
	
	var _controller = __webpack_require__(19);
	
	var _structure = __webpack_require__(14);
	
	var _data = __webpack_require__(16);
	
	var _standard = __webpack_require__(21);
	
	function Block_Loader_Part(config) {
		_controller.Block_Loader.call(this, config);
	
		this._settings.load_meta_tags = false;
	
		(0, _data.add_to_settings)(config, this, 'load_meta_tags');
	}
	
	Block_Loader_Part.prototype = Object.create(_controller.Block_Loader.prototype);
	
	Block_Loader_Part.prototype._prepare_post_data = function (post_data) {
		if (!post_data) post_data = {};
	
		post_data[this._settings.post_name] = 'content';
	
		this._variables.post_data = post_data;
	};
	
	Block_Loader_Part.prototype._send_request = function () {
		var url = this._variables.post_url,
		    data = this._variables.post_data,
		    post_name = this._settings.post_name,
		    request_manager = new _block.Request_Manager_Block();
	
		this._response = request_manager.next(url, data, post_name);
	};
	
	Block_Loader_Part.prototype._load_head_of_page = function () {
		if (this._settings.load_meta_tags) {
			_structure.data_controller.change_much({
				title: APP.DATA.title,
				description: APP.DATA.description
			});
	
			$('title').html(_structure.data_controller.get('title'));
			$('meta[ name="description" ]').attr('content', _structure.data_controller.get('description'));
		}
	};
	
	Block_Loader_Part.prototype._receive_response = function () {
		var _this = this;
	
		return new Promise(function (resolve, reject) {
			_this._response.then(function (response) {
				var precise_data = void 0;
	
				if (_this._check_for_errors(response)) reject(response);else if (_this._is_redirect(response)) precise_data = {
					status: 'success',
					code: response.code,
					url: response.url
				};else precise_data = {
					html: response.html,
					status: 'success',
					code: response.code
				};
	
				resolve(precise_data);
			}).catch(reject);
		});
	};
	
	Block_Loader_Part.prototype.redirect = function (change_url) {
		var _this2 = this;
	
		return new Promise(function (resolve) {
			var url = APP.DATA.redirect || _structure.data_controller.get('path'),
			    delay = (0, _data.select_number)(APP.DATA.delay, 0),
			    state = _this2._state,
			    variables = _this2._variables;
	
			state.can_do_redirect = true;
			clearTimeout(variables.redirect_time_out);
	
			variables.redirect_time_out = setTimeout(function () {
				if (state.can_do_redirect === true) {
					var request_manager = new _block.Request_Manager_Block();
	
					change_url(url);
	
					_this2.load_content(url).then(resolve);
					request_manager.send_list();
				}
			}, delay);
		});
	};
	
	Block_Loader_Part.prototype.reload = function () {
		var _this3 = this;
	
		(0, _standard.timeout_promise)().then(function () {
			_this3.load_content();
		});
	};
	
	Block_Loader_Part.prototype._is_redirect = function (response) {
		return response && response.code === 302;
	};
	
	Block_Loader_Part.prototype.load_content = function (post_url, post_data) {
		var _this4 = this;
	
		return new Promise(function (resolve) {
			_this4._get_content(post_url, post_data);
	
			_this4._hide_content().then(function () {
				_this4._receive_response().then(function (response) {
					if (_this4._is_redirect(response)) resolve(response);
	
					_this4._set_content(response);
	
					_this4._load_head_of_page();
	
					_this4._prepare_content_to_show(response);
	
					_this4._show_content().then(function () {
						resolve(response);
					});
				}).catch(function (response) {
					var dialog_event = new CustomEvent('open_dialog_error', {
						'detail': {
							title: 'Error',
							content: response.content,
							code: response.code
						}
					});
	
					APP.throw_event(dialog_event);
	
					_this4._prepare_content_to_show(response);
	
					_this4._show_content().then(function () {
						resolve(response);
					});
				});
			});
		});
	};
	
	Block_Loader_Part.prototype.load_simple_content = function (url, post_data) {
		var request_manager = new _block.Request_Manager_Block(),
		    result = this.load_content(url, post_data);
	
		request_manager.send_list();
		return result;
	};

/***/ },
/* 13 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Request_Manager_Block = Request_Manager_Block;
	
	var _structure = __webpack_require__(14);
	
	var _init = __webpack_require__(15);
	
	__webpack_require__(18);
	
	var _model = __webpack_require__(17);
	
	var model = _interopRequireWildcard(_model);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	function Request_Manager_Block() {
		if (_typeof(Request_Manager_Block.instance) === 'object') return Request_Manager_Block.instance;
	
		_init.Request_Manager.call(this);
	
		model._sending = undefined;
		model._data_block = {};
	
		this._clear_request();
	
		Request_Manager_Block.instance = this;
	}
	
	Request_Manager_Block.prototype = Object.create(_init.Request_Manager.prototype);
	
	Request_Manager_Block.prototype._add_request = function (url, post_data) {
		if (typeof model._data_block.url === 'undefined') model._data_block.url = url;
	
		model._data_block.list.push(post_data);
	};
	
	Request_Manager_Block.prototype._clear_request = function () {
		model._sending = false;
	
		model._data_block = {
			url: undefined,
			list: []
		};
	
		model._data = {
			url: undefined,
			data: {}
		};
	};
	
	Request_Manager_Block.prototype._prepare_block_post_data = function () {
		var post_data = {};
	
		if (model._data_block.list.length) {
			model._data_block.list.forEach(function (element) {
				if (element) Object.assign(post_data, element);else return false;
			});
	
			post_data[_structure.data_controller.get_crsf('name')] = _structure.data_controller.get_crsf('value');
	
			return post_data;
		}
	
		return false;
	};
	
	Request_Manager_Block.prototype._add_to_queue = function () {
		var data = {
			post_url: undefined,
			post_data: this._prepare_block_post_data()
		},
		    do_step = function do_step(resolve) {
			resolve(data);
		},
		    promise = new Promise(function (resolve) {
			var length = model._queue.length,
			    last_number = length - 1;
	
			if (length === 0) model._request_promise.then(function () {
				return do_step(resolve);
			});else model._queue[last_number].promise.then(function () {
				return do_step(resolve);
			});
		}),
		    queue_data = Object.assign({ promise: promise }, data);
	
		model._queue.push(queue_data);
	
		return promise;
	};
	
	Request_Manager_Block.prototype._make_request = function (timer, send_and_wait, resolve, reject) {
		clearTimeout(timer);
	
		if (model._sending === false) reject('Request Manager error: Promise doesn\'t exist.');
	
		this._send_request().then(function (response) {
			resolve(response);
		}).catch(reject);
	};
	
	Request_Manager_Block.prototype._run_sending = function () {
		var _this = this;
	
		if (model._sending === false) model._sending = new Promise(function (resolve, reject) {
			var throw_exception = function throw_exception() {
				_this._catch_timeout_error();
			},
			    send_and_wait = function send_and_wait() {
				window.removeEventListener('send_request', send_and_wait, false);
	
				if (model._request_status === false) {
					var timer = setTimeout(throw_exception, 3000);
	
					model._data.url = model._data_block.url;
					model._data.data = _this._prepare_block_post_data();
	
					_this._make_request(timer, send_and_wait, resolve, reject);
				} else {
					_this._add_to_queue().then(function (data) {
						var timer = setTimeout(throw_exception, 3000);
	
						model._data.url = model._data_block.url;
						model._data.data = data.post_data;
	
						_this._make_request(timer, send_and_wait, resolve, reject);
					});
				}
			};
	
			window.addEventListener('send_request', send_and_wait, false);
		});
	
		return model._sending;
	};
	
	Request_Manager_Block.prototype.next = function (post_url, post_data, post_name) {
		var _this2 = this;
	
		return new Promise(function (resolve, reject) {
			_this2._add_request(post_url, post_data);
	
			_this2._run_sending().then(function (response) {
				if (typeof response.json[post_name] !== 'undefined') response = response.json[post_name];else reject({
					content: 'Request_Manager_Block error: Invalid response.',
					code: response.code
				});
	
				resolve(response);
			}).catch(reject);
		});
	};
	
	delete Request_Manager_Block.prototype.send;
	
	Request_Manager_Block.prototype.send_list = function () {
		APP.throw_event(window.EVENTS.send_request);
	};

/***/ },
/* 14 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var data_controller = exports.data_controller = new function Data_Controller() {
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
				page_name: 'Medinox',
				title: 'Loading - Medinox',
				description: 'This page is shop, which is ownership Medinox.',
				statement_content: 'Empty statement.'
			};
		};
	
		this.reset();
	
		this.get = function (name) {
			if (typeof private_data[name] !== 'undefined') return private_data[name];else if (typeof public_data[name] !== 'undefined') return public_data[name];else {
				console.warn('Data structure error: Wrong call! Veriable with this name doesn\'t exist: "' + name + '".');
			}
		};
	
		this.get_crsf = function (what) {
			if (what === 'name') return 'csrfmiddlewaretoken';else if (what === 'value') return private_data.csrf_token;else console.warn('Data structure error: Wrong call! Veriable with this name doesn\'t exist (crsf).');
		};
	
		this.change = function (name, value) {
			if (typeof public_data[name] !== 'undefined' && typeof value !== 'undefined') public_data[name] = value;else console.warn('Data structure error: Wrong call! Veriable with this name doesn\'t exist: "' + name + '".');
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
/* 15 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Request_Manager = Request_Manager;
	
	var _structure = __webpack_require__(14);
	
	var _data2 = __webpack_require__(16);
	
	var _model = __webpack_require__(17);
	
	var model = _interopRequireWildcard(_model);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	function Request_Manager() {
		var _this = this;
	
		var error = false,
		    pack_response = function pack_response(json, code) {
			try {
				var data = {
					json: JSON.parse(json),
					code: code
				};
	
				console.log(data);
				console.groupEnd();
				return data;
			} catch (e) {
				var _data = {
					json: json,
					code: code
				};
				error = true;
	
				console.log(_data);
				console.groupEnd();
	
				_this._show_error(json);
	
				return _data;
			}
		},
		    check_status = function check_status(code) {
			return code >= 200 && code < 400;
		};
	
		this._request = function (obj) {
			return new Promise(function (resolve, reject) {
				var xhr = new XMLHttpRequest(),
				    method = obj.method || "GET",
				    data = (0, _data2.object_to_formdata)(obj.data);
	
				error = false;
				model._request_status = true;
	
				console.group('Request data: ');
				console.log(obj.url);
				console.log(obj.data);
	
				xhr.open(method, obj.url);
	
				if (obj.headers) {
					Object.keys(obj.headers).forEach(function (key) {
						xhr.setRequestHeader(key, obj.headers[key]);
					});
				}
	
				xhr.onload = function () {
					if (error === false) if (check_status(xhr.status)) resolve(pack_response(xhr.response, xhr.status));else reject(pack_response(xhr.response, xhr.status));
				};
				xhr.onerror = function () {
					if (error === false) reject(pack_response(xhr.response, xhr.status));
				};
				xhr.send(data);
			});
		};
	}
	
	Request_Manager.prototype._clear_request = function () {
		model._data = {
			url: undefined,
			data: {}
		};
	};
	
	Request_Manager.prototype._add_request = function (post_url, post_data) {
		if (model._data.url === undefined) model._data.url = post_url || '';
	
		model._data.data = post_data || {};
	};
	
	Request_Manager.prototype._prepare_url = function () {
		var url = model._data.url;
	
		if (url && url.substring && url.substring(0, 1) === '/') return url;else return _structure.data_controller.get('path');
	};
	
	Request_Manager.prototype._prepare_post_data = function () {
		if (model._data.data) {
			var post_data = model._data.data;
	
			post_data[_structure.data_controller.get_crsf('name')] = _structure.data_controller.get_crsf('value');
	
			return post_data;
		}
	
		return false;
	};
	
	Request_Manager.prototype._send_request = function () {
		var _this2 = this;
	
		model._request_promise = new Promise(function (resolve, reject) {
			var post_url = _this2._prepare_url(),
			    post_data = _this2._prepare_post_data();
	
			if (post_data) {
				_this2._clear_request();
	
				_this2._request({
					method: 'POST',
					url: post_url,
					data: post_data
				}).then(function (response) {
					model._request_status = false;
					resolve(response);
				}).catch(function (response) {
					model._request_status = false;
					reject({
						content: 'Request Manager error: Invalid response.',
						code: response.code
					});
				});
			} else {
				console.trace();
				console.warn(post_data);
				reject({
					content: 'Request Manager error: Invalid post data.',
					code: undefined
				});
			}
		});
	
		return model._request_promise;
	};
	
	Request_Manager.prototype._show_error = function (response) {
		var new_tab = window.open('', '_blank');
		new_tab.document.write(response);
		new_tab.focus();
	};
	
	Request_Manager.prototype._catch_timeout_error = function () {
		console.error('Request Manager error: Request Timeout. ' + 'Run `send` in Request Manager.');
	
		this._clear_request();
	};

/***/ },
/* 16 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var is_undefined = exports.is_undefined = function is_undefined(object) {
		return typeof object === 'undefined';
	},
	    is_defined = exports.is_defined = function is_defined(object) {
		return typeof object !== 'undefined';
	},
	    is_number = exports.is_number = function is_number(object) {
		return typeof object === 'number';
	},
	    is_not_number = exports.is_not_number = function is_not_number(object) {
		return typeof object !== 'number';
	},
	    is_empty = exports.is_empty = function is_empty(string) {
		return string === '';
	},
	    object_to_formdata = exports.object_to_formdata = function object_to_formdata(obj) {
		var form_data = new FormData();
	
		for (var prop in obj) {
			if (obj.hasOwnProperty(prop)) form_data.append(prop, obj[prop]);
		}return form_data;
	},
	    select_number = exports.select_number = function select_number(to_checking, emergency) {
		if (is_number(to_checking)) return to_checking;
	
		if (is_number(emergency)) return emergency;
	
		console.error('Utilities data error: Variable emergency is not number.');
		return undefined;
	},
	    add_to_object = exports.add_to_object = function add_to_object(from, to, from_what, to_what) {
		if (is_undefined(from[from_what])) return false;
	
		if (from_what && to_what) to[to_what] = from[from_what];else if (from_what) to[from_what] = from[from_what];
	},
	    add_to_settings = exports.add_to_settings = function add_to_settings(from, to, from_what, to_what) {
		if (is_undefined(to) && is_undefined(to._settings)) {
			console.error('Data Utilities error: Invalid object.');
			return false;
		}
	
		add_to_object(from, to._settings, from_what, to_what);
	};

/***/ },
/* 17 */
/***/ function(module, exports) {

	"use strict";
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var _data = exports._data = undefined,
	    _data_block = exports._data_block = undefined,
	    _queue = exports._queue = [],
	    _request_promise = exports._request_promise = undefined,
	    _request_status = exports._request_status = false;
	
	window.queue = _queue;

/***/ },
/* 18 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Request_Manager = undefined;
	
	var _init = __webpack_require__(15);
	
	Object.defineProperty(exports, 'Request_Manager', {
		enumerable: true,
		get: function get() {
			return _init.Request_Manager;
		}
	});
	
	var _model = __webpack_require__(17);
	
	var model = _interopRequireWildcard(_model);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	_init.Request_Manager.prototype._add_to_queue = function (data) {
		var _this = this;
	
		var do_step = function do_step(resolve, reject) {
			_this._make_request(data, resolve, reject);
		},
		    promise = new Promise(function (resolve, reject) {
			var length = _this._queue.length,
			    last_number = length - 1;
	
			if (length === 0) model._request_promise.then(function () {
				return do_step(resolve, reject);
			});else model._queue[last_number].promise.then(function () {
				return do_step(resolve, reject);
			});
		}),
		    queue_data = Object.assign({ promise: promise }, data);
	
		model._queue.push(queue_data);
	
		return promise;
	};
	
	_init.Request_Manager.prototype._make_request = function (data, resolve, reject) {
		var _this2 = this;
	
		var post_url = data.post_url,
		    post_data = data.post_data,
		    post_name = data.post_name;
	
		this._add_request(post_url, post_data);
	
		this._send_request().then(function (response) {
			_this2._clear_request();
	
			if (typeof response.json[post_name] !== 'undefined') response = response.json[post_name];else {
				console.error('Request_Manager error: Invalid response.');
				reject('Request_Manager error: Invalid response.');
			}
	
			resolve(response);
		}).catch(reject);
	};
	
	_init.Request_Manager.prototype.send = function (post_url, post_data, post_name) {
		var _this3 = this;
	
		if (typeof post_name === 'undefined') {
			console.error('Request_Manager error: Invalid variable "post_name"');
			return false;
		}
	
		var data = {
			post_url: post_url,
			post_data: post_data,
			post_name: post_name
		};
	
		if (model._request_status === false) return new Promise(function (resolve, reject) {
			_this3._make_request(data, resolve, reject);
		});else return this._add_to_queue(data);
	};

/***/ },
/* 19 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Loader = undefined;
	
	var _init = __webpack_require__(20);
	
	Object.defineProperty(exports, 'Block_Loader', {
		enumerable: true,
		get: function get() {
			return _init.Block_Loader;
		}
	});
	
	var _structure = __webpack_require__(14);
	
	var _data = __webpack_require__(16);
	
	var _standard = __webpack_require__(21);
	
	var _block = __webpack_require__(13);
	
	__webpack_require__(22);
	
	__webpack_require__(23);
	
	_init.Block_Loader.prototype.redirect = function () {
		var _this = this;
	
		return new Promise(function (resolve) {
			var url = APP.DATA.redirect || _structure.data_controller.get('path'),
			    delay = (0, _data.select_number)(APP.DATA.delay, 0),
			    state = _this._state,
			    variables = _this._variables;
	
			state.can_do_redirect = true;
			clearTimeout(variables.redirect_time_out);
	
			variables.redirect_time_out = setTimeout(function () {
				if (state.can_do_redirect === true) {
					var request_manager = new _block.Request_Manager_Block();
	
					_this.load_content(url).then(resolve);
					request_manager.send_list();
				}
			}, delay);
		});
	};
	
	_init.Block_Loader.prototype.reload = function () {
		var _this2 = this;
	
		return new Promise(function (resolve) {
			var delay = (0, _data.select_number)(APP.DATA.delay, 0);
	
			(0, _standard.timeout_promise)(delay).then(function () {
				_this2.load_content().then(resolve);
			});
		});
	};
	
	_init.Block_Loader.prototype.load_content = function (post_url, post_data) {
		var _this3 = this;
	
		return new Promise(function (resolve) {
			_this3._get_content(post_url, post_data);
	
			_this3._hide_content().then(function () {
				_this3._receive_response().then(function (response) {
					_this3._set_content(response);
	
					_this3._prepare_content_to_show();
	
					_this3._show_content().then(function () {
						resolve(response);
					});
				});
			});
		});
	};
	
	_init.Block_Loader.prototype.define = function () {
		var _this4 = this;
	
		APP.add_own_event(this._settings.part_name + '_reload', function () {
			_this4.reload();
		});
	};

/***/ },
/* 20 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Loader = Block_Loader;
	
	var _data = __webpack_require__(16);
	
	function Block_Loader(config) {
	
		if (typeof config === 'undefined') {
			console.error('Part Loader error: Invalid configuration.');
			return {};
		}
	
		this._settings = {
			part_name: undefined,
			post_name: undefined,
	
			container: undefined,
	
			duration_show: 150,
			duration_hide: 100,
	
			opacity_show: 1,
			opacity_hide: 0.4
		};
	
		this._variables = {
			post_url: undefined,
			post_data: undefined,
	
			external_callback: undefined,
			redirect_time_out: undefined
		};
	
		this._state = {
			reload: false,
	
			can_do_load: true,
			can_do_redirect: true
		};
	
		(0, _data.add_to_settings)(config, this, 'part_name');
		this._settings.post_name = '__' + this._settings.part_name + '__';
	
		(0, _data.add_to_settings)(config, this, 'container');
	
		(0, _data.add_to_settings)(config, this, 'duration_show');
		(0, _data.add_to_settings)(config, this, 'duration_hide');
	
		(0, _data.add_to_settings)(config, this, 'opacity_show');
		(0, _data.add_to_settings)(config, this, 'opacity_hide');
	}

/***/ },
/* 21 */
/***/ function(module, exports, __webpack_require__) {

	"use strict";
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.timeout_promise = undefined;
	
	var _data = __webpack_require__(16);
	
	var timeout_promise = exports.timeout_promise = function timeout_promise(delay) {
		if ((0, _data.is_not_number)(delay)) delay = 0;
	
		return new Promise(function (resolve) {
			setTimeout(function () {
				resolve();
			}, delay);
		});
	};

/***/ },
/* 22 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _structure = __webpack_require__(14);
	
	var _block = __webpack_require__(13);
	
	var _init = __webpack_require__(20);
	
	_init.Block_Loader.prototype._if_reload = function (url) {
		var old_url = _structure.data_controller.get('path'),
		    new_url = url;
	
		return old_url === new_url || !new_url;
	};
	
	_init.Block_Loader.prototype._refresh_events = function () {
		APP.throw_event(EVENTS.define);
	};
	
	_init.Block_Loader.prototype._prepare_to_change_content = function (post_url) {
		this._variables.post_url = post_url;
		this._state.can_do_redirect = false;
		this._state.reload = this._if_reload(post_url);
	
		_structure.data_controller.reset();
	};
	
	_init.Block_Loader.prototype._prepare_post_data = function (post_data) {
		if (!post_data) post_data = {};
	
		post_data[this._settings.post_name] = 'content';
	
		this._variables.post_data = post_data;
	};
	
	_init.Block_Loader.prototype._send_request = function () {
		var url = this._variables.post_url,
		    data = this._variables.post_data,
		    post_name = this._settings.post_name,
		    request_manager = new _block.Request_Manager_Block();
	
		this._response = request_manager.send(url, data, post_name);
	};
	
	_init.Block_Loader.prototype._check_for_errors = function (response) {
		if (typeof response.html === 'undefined' || typeof response.code === 'undefined') return true;
	
		return false;
	};
	
	_init.Block_Loader.prototype._process_response = function (response) {
		return {
			html: response.html,
			code: response.code
		};
	};

/***/ },
/* 23 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _img_loader = __webpack_require__(24);
	
	var img_loader = _interopRequireWildcard(_img_loader);
	
	var _init = __webpack_require__(20);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	_init.Block_Loader.prototype._hide_content = function () {
		var _this = this;
	
		return new Promise(function (resolve) {
			var container = _this._settings.container,
			    opacity = _this._settings.opacity_hide,
			    duration = _this._settings.duration_hide;
	
			$(container).animate({ opacity: opacity }, duration, resolve);
		});
	};
	
	_init.Block_Loader.prototype._get_content = function (post_url, post_data) {
		this._prepare_to_change_content(post_url);
		this._prepare_post_data(post_data);
	
		this._send_request();
	};
	
	_init.Block_Loader.prototype._receive_response = function () {
		var _this2 = this;
	
		return new Promise(function (resolve) {
			_this2._response.then(function (response) {
				resolve(_this2._process_response(response));
			});
		});
	};
	
	_init.Block_Loader.prototype._prepare_content_to_show = function (response) {
		if (this._state.reload === false) $(this._settings.container).scrollTop(0);
	
		if (response.html !== '') {
			this._refresh_events();
			img_loader.define();
		}
	};
	
	_init.Block_Loader.prototype._set_content = function (response) {
		if (response.html !== '') $(this._settings.container).html(response.html);
	};
	
	_init.Block_Loader.prototype._show_content = function () {
		var _this3 = this;
	
		return new Promise(function (resolve) {
			var container = _this3._settings.container,
			    opacity = _this3._settings.opacity_show,
			    duration = _this3._settings.duration_show;
	
			$(container).animate({ opacity: opacity }, duration, resolve);
		});
	};

/***/ },
/* 24 */
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
	      default_src = '/static/img/icons/256/band_aid.png',
	      image = new Image();
	
	  function download_img($imgs, i) {
	    if (!$imgs[i]) return false;
	
	    var downloadingImage = new Image(),
	        data_src = attr($imgs[i], 'data-src'),
	        data_src_default = attr($imgs[i], 'data-default-src');
	
	    downloadingImage.onload = function () {
	      $imgs[i].src = this.src;
	      setTimeout(function () {
	        $imgs[i].style = 'opacity: 1;';
	        download_img($images, i + 1);
	      }, 100);
	    };
	
	    downloadingImage.onerror = function () {
	      $imgs[i].src = data_src_default || default_src;
	
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
/* 25 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Motion_Controllers = undefined;
	
	var _views = __webpack_require__(26);
	
	var Block_Motion_Controllers = exports.Block_Motion_Controllers = function Block_Motion_Controllers(config) {
		var plugin_motion_views = new _views.Block_Motion_Views(config),
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
	
			APP.add_own_event('part_close', pre_plugin_close);
			APP.throw_event(EVENTS.part.close);
		};
	
		this.plugin_open = plugin_motion_views.plugin_open;
		this.plugin_close = plugin_motion_views.plugin_close;
		this.is_open = plugin_motion_views.is_open;
	};

/***/ },
/* 26 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Motion_Views = undefined;
	
	var _models = __webpack_require__(27);
	
	var Block_Motion_Views = exports.Block_Motion_Views = function Block_Motion_Views(config) {
		var models = new _models.Block_Motion_Models(config),
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
/* 27 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Block_Motion_Models = undefined;
	
	var _structure = __webpack_require__(14);
	
	var Block_Motion_Models = exports.Block_Motion_Models = function Block_Motion_Models(config) {
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
/* 28 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Form_Controllers = undefined;
	
	var _model = __webpack_require__(29);
	
	var _model_for_dialog = __webpack_require__(48);
	
	var _controllers = __webpack_require__(51);
	
	var validator = _interopRequireWildcard(_controllers);
	
	var _controllers2 = __webpack_require__(55);
	
	var auto_form = _interopRequireWildcard(_controllers2);
	
	var _controllers3 = __webpack_require__(58);
	
	var _controller = __webpack_require__(59);
	
	var _controllers4 = __webpack_require__(60);
	
	var file_converter = _interopRequireWildcard(_controllers4);
	
	var _controller2 = __webpack_require__(63);
	
	var _controller3 = __webpack_require__(65);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var Form_Controllers = exports.Form_Controllers = function Form_Controllers(config, is_dialog) {
		var address_switcher = new _controller2.Address_Switcher_Controller(config),
		    currency_converter = new _controller3.Currency_Converter_Controller(config),
		    selected_form = new _controllers3.Selected_Form_Controller(config),
		    feature_setter = new _controller.Feature_Setter(config),
		    form_models = void 0,
		    variables = void 0;
	
		if (is_dialog === true) form_models = new _model_for_dialog.Dialog_Form_Models(config);else form_models = new _model.Form_Models(config);
	
		variables = form_models.variables;
	
		var prepare_form_to_send = function prepare_form_to_send(event) {
			var form_action = $(this).attr('action'),
			    protocol = void 0;
	
			if (typeof form_action === 'string') protocol = form_action.substring(0, 4);
	
			if (protocol !== 'http') {
				event.preventDefault();
	
				variables.form_name = $(this).data('name');
				variables.post_url = $(this).attr('action');
				variables.post_data = $(this).serialize_object();
				variables.reload = $(this).data('reload');
				variables.redirect = $(this).data('redirect');
				variables.event = $(this).data('event');
				variables.delay = $(this).data('delay');
	
				form_models.send();
			}
		};
	
		this.define = function () {
			var $container = $(config.container),
			    config_form = {
				post_name: '__' + config.part_name + '__',
				$container: $container
			};
	
			$('form', $container).submit(prepare_form_to_send);
	
			validator.define(config_form);
			auto_form.define(config_form);
			file_converter.define(config_form);
			feature_setter.define(config_form);
			selected_form.define();
			address_switcher.define();
			currency_converter.define();
		};
	};

/***/ },
/* 29 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Form_Models = undefined;
	
	var _utilities = __webpack_require__(30);
	
	var utilities = _interopRequireWildcard(_utilities);
	
	var _form = __webpack_require__(31);
	
	var _controller = __webpack_require__(32);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var Form_Models = exports.Form_Models = function Form_Models(config) {
		var _this = this;
	
		this._form_loader = new _form.Block_Loader_Form(config);
		this._ground_controller = new _controller.Ground_Controller();
	
		this.variables = {
			form_name: undefined,
			post_url: undefined,
			post_data: undefined,
	
			reload: undefined,
			redirect: undefined,
			event: undefined,
			delay: undefined
		};
	
		this._prepare_post_data = function () {
			var variables = _this.variables;
	
			if (!variables.post_data) variables.post_data = {};
	
			variables.post_data._name_ = variables.form_name;
		};
	
		this._end_loading = function (response) {
			if (_this._ground_controller.is_redirect(response)) {
				_this._ground_controller.change_url(response.url);
				_this._ground_controller.load_single_ground_content();
			}
	
			var variables = _this.variables,
			    events = void 0;
	
			events = {
				reload: variables.reload,
				redirect: variables.redirect,
				events: variables.event,
				delay: variables.delay
			};
	
			utilities.reload_plugins(events);
			utilities.redirect_ground(events);
			utilities.launch_event(events);
		};
	};
	
	Form_Models.prototype.send = function () {
		var post_url = this.variables.post_url,
		    post_data = this.variables.post_data;
	
		this._prepare_post_data();
	
		this._form_loader.load_simple_content(post_url, post_data).then(this._end_loading);
	};

/***/ },
/* 30 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.launch_event = exports.redirect_ground = exports.reload_plugins = exports.prepare_delay = exports.get_and_remove_data = exports.get_data = exports.request_manager = undefined;
	
	var _block = __webpack_require__(13);
	
	var _standard = __webpack_require__(21);
	
	__webpack_require__(16);
	
	var get_event_creator = function get_event_creator(events, text_event) {
		var fun = void 0,
		    end_position_of_function = text_event.indexOf('(');
	
		if (end_position_of_function > 0) {
			var fun_string = text_event.slice(0, end_position_of_function);
	
			fun = events[fun_string];
	
			if (typeof fun !== 'undefined' && fun.constructor !== Event) return fun;
		}
	},
	    get_args_from_event = function get_args_from_event(text_event) {
		var bracket_1 = text_event.indexOf('('),
		    bracket_2 = text_event.indexOf(')'),
		    args_obj = {};
	
		if (bracket_1 >= 0 && bracket_2 > bracket_1) {
			var start_slice = bracket_1 + 1,
			    end_slice = bracket_2,
			    phrase = text_event.slice(start_slice, end_slice),
			    split_args = void 0;
	
			if (phrase.indexOf(',') > 0) split_args = phrase.split(',');else split_args = [phrase];
	
			for (var i = 0; split_args.length > i; ++i) {
				var arg = split_args[i],
				    value_position = arg.indexOf(':'),
				    name = arg.slice(0, value_position),
				    value = arg.slice(value_position + 1);
	
				if (name && value) args_obj[name] = value;
			}
	
			return args_obj;
		}
	
		return {};
	};
	
	var request_manager = exports.request_manager = new _block.Request_Manager_Block(),
	    get_data = exports.get_data = function get_data(elem, name) {
		return $(elem).data(name);
	},
	    get_and_remove_data = exports.get_and_remove_data = function get_and_remove_data(elem, name) {
		var data = get_data(elem, name);
	
		if (typeof data === 'undefined') data = '';
	
		return String(data);
	},
	    prepare_delay = exports.prepare_delay = function prepare_delay(data) {
		var delay = data.delay;
	
		if (delay >= 0) APP.DATA.delay = delay;else APP.DATA.delay = 0;
	},
	    reload_plugins = exports.reload_plugins = function reload_plugins(data) {
		var plugins = data.reload,
		    plugins_array = void 0,
		    array_length = void 0,
		    delay = 0;
	
		if (!plugins || typeof plugins !== 'string') return false;
	
		plugins_array = plugins.split(' ');
		array_length = plugins_array.length;
	
		for (var i = 0; i < array_length; ++i) {
			if (plugins_array[i]) {
				prepare_delay(data);
				APP.throw_event(EVENTS.part['reload_' + plugins_array[i]]);
			}
		}if (typeof APP.DATA.delay !== 'undefined') {
			delay = APP.DATA.delay;
			APP.DATA.delay = undefined;
		}
	
		(0, _standard.timeout_promise)(delay).then(function () {
			request_manager.send_list();
		});
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
					if (typeof ready_event[split_event[_i]] === 'undefined') {
						var fun = get_event_creator(ready_event, split_event[_i]),
						    args = get_args_from_event(split_event[_i]);
	
						if (fun && args) ready_event = fun(args);else console.error('Launch Event error: Event ' + split_event[_i] + ' doesn\'t exist.');
					} else ready_event = ready_event[split_event[_i]];
				}if (ready_event.constructor === Event || ready_event.constructor === CustomEvent) {
					prepare_delay(data);
					APP.throw_event(ready_event);
				} else console.error('Event error: This event doesn\'t exist');
			}
		}
	};

/***/ },
/* 31 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Loader_Form = Block_Loader_Form;
	
	var _block = __webpack_require__(13);
	
	var _block2 = __webpack_require__(12);
	
	function Block_Loader_Form(config) {
		_block2.Block_Loader_Part.call(this, config);
	}
	
	Block_Loader_Form.prototype = Object.create(_block2.Block_Loader_Part.prototype);
	
	Block_Loader_Form.prototype._prepare_post_data = function (post_data) {
		if (!post_data) post_data = {};
	
		post_data[this._settings.post_name] = 'form';
	
		this._variables.post_data = post_data;
	};
	
	Block_Loader_Form.prototype._send_request = function () {
		var post_url = this._variables.post_url,
		    post_data = this._variables.post_data,
		    post_name = this._settings.post_name,
		    request_manager = new _block.Request_Manager_Block();
	
		this._response = request_manager.next(post_url, post_data, post_name);
	};
	
	Block_Loader_Form.prototype.load_simple_content = function (post_url, post_data) {
		var request_manager = void 0,
		    loading = void 0;
	
		request_manager = new _block.Request_Manager_Block();
	
		loading = this.load_content(post_url, post_data);
		request_manager.send_list();
	
		return loading;
	};

/***/ },
/* 32 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Ground_Controller = Ground_Controller;
	
	var _view = __webpack_require__(33);
	
	function Ground_Controller() {
		if (_typeof(Ground_Controller.instance) === 'object') return Ground_Controller.instance;
	
		Ground_Controller.instance = this;
	
		var view = new _view.Ground_View(),
		    model = view.model,
		    transfer_event = function transfer_event(fun) {
			return function (event) {
				fun(this, event);
			};
		},
		    disable_cookie = function disable_cookie() {
			$(this).remove();
			$('.footer-cookies-content').html('&nbsp;');
		};
	
		this.is_redirect = function (response) {
			return model.is_redirect(response);
		};
		this.change_url = function (url) {
			return model.change_url(url);
		};
		this.load_single_ground_content = function () {
			return model.load_single_ground_content();
		};
	
		this.define = function () {
			view.change_height_content();
	
			$('a').click(transfer_event(view.go_to_link));
			APP.add_own_event('redirect', model.redirect_ground);
			APP.add_own_event('popstate', model.back_url);
			$(window).resize(transfer_event(view.change_height_content));
	
			var $container = $(model.container);
	
			$('.change_length', $container).click(transfer_event(view.change_to_long));
			$('.change_length .change_length-button', $container).click(transfer_event(view.change_to_long_or_short));
	
			$('.cookie_disabler').click(disable_cookie);
	
			model.ground_form_controller.define();
			model.define_post_button(model.config_loader);
			model.define_event_button(model.config_form);
		};
	
		this.get_content = function () {
			model.ground_loader.define();
			model.load_ground_content();
		};
	}

/***/ },
/* 33 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Ground_View = Ground_View;
	
	var _model = __webpack_require__(34);
	
	function Ground_View() {
		var _this = this;
	
		var model = void 0;
	
		this.model = new _model.Ground_Model();
		model = this.model;
	
		this.go_to_link = function (that, event) {
			var url = $(that).attr('href'),
			    protocol = url.substring(0, 4),
			    mailto = url.substring(0, 7);
	
			if (protocol !== 'http' && protocol !== 'tel:' && mailto !== 'mailto:') if (event.which === 1) {
				event.preventDefault();
				APP.throw_event(EVENTS.part.close);
	
				model.change_url(url);
	
				model.load_single_ground_content(url);
			}
		};
	
		this._change_height_ground = function () {
			var $ground = $(model.container),
			    height = {
				window: model.page_controller.get_height(),
				header: model.menu_controller.get_height(),
				ground_top: $ground.position().top
			},
			    height_ground = height.window - height.header - height.ground_top;
	
			$ground.height(height_ground);
		};
	
		this._change_height_ground_by_spacer = function () {
			var $ground = $(model.container),
			    $ground_block = $ground.find('.ground-block'),
			    $spacer = $ground.find('.ground-block-spacer'),
			    $footer = $ground.find('.footer'),
			    height = {
				window: model.page_controller.get_height(),
				header: model.menu_controller.get_height(),
				ground_top: $ground.position().top,
				ground_blocks: 0,
				footer: parseInt($footer.outerHeight())
			},
			    height_spacer = height.window - height.header - height.ground_top - height.footer;
	
			if ($ground_block.length) $ground_block.each(function () {
				height.ground_blocks += parseInt($(this).outerHeight());
			});
	
			height_spacer -= height.ground_blocks;
	
			if (height_spacer > 0) {
				if ($spacer.length < 1) $($footer).before('<div class="ground-block-spacer">&nbsp;</div>');
	
				$ground.find('.ground-block-spacer').height(height_spacer);
			} else if ($spacer.length) $spacer.remove();
		};
	
		this.change_height_content = function () {
			_this._change_height_ground();
			_this._change_height_ground_by_spacer();
		};
	
		this.change_to_long_or_short = function (that, event) {
			var $element = $(that).parents('.change_length');
			event.stopPropagation();
	
			if ($element.hasClass('is-long')) $element.removeClass('is-long');else $element.addClass('is-long');
		};
	
		this.change_to_long = function (that, event) {
			event.stopPropagation();
	
			$(that).addClass('is-long');
		};
	}

/***/ },
/* 34 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Ground_Model = Ground_Model;
	
	var _block = __webpack_require__(12);
	
	var _controllers = __webpack_require__(6);
	
	var _controller = __webpack_require__(35);
	
	var _controller2 = __webpack_require__(28);
	
	var _define = __webpack_require__(41);
	
	var _define2 = __webpack_require__(36);
	
	function Ground_Model() {
		var _this = this;
	
		this.container = '.ground';
	
		this.config_loader = {
			part_name: 'ground',
			container: this.container,
			load_meta_tags: true
		};
		this.config_form = {
			part_name: 'ground',
			container: this.container
		};
	
		this.ground_loader = new _block.Block_Loader_Part(this.config_loader);
	
		this.define_post_button = _define.define_post_button;
		this.define_event_button = _define2.define_event_button;
		this.ground_form_controller = new _controller2.Form_Controllers(this.config_loader);
	
		this.page_controller = new _controllers.Page_Controller();
		this.menu_controller = new _controller.Menu_Controller();
	
		this.change_url = function (url) {
			var protocol = url.substring(0, 4),
			    mailto = url.substring(0, 7);
	
			if (protocol !== 'http' && protocol !== 'tel:' && mailto !== 'mailto:') history.pushState('', url, url);else window.location = url;
		};
	
		this.is_redirect = function (response) {
			return response && response.code === 302;
		};
	
		this.check_redirect = function (response) {
			if (_this.is_redirect(response)) {
				_this.change_url(response.url);
				_this.load_single_ground_content();
			}
		};
	
		this.load_ground_content = function (url, data) {
			var result = _this.ground_loader.load_content(url, data);
	
			result.then(function (response) {
				return _this.check_redirect(response);
			});
		};
	
		this.load_single_ground_content = function (url, data) {
			var result = _this.ground_loader.load_simple_content(url, data);
	
			result.then(function (response) {
				return _this.check_redirect(response);
			});
		};
	
		this.redirect_ground = function () {
			var result = _this.ground_loader.redirect(_this.change_url);
	
			result.then(function (response) {
				return _this.check_redirect(response);
			});
		};
	
		this.back_url = function (event) {
			event.preventDefault();
			_this.load_single_ground_content();
		};
	}

/***/ },
/* 35 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Menu_Controller = Menu_Controller;
	
	var _block = __webpack_require__(12);
	
	var _define = __webpack_require__(36);
	
	function Menu_Controller() {
		if (_typeof(Menu_Controller.instance) === 'object') return Menu_Controller.instance;
	
		Menu_Controller.instance = this;
	
		var container_id = '#MENU',
		    container = '.menu',
		    part_name = 'menu',
		    loader = new _block.Block_Loader_Part({
			part_name: part_name,
			container: container
		});
	
		this.get_height = function () {
			return $(container_id).outerHeight();
		};
	
		this.define = function () {
			(0, _define.define_event_button)({
				container: container_id
			});
		};
	
		this.get_content = function () {
			loader.define();
			loader.load_content();
		};
	}

/***/ },
/* 36 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define_event_button = undefined;
	
	var _controller = __webpack_require__(37);
	
	var define_event_button = exports.define_event_button = function define_event_button(config) {
		var $buttons = $('.event_button', config.container);
	
		$buttons.each(function () {
			new _controller.Event_Button(this, config.part_name);
		});
	};

/***/ },
/* 37 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Event_Button = undefined;
	
	var _view = __webpack_require__(38);
	
	Object.defineProperty(exports, 'Event_Button', {
		enumerable: true,
		get: function get() {
			return _view.Event_Button;
		}
	});
	
	var _utilities = __webpack_require__(30);
	
	var _event = __webpack_require__(10);
	
	_view.Event_Button.prototype.collect_data = function (button) {
		this._button_data = {
			elem: button,
			reload: (0, _utilities.get_and_remove_data)(button, 'reload'),
			redirect: (0, _utilities.get_and_remove_data)(button, 'redirect'),
			event: (0, _utilities.get_and_remove_data)(button, 'event'),
			delay: (0, _utilities.get_and_remove_data)(button, 'delay')
		};
	};
	
	_view.Event_Button.prototype.define_events = function (button) {
		var _this = this;
	
		$(button).click((0, _event.event_broker)(function () {
			if (_this._is_not_loading()) {
				_this._set_loading();
	
				_this._run_events();
	
				_this._set_end_loading();
			}
		}));
	};

/***/ },
/* 38 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Event_Button = undefined;
	
	var _model = __webpack_require__(39);
	
	Object.defineProperty(exports, 'Event_Button', {
		enumerable: true,
		get: function get() {
			return _model.Event_Button;
		}
	});
	
	var _utilities = __webpack_require__(30);
	
	_model.Event_Button.prototype._run_events = function () {
		var events = {
			reload: this._button_data.reload,
			redirect: this._button_data.redirect,
			events: this._button_data.event,
			delay: this._button_data.delay
		};
	
		(0, _utilities.reload_plugins)(events);
		(0, _utilities.redirect_ground)(events);
		(0, _utilities.launch_event)(events);
	};

/***/ },
/* 39 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Event_Button = undefined;
	
	var _init = __webpack_require__(40);
	
	Object.defineProperty(exports, 'Event_Button', {
		enumerable: true,
		get: function get() {
			return _init.Event_Button;
		}
	});
	
	
	_init.Event_Button.prototype._is_not_loading = function () {
		return this._variables.is_loading === false;
	};
	
	_init.Event_Button.prototype._set_loading = function () {
		this._variables.is_loading = true;
	};
	
	_init.Event_Button.prototype._set_end_loading = function () {
		this._variables.is_loading = false;
	};

/***/ },
/* 40 */
/***/ function(module, exports) {

	"use strict";
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Event_Button = Event_Button;
	function Event_Button(button) {
		this._button_data = {
			elem: undefined,
	
			reload: undefined,
			redirect: undefined,
			event: undefined,
			delay: undefined
		};
	
		this._variables = {
			is_loading: false
		};
	
		this.collect_data(button);
		this.define_events(button);
	}

/***/ },
/* 41 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define_post_button = undefined;
	
	var _controller = __webpack_require__(42);
	
	var define_post_button = exports.define_post_button = function define_post_button(config) {
		var $post_buttons = $('.post_button', config.container);
	
		$post_buttons.each(function () {
			new _controller.Post_Button(this, config.part_name);
		});
	};

/***/ },
/* 42 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Post_Button = undefined;
	
	var _view = __webpack_require__(43);
	
	Object.defineProperty(exports, 'Post_Button', {
		enumerable: true,
		get: function get() {
			return _view.Post_Button;
		}
	});
	
	var _utilities = __webpack_require__(30);
	
	var _event = __webpack_require__(10);
	
	var get_button_text = function get_button_text(button) {
		var $button = $(button);
	
		if ($button.hasClass('is-text_icon')) return $button.find('.button-text').html();else return $button.html();
	};
	
	_view.Post_Button.prototype.collect_data = function (button) {
		this._button_data = {
			elem: button,
			elem_text: get_button_text(button),
			name: (0, _utilities.get_and_remove_data)(button, 'name'),
			action: (0, _utilities.get_and_remove_data)(button, 'action'),
			value: (0, _utilities.get_and_remove_data)(button, 'value'),
			other_1: (0, _utilities.get_and_remove_data)(button, 'other_1'),
			other_2: (0, _utilities.get_and_remove_data)(button, 'other_2'),
			other_3: (0, _utilities.get_and_remove_data)(button, 'other_3'),
			reload: (0, _utilities.get_and_remove_data)(button, 'reload'),
			redirect: (0, _utilities.get_and_remove_data)(button, 'redirect'),
			event: (0, _utilities.get_and_remove_data)(button, 'event'),
			delay: (0, _utilities.get_and_remove_data)(button, 'delay'),
			url: (0, _utilities.get_and_remove_data)(button, 'url')
		};
	};
	
	_view.Post_Button.prototype.define_events = function (button) {
		var _this = this;
	
		$(button).click((0, _event.event_broker)(function () {
			if (_this._is_not_loading()) {
				_this._set_loading();
	
				_this._set_text_sending().then(function () {
					return _this._set_text_waiting();
				});
	
				_this._send().then(function (response) {
					_this._set_end_loading();
	
					if (_this._is_error(response)) _this._set_text_error();else {
						_this._run_events();
	
						_this._set_text_done().then(function () {
							return _this._set_text_standard();
						});
					}
				});
			}
		}));
	};

/***/ },
/* 43 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Post_Button = undefined;
	
	var _model = __webpack_require__(44);
	
	Object.defineProperty(exports, 'Post_Button', {
		enumerable: true,
		get: function get() {
			return _model.Post_Button;
		}
	});
	
	var _utilities = __webpack_require__(30);
	
	var _standard = __webpack_require__(21);
	
	var if_not_button_text = function if_not_button_text($button) {
		return $button.hasClass('is-icon');
	};
	
	_model.Post_Button.prototype._insert_text = function (text) {
		var $button = $(this._button_data.elem);
	
		if (if_not_button_text($button)) return false;
	
		if ($button.hasClass('is-text_icon')) $button.find('.button-text').html(text);else $button.html(text);
	};
	
	_model.Post_Button.prototype._set_text_sending = function () {
		this._insert_text(this._text_data.sending);
	
		return (0, _standard.timeout_promise)(this._text_data.delay_after_sending);
	};
	
	_model.Post_Button.prototype._set_text_waiting = function () {
		if (this._is_loading()) this._insert_text(this._text_data.waiting);
	};
	
	_model.Post_Button.prototype._set_text_done = function () {
		this._insert_text(this._text_data.done);
	
		return (0, _standard.timeout_promise)(this._text_data.delay_after_done);
	};
	
	_model.Post_Button.prototype._set_text_standard = function () {
		if (this._is_not_loading()) this._insert_text(this._text_data.standard);
	};
	
	_model.Post_Button.prototype._set_text_error = function () {
		this._insert_text(this._text_data.error);
	};
	
	_model.Post_Button.prototype._run_events = function () {
		var events = {
			reload: this._button_data.reload,
			redirect: this._button_data.redirect,
			events: this._button_data.event,
			delay: this._button_data.delay
		};
	
		(0, _utilities.reload_plugins)(events);
		(0, _utilities.redirect_ground)(events);
		(0, _utilities.launch_event)(events);
	};
	
	_model.Post_Button.prototype._send = function () {
		this._prepare_post_data();
	
		return this._send_post();
	};

/***/ },
/* 44 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Post_Button = undefined;
	
	var _init = __webpack_require__(45);
	
	Object.defineProperty(exports, 'Post_Button', {
		enumerable: true,
		get: function get() {
			return _init.Post_Button;
		}
	});
	
	var _main = __webpack_require__(46);
	
	var _standard = __webpack_require__(21);
	
	var _response = __webpack_require__(47);
	
	_init.Post_Button.prototype._is_loading = function () {
		return this._variables.is_loading === true;
	};
	
	_init.Post_Button.prototype._is_not_loading = function () {
		return this._variables.is_loading === false;
	};
	
	_init.Post_Button.prototype._set_loading = function () {
		this._variables.is_loading = true;
	};
	
	_init.Post_Button.prototype._set_end_loading = function () {
		this._variables.is_loading = false;
	};
	
	_init.Post_Button.prototype._is_error = function (response) {
		return (0, _response.recognise_status)(response.code) !== 'success';
	};
	
	_init.Post_Button.prototype._prepare_post_data = function () {
		var data = {},
		    post_name = this._settings.post_name,
		    value = this._button_data.value,
		    action = this._button_data.action,
		    other_1 = this._button_data.other_1,
		    other_2 = this._button_data.other_2,
		    other_3 = this._button_data.other_3;
	
		data[post_name] = 'button';
		data._name_ = action;
	
		if (value) data.value = value;
	
		data.other_1 = other_1 || '';
		data.other_2 = other_2 || '';
		data.other_3 = other_3 || '';
	
		this._settings.post_data = data;
	};
	
	_init.Post_Button.prototype._send_post = function () {
		var _this = this;
	
		return new Promise(function (resolve) {
			(0, _standard.timeout_promise)(200).then(function () {
				var post_url = _this._button_data.url,
				    post_data = _this._settings.post_data,
				    post_name = _this._settings.post_name,
				    request_manager = new _main.Request_Manager_Main();
	
				request_manager.send(post_url, post_data, post_name).then(resolve, resolve);
			});
		});
	};

/***/ },
/* 45 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Post_Button = Post_Button;
	function Post_Button(button, part_name) {
		var dictionary = APP.dictionary;
	
		this._button_data = {
			elem: undefined,
			elem_text: undefined,
			name: undefined,
			action: undefined,
			value: undefined,
			other_1: undefined,
			other_2: undefined,
			other_3: undefined,
			reload: undefined,
			redirect: undefined,
			event: undefined,
			delay: undefined,
			url: undefined
		};
	
		this.collect_data(button);
	
		this._text_data = {
			standard: this._button_data.elem_text,
			sending: dictionary.get_word('Sending...'),
			waiting: dictionary.get_word('Waiting...'),
			done: dictionary.get_word("It's done!"),
			error: dictionary.get_word('Error / Resend'),
	
			delay_after_sending: 500,
			delay_after_done: 1000
		};
	
		this._settings = {
			post_url: this._button_data.url,
			post_name: '__' + part_name + '__',
			post_data: undefined
		};
	
		this._variables = {
			is_loading: false
		};
	
		this._prepare_post_data();
		this.define_events(button);
	}

/***/ },
/* 46 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Request_Manager_Main = Request_Manager_Main;
	
	var _controller = __webpack_require__(18);
	
	function Request_Manager_Main() {
	  _controller.Request_Manager.call(this);
	}
	
	Request_Manager_Main.prototype = Object.create(_controller.Request_Manager.prototype);

/***/ },
/* 47 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var recognise_status = exports.recognise_status = function recognise_status(code) {
		if (code >= 200 && code < 300) return 'success';
	
		if (code >= 300 && code < 400) return 'redirect';
	
		return 'error';
	};

/***/ },
/* 48 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Form_Models = Dialog_Form_Models;
	
	var _model = __webpack_require__(29);
	
	var _dialog_form = __webpack_require__(49);
	
	function Dialog_Form_Models(config) {
		_model.Form_Models.call(this, config);
	
		this._dialog_form_loader = new _dialog_form.Block_Loader_Dialog_Form(config);
	}
	
	Dialog_Form_Models.prototype = Object.create(_model.Form_Models.prototype);
	
	Dialog_Form_Models.prototype.send = function () {
		var post_url = this.variables.post_url,
		    post_data = this.variables.post_data;
	
		this._prepare_post_data();
	
		this._dialog_form_loader.load_content(post_url, post_data).then(this._end_loading);
	};

/***/ },
/* 49 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Loader_Dialog_Form = Block_Loader_Dialog_Form;
	
	var _dialog = __webpack_require__(50);
	
	function Block_Loader_Dialog_Form(config) {
		_dialog.Block_Loader_Dialog.call(this, config);
	}
	
	Block_Loader_Dialog_Form.prototype = Object.create(_dialog.Block_Loader_Dialog.prototype);
	
	Block_Loader_Dialog_Form.prototype._prepare_post_data = function (post_data) {
		if (!post_data) post_data = {};
	
		post_data[this._settings.post_name] = 'form';
	
		this._variables.post_data = post_data;
	};

/***/ },
/* 50 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Block_Loader_Dialog = Block_Loader_Dialog;
	
	var _response = __webpack_require__(47);
	
	var _data = __webpack_require__(16);
	
	var _main = __webpack_require__(46);
	
	var _controller = __webpack_require__(19);
	
	function Block_Loader_Dialog(config) {
		_controller.Block_Loader.call(this, config);
	}
	
	Block_Loader_Dialog.prototype = Object.create(_controller.Block_Loader.prototype);
	
	Block_Loader_Dialog.prototype._send_request = function () {
		var post_data = this._variables.post_data,
		    post_name = this._settings.post_name,
		    request_manager = new _main.Request_Manager_Main();
	
		this._response = request_manager.send(undefined, post_data, post_name);
	};
	
	Block_Loader_Dialog.prototype._close_dialog_if_no_content = function (response) {
		if ((0, _response.recognise_status)(response.code) === 'success' && (0, _data.is_empty)(response.html)) {
			APP.DATA.delay = 0;
			APP.throw_event(EVENTS.part.close_dialog);
			return true;
		}
	
		return false;
	};
	
	Block_Loader_Dialog.prototype.load_content = function (post_url, post_data) {
		var _this = this;
	
		return new Promise(function (resolve) {
			_this._get_content(post_url, post_data);
	
			_this._hide_content().then(function () {
				_this._receive_response().then(function (response) {
					if (_this._close_dialog_if_no_content(response)) resolve(response);
	
					_this._set_content(response);
	
					_this._prepare_content_to_show(response);
	
					_this._show_content().then(function () {
						resolve(response);
					});
				});
			});
		});
	};
	
	Block_Loader_Dialog.prototype.define = function () {};

/***/ },
/* 51 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define = undefined;
	
	var _checkers = __webpack_require__(52);
	
	var Validators = {};
	
	window.Validators = Validators;
	
	var define = exports.define = function define(config) {
	
		$('form[data-test=yes]', config.$container).each(function () {
			var name = $(this).data('name'),
			    type = $(this).data('type'),
			    post_name = config.post_name;
	
			if ((name || type) && post_name) {
				Validators[name] = new _checkers.Constructor_Validator(name, type, post_name);
	
				var fields_of_form = Validators[name].hasErrors();
				for (var key in fields_of_form) {
					if (fields_of_form.hasOwnProperty(key)) {
						var $field = $('form[data-name=' + name + '] *[name=' + key + ']');
	
						if ($field.val()) validate($field);
					}
				}
			} else console.error('Validation Error: Incorrect or empty form name/type.');
		});
	
		$('form[data-test=yes] .test', config.$container).keyup(catch_event_validate).change(catch_event_validate).focusout(catch_event_validate);
	
		$('.show_password-checkbox', config.$container).change(function () {
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
			    $status = $field.parent().find('.status'),
			    $status_external = $field.parent().find('.status-external');
	
			var bool = result.bool,
			    message = result.message,
			    correction = result.correction;
	
			Validator.change_status_field(field_name, bool);
	
			if ($field.val() != correction && typeof correction !== 'undefined' && correction !== '') $field.val(correction);
	
			if (bool) {
				$field.removeClass('form_error');
				$status.html('');
			} else if (typeof message === 'undefined') {
				$field.addClass('form_error');
				$status.html('');
			} else {
				$field.addClass('form_error');
				$status.html(message);
				$status_external.html('');
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
/* 52 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Constructor_Validator = undefined;
	
	var _views = __webpack_require__(53);
	
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
	
	_views.checker.create_checker('email_no_in_db', function (value, callback, post_name) {
		var result = _views.checker.create_result(),
		    re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	
		if (_views.checker.check_condition(re.test(value))) {
			result = _views.checker.create_error('It\'s not email.');
			callback(result);
		} else {
			_views.checker.run_if_no_in_db('email', value, callback, post_name, 'Someone already has that email. Try another?');
		}
	});
	
	_views.checker.create_checker('email_in_db', function (value, callback, post_name) {
		var result = _views.checker.create_result(),
		    re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	
		if (_views.checker.check_condition(re.test(value))) {
			result = _views.checker.create_error('It\'s not email.');
			callback(result);
		} else {
			_views.checker.run_if_in_db('email', value, callback, post_name, 'We don\'t know this email.');
		}
	});
	
	_views.checker.create_checker('password', function (value, callback) {
		var result = _views.checker.create_result();
	
		if (_views.checker.check_condition(value.length >= 8)) result = _views.checker.create_error('Short passwords are easy to guess. Try one with at least 8 characters.');
	
		callback(result);
	});
	
	_views.checker.create_checker('safety_password', function (value, callback, post_name) {
		var result = _views.checker.create_result();
	
		if (_views.checker.check_condition(value.length >= 8)) {
			result = _views.checker.create_error('Short passwords are easy to guess. Try one with at least 8 characters.');
			callback(result);
		} else _views.checker.run_if_no_in_db('password', value, callback, post_name, 'This password is not safety. Try another?');
	});
	
	_views.checker.create_checker('password_login', function (value, callback) {
		var result = _views.checker.create_result();
	
		if (_views.checker.check_condition(value.length >= 8)) result = _views.checker.create_error('The password must be 8 characters long.');
	
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
/* 53 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Constructor_Validator = exports.checker = undefined;
	
	var _config = __webpack_require__(54);
	
	var _controller = __webpack_require__(18);
	
	var request_manager = new _controller.Request_Manager();
	
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
	
		run_if_in_db: function run_if_in_db(name, value, callback, post_name, message) {
			if (name && value) {
				(function () {
					var run_error = function run_error() {
						console.error('Something is wrong.');
						callback(checker.create_error('Validator, don\' work. Please, refresh website.'));
					},
					    post_data = {};
	
					post_data[post_name] = 'exist';
					post_data['_name_'] = name;
					post_data['value'] = value;
	
					request_manager.send(undefined, post_data, post_name).then(function (data) {
						if (data.html !== 'undefined') {
							if (data.html === 'false') callback(checker.create_error(message));else if (data.html === 'true') callback(checker.create_result());
						} else {
							run_error();
						}
					}, run_error);
				})();
			}
		},
	
		run_if_no_in_db: function run_if_no_in_db(name, value, callback, post_name, message) {
			if (name && value) {
				(function () {
					var run_error = function run_error() {
						console.error('Something is wrong.');
						callback(checker.create_error('Validator, don\' work. Please, refresh website.'));
					},
					    post_data = {};
	
					post_data[post_name] = 'exist';
					post_data['_name_'] = name;
					post_data['value'] = value;
	
					request_manager.send(undefined, post_data, post_name).then(function (data) {
						if (data.html !== 'undefined') {
							if (data.html === 'true') callback(checker.create_error(message));else if (data.html === 'false') callback(checker.create_result());
						} else {
							run_error();
						}
					}, run_error);
				})();
			}
		}
	};
	
	var Constructor_Validator = exports.Constructor_Validator = function Constructor_Validator(form_name, form_type, post_name) {
	
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
	
				_checker.validate(value, callback, post_name);
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
/* 54 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var list_configs = exports.list_configs = {};
	
	list_configs.register = {
		email: 'email_no_in_db',
		username: 'length_3',
		phone: 'length_3',
		password: 'safety_password'
	};
	
	list_configs.login = {
		email: 'email',
		password: 'password_login'
	};
	
	list_configs.user_address = {
		name: 'proper_name',
		surname: 'proper_name',
		address_line: 'no_empty',
		city: 'proper_name',
		region: 'proper_name',
		postcode: 'no_empty',
		country: 'proper_name'
	};
	
	list_configs.root_address = {
		name: 'proper_name',
		surname: 'proper_name',
		address_line: 'no_empty',
		city: 'proper_name',
		region: 'proper_name',
		postcode: 'no_empty',
		country: 'proper_name',
		email: 'email'
	};
	
	list_configs.shop_address = {
		name: 'proper_name',
		surname: 'proper_name',
		address_line: 'no_empty',
		city: 'proper_name',
		region: 'proper_name',
		postcode: 'no_empty',
		country: 'proper_name',
		email: 'email'
	};
	
	list_configs.forgot_password = {
		email: 'email_in_db'
	};
	
	list_configs.change_password = {
		password: 'safety_password'
	};
	
	list_configs.email_contact = {
		client: 'proper_name',
		email: 'email',
		message: 'no_empty'
	};

/***/ },
/* 55 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define = undefined;
	
	var _views = __webpack_require__(56);
	
	var add_event_on_fields = function add_event_on_fields(auto_form_views) {
		var settings = auto_form_views.models.settings,
		    $field = void 0;
	
		settings.fields.each(function () {
			$field = $(this);
	
			if ($field.is(':checkbox')) $field.change(auto_form_views.send_checkbox);else if ($field.is(':text')) {
				if ($field.hasClass('only_enter')) $field.keydown(auto_form_views.send_on_enter);else {
					if ($field.hasClass('always')) $field.keyup(auto_form_views.send_if_number_only);
	
					if ($field.hasClass('only_number_3')) $field.keydown(auto_form_views.try_press_number_max_3);
	
					if ($field.hasClass('searcher_field')) $field.keydown(auto_form_views.send_for_searcher);else $field.change(auto_form_views.send_default).keydown(auto_form_views.send_on_enter);
				}
			} else $field.change(auto_form_views.send_default);
		});
	},
	    do_nothing = function do_nothing(event) {
		event.preventDefault();
		return false;
	};
	
	var define = exports.define = function define(config) {
		var $container = config.$container,
		    $forms = $('form.auto_form, .auto_form form', $container);
	
		$forms.each(function () {
			var $form = $(this),
			    config_form = {
				form: $form,
				fields: $('.auto_field', $form),
				post_name: config.post_name
			},
			    auto_form_views = new _views.Auto_Form_Views(config_form);
	
			$form.submit(do_nothing);
			add_event_on_fields(auto_form_views);
		});
	};

/***/ },
/* 56 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Auto_Form_Views = undefined;
	
	var _response = __webpack_require__(47);
	
	var _utilities = __webpack_require__(30);
	
	var _models = __webpack_require__(57);
	
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
				    other_1 = $field.data('other_1'),
				    other_2 = $field.data('other_2'),
				    other_3 = $field.data('other_3'),
				    value = $field.val();
	
				that.send_default(name, value, other_1, other_2, other_3);
			}
		};
	
		var check_is_key_code_enter = function check_is_key_code_enter(event) {
			return event.keyCode === 13;
		};
	
		this.send_checkbox = function () {
			var $field = $(this),
			    name = $field.attr('name'),
			    value = $field.val(),
			    action = void 0;
	
			if ($field.is(':checked')) action = 'append';else action = 'delete';
	
			models.prepare_post_data(name, value, action);
	
			send();
		};
	
		this.send_default = function (name, value, other_1, other_2, other_3) {
			if (name && value) {
				models.prepare_post_data(name, value, undefined, undefined, other_1, other_2, other_3);
			} else {
				var $field = $(this),
				    _name = $field.data('name'),
				    _other_ = $field.data('other_1'),
				    _other_2 = $field.data('other_2'),
				    _other_3 = $field.data('other_3'),
				    _value = $field.val(),
				    field = $field.attr('name');
	
				models.prepare_post_data(_name, _value, undefined, field, _other_, _other_2, _other_3);
			}
	
			send();
		};
	
		this.send_for_searcher = function (name, value, other_1, other_2, other_3) {
			if (name && value) {
				models.prepare_post_data(name, value, undefined, undefined, other_1, other_2, other_3);
			} else {
				var $field = $(this),
				    _name2 = $field.attr('name'),
				    _other_4 = $field.data('other_1'),
				    _other_5 = $field.data('other_2'),
				    _other_6 = $field.data('other_3'),
				    _value2 = $field.val();
	
				models.prepare_post_data(_name2, _value2, undefined, undefined, _other_4, _other_5, _other_6);
			}
	
			send();
		};
	
		this.send_on_enter = function (event) {
			if (check_is_key_code_enter(event)) {
				event.preventDefault();
				var $field = $(this),
				    name = $field.attr('name'),
				    other_1 = $field.data('other_1'),
				    other_2 = $field.data('other_2'),
				    other_3 = $field.data('other_3'),
				    value = $field.val();
	
				models.prepare_post_data(name, value, undefined, undefined, other_1, other_2, other_3);
	
				send();
			}
		};
	
		var show_changes = function show_changes() {
			var delay = void 0,
			    function_for_setTimeout = function function_for_setTimeout() {
				if (models.get_state_response() && models.get_state_error() === false) {
	
					(0, _utilities.reload_plugins)(models.settings);
					(0, _utilities.redirect_ground)(models.settings);
					(0, _utilities.launch_event)(models.settings);
				} else if (models.get_state_error()) {
					return false;
				} else {
					sent_http_request = setTimeout(function_for_setTimeout, 100);
				}
			};
	
			if (typeof models.settings.delay !== 'undefined') delay = models.settings.delay;else delay = 0;
	
			clearTimeout(sent_http_request);
			sent_http_request = setTimeout(function_for_setTimeout, delay);
		},
		    is_error = function is_error(code) {
			return (0, _response.recognise_status)(code) === 'error';
		},
		    set_response = function set_response(response) {
			if (is_error(response.code)) {
				models.set_state_error(true);
				models.set_state_response(false);
				return false;
			}
	
			models.set_state_error(false);
			models.set_state_response(true);
		},
		    send = function send() {
			models.send().then(function (response) {
				set_response(response);
			});
			show_changes();
		};
	};

/***/ },
/* 57 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Auto_Form_Models = undefined;
	
	var _main = __webpack_require__(46);
	
	var _data = __webpack_require__(16);
	
	var Auto_Form_Models = exports.Auto_Form_Models = function Auto_Form_Models(config) {
		var _this = this;
	
		var request_manager = new _main.Request_Manager_Main();
	
		this.settings = {
			post_name: undefined,
	
			form: undefined,
			fields: undefined,
	
			origin: undefined,
			redirect: undefined,
			reload: undefined,
			event: undefined,
			delay: undefined
		};
	
		var variables = {
			post_data: {}
		},
		    state = {
			response: false,
			error: false
		},
		    load_settings = function load_settings() {
			if (typeof config !== 'undefined') {
				if (typeof config.form !== 'undefined') {
					_this.settings.post_name = config.post_name;
					_this.settings.form = config.form;
	
					var $form = _this.settings.form;
					_this.settings.origin = $form.data('origin');
					_this.settings.redirect = $form.data('redirect');
					_this.settings.reload = $form.data('reload');
					_this.settings.event = $form.data('event');
					_this.settings.delay = $form.data('delay');
				}
	
				if (typeof config.fields !== 'undefined') _this.settings.fields = config.fields;
			}
		};
	
		load_settings();
	
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
	
		this.prepare_post_data = function (name, value, action, field, other_1, other_2, other_3) {
			variables.post_data = {};
	
			variables.post_data[this.settings.post_name] = this.settings.origin;
			variables.post_data._name_ = name;
			variables.post_data.value = value;
			variables.post_data.other_1 = other_1;
			variables.post_data.other_2 = other_2;
			variables.post_data.other_3 = other_3;
	
			if ((0, _data.is_defined)(action)) variables.post_data.action = action;
	
			if ((0, _data.is_defined)(field)) variables.post_data.field = field;
		};
	
		this.send = function () {
			this.set_state_response(false);
	
			return request_manager.send(undefined, variables.post_data, this.settings.post_name);
		};
	};

/***/ },
/* 58 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Selected_Form_Controller = Selected_Form_Controller;
	function Selected_Form_Controller(config) {
		if (!config || !config.container) {
			console.error('Part Loader error: Invalid configuration.');
			return {};
		}
	
		var $container = config.container,
		    change_fields = function change_fields(select_choice) {
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
	
		this.define = function () {
			$('.selected_form-choice', $container).change(change_form);
		};
	}

/***/ },
/* 59 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	var Feature_Setter = exports.Feature_Setter = function Feature_Setter(config) {
		if (typeof config === 'undefined' && typeof config.container === 'undefined') {
			console.error('Exeption error: invalid container.');
			return {};
		}
	
		var get_setters = function get_setters($setter) {
			var $form = $setter.parents('form'),
			    name = $setter.attr('name');
	
			return $('.if_feature[name=' + name + ']', $form);
		},
		    set_feature = function set_feature() {
			var $setter = $(this),
			    id = $setter.data('id'),
			    $elem_id = $('.set_feature[data-id=' + id + ']', config.container),
			    feature = $elem_id.data('feature');
	
			$elem_id.prop(feature, true);
		},
		    change_input_status = function change_input_status() {
			var $setter = $(this),
			    id = $setter.data('id'),
			    type = $setter.attr('type'),
			    status = $setter.is(':checked') === false,
			    $all_setters = get_setters($setter),
			    $elem_id = $('.set_feature[data-id=' + id + ']', config.container),
			    feature = $elem_id.data('feature');
	
			if (type === 'radio') $all_setters.each(set_feature);
	
			$elem_id.prop(feature, status);
		};
	
		this.define = function () {
			var $all_setters = $('.if_feature', config.container);
	
			$all_setters.each(set_feature);
	
			$all_setters.click(change_input_status);
		};
	};

/***/ },
/* 60 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define = undefined;
	
	var _views = __webpack_require__(61);
	
	var image_convert_views = _interopRequireWildcard(_views);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	var define = exports.define = function define(config) {
		var views = image_convert_views,
		    settings = views.models.settings,
		    $forms = $(settings.form, config.$container),
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
/* 61 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Callback_Functions = exports.get_base64 = exports.settings = exports.models = undefined;
	
	var _models = __webpack_require__(62);
	
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
/* 62 */
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
/* 63 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Address_Switcher_Controller = Address_Switcher_Controller;
	
	var _main = __webpack_require__(64);
	
	function Address_Switcher_Controller(config) {
		if (!config || !config.container) {
			console.error('Part Loader error: Invalid configuration.');
			return {};
		}
	
		this.container = config.container;
	
		var add_switcher = function add_switcher() {
			new _main.Address_Switcher(this);
		};
	
		this.define = function () {
			$('.form-address_switcher', this.container).each(add_switcher);
		};
	}

/***/ },
/* 64 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Address_Switcher = Address_Switcher;
	function Address_Switcher(button) {
		var $button = $(button),
		    new_address = $button.data('address'),
		    $form = $button.parents('form'),
		    receive_event = function receive_event() {
			var old_address = $form.attr('action');
	
			$form.data('reload', 'cart');
			$form.data('event', 'part.open_cart');
			$form.attr('action', new_address);
			$form.submit();
			$form.attr('action', old_address);
			$form.data('reload', '');
			$form.data('event', '');
		};
	
		$(button).click(receive_event);
	}

/***/ },
/* 65 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Currency_Converter_Controller = Currency_Converter_Controller;
	
	var _model = __webpack_require__(66);
	
	var model = _interopRequireWildcard(_model);
	
	var _event = __webpack_require__(10);
	
	var _view = __webpack_require__(67);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	function Currency_Converter_Controller(config) {
		if (!config || !config.container) {
			console.error('Part Loader error: Invalid configuration.');
			return {};
		}
	
		var container = config.container,
		    view = new _view.Currency_Converter_View();
	
		this.define = function () {
			$(model.selector.input, container).each((0, _event.event_broker)(view.change_status_field));
	
			$(model.selector.button, container).click((0, _event.event_broker)(view.calculate));
		};
	}

/***/ },
/* 66 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.get_price = exports.selector = undefined;
	
	var _controller = __webpack_require__(18);
	
	var request_manager = new _controller.Request_Manager(),
	    prepare_currencies = function prepare_currencies(list) {
		var text = '';
	
		for (var i = 0; list.length > i; ++i) {
			if (i === 0) text += list[i];else text += ' ' + list[i];
		}
	
		return text;
	},
	    receive_data = function receive_data(resolve) {
		return function (response) {
			var list = JSON.parse(response.html),
			    array = [];
	
			if (typeof list.EUR !== 'undefined') array.push({
				currency: 'EUR',
				price: list.EUR
			});
			if (typeof list.PLN !== 'undefined') array.push({
				currency: 'PLN',
				price: list.PLN
			});
			if (typeof list.GBP !== 'undefined') array.push({
				currency: 'GBP',
				price: list.GBP
			});
	
			resolve(array);
		};
	};
	
	var selector = exports.selector = {
		container: '.currency_converter',
		column: '.currency_converter-col',
		checkbox: '.currency_converter-checkbox',
		input: '.currency_converter-field',
		button: '.currency_converter-button'
	},
	    get_price = exports.get_price = function get_price(url, base_price, base_currency, list_of_currencies) {
		return new Promise(function (resolve) {
			var content = '__ground__',
			    data = {
				__ground__: 'get',
				_name_: 'exchange_rate',
				amount: base_price,
				currency_from: base_currency,
				currencies_to: prepare_currencies(list_of_currencies)
			};
	
			request_manager.send(url, data, content).then(receive_data(resolve));
		});
	};

/***/ },
/* 67 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Currency_Converter_View = Currency_Converter_View;
	
	var _model = __webpack_require__(66);
	
	var model = _interopRequireWildcard(_model);
	
	function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }
	
	function Currency_Converter_View() {
		this.change_status_field = function (input) {
			var $input = $(input),
			    $column = $input.parents(model.selector.column),
			    $button = $(model.selector.button, $column);
	
			if ($column.data('currency') === 'EUR' || $column.data('currency') === 'GBP') {
				$input.prop('disabled', true);
				$button.prop('disabled', true);
			}
		};
	
		this.calculate = function (button) {
			var $button = $(button),
			    $column = $button.parents(model.selector.column),
			    $container = $column.parents(model.selector.container),
			    $input = $(model.selector.input, $column),
			    base_price = $input.val(),
			    base_currency = $column.data('currency'),
			    url = $container.data('url'),
			    $all_columns = $(model.selector.column, $container),
			    list_of_currencies = [];
	
			$all_columns.each(function () {
				var currency = $(this).data('currency');
	
				if (base_currency !== currency) list_of_currencies.push(currency);
			});
	
			if (base_price && base_currency && list_of_currencies) model.get_price(url, base_price, base_currency, list_of_currencies).then(function (array) {
				for (var i = 0; array.length > i; ++i) {
					var currency = array[i].currency,
					    price = array[i].price,
					    $input_for_setting = $(model.selector.input, model.selector.column + '[data-currency=' + currency + ']');
	
					$input_for_setting.val(price);
				}
			});
		};
	}

/***/ },
/* 68 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.define_directory_tree = undefined;
	
	var _controller = __webpack_require__(69);
	
	var define_directory_tree = exports.define_directory_tree = function define_directory_tree(config) {
		var $element = $('.directory_tree', config.container);
	
		$element.each(function () {
			new _controller.Directory_Tree(this);
		});
	};

/***/ },
/* 69 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Directory_Tree = Directory_Tree;
	function Directory_Tree(container) {
		if (!container) {
			console.error('Part Loader error: Invalid configuration.');
			return {};
		}
	
		this.container = container;
	
		var change_state = function change_state() {
			var $parent = $(this).parent().parent(),
			    $arrow = $parent.children('.directory_tree-single').children('.directory_tree-name').children('.directory_tree-arrow'),
			    $list = $parent.children('.directory_tree-list'),
			    $all_lists = $parent.find('.directory_tree-list'),
			    is_open = $list.hasClass('is-open');
	
			if (is_open) {
				if ($arrow.hasClass('is-open')) $arrow.removeClass('is-open').addClass('is-close');
				$all_lists.removeClass('is-open').addClass('is-close');
			} else {
				if ($arrow.hasClass('is-close')) $arrow.removeClass('is-close').addClass('is-open');
				$list.removeClass('is-close').addClass('is-open');
			}
		};
	
		this.define = function () {
			$('.directory_tree-name', this.container).click(change_state);
		};
	
		this.define();
	}

/***/ },
/* 70 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Cart_Controller = Cart_Controller;
	
	var _block = __webpack_require__(12);
	
	var _controller = __webpack_require__(25);
	
	var _controller2 = __webpack_require__(28);
	
	var _define = __webpack_require__(41);
	
	var _define2 = __webpack_require__(36);
	
	function Cart_Controller() {
		var _this = this;
	
		if (_typeof(Cart_Controller.instance) === 'object') return Cart_Controller.instance;
	
		Cart_Controller.instance = this;
	
		var container_id = '#CART',
		    container = '.cart',
		    part_name = 'cart',
		    config_loader = {
			part_name: part_name,
			container: container
		},
		    cart_loader = new _block.Block_Loader_Part(config_loader),
		    cart_motion_controller = new _controller.Block_Motion_Controllers({
			container: container_id,
			content: container,
			open: 'left',
			can_open_by: 'width',
			can_open_from: 0,
			duration_open: 200,
			duration_close: 200
		}),
		    cart_form_controller = new _controller2.Form_Controllers(config_loader),
		    manage_key = function manage_key(event) {
			if (event.keyCode === 27) cart_motion_controller.plugin_close();
	
			if (event.ctrlKey && event.shiftKey && event.keyCode === 88) {
				event.preventDefault();
				if (cart_motion_controller.is_open()) cart_motion_controller.plugin_close();else cart_motion_controller.plugin_open();
			}
		};
	
		this.plugin_open = function () {
			return cart_motion_controller.plugin_open();
		};
	
		this.plugin_close = function () {
			return cart_motion_controller.plugin_close();
		};
	
		this.open_or_close = function () {
			APP.throw_event(EVENTS.part.close_menu_mobile);
	
			if (cart_motion_controller.is_open()) _this.plugin_close();else _this.plugin_open();
		};
	
		this.reload = function () {
			_this.plugin_open();
		};
	
		this.define = function () {
			APP.add_own_event('cart_open', _this.plugin_open);
			APP.add_own_event('cart_close', _this.plugin_close);
			APP.add_own_event('cart_open_or_close', _this.open_or_close);
	
			$('body').keydown(manage_key);
	
			cart_form_controller.define();
			cart_motion_controller.define();
			(0, _define2.define_event_button)({
				container: container_id
			});
			(0, _define.define_post_button)(config_loader);
		};
	
		this.get_content = function () {
			cart_loader.define();
			cart_loader.load_content();
			cart_motion_controller.set_start_position();
		};
	}

/***/ },
/* 71 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Menu_Mobile_Controller = Menu_Mobile_Controller;
	
	var _block = __webpack_require__(12);
	
	var _controller = __webpack_require__(25);
	
	var _define = __webpack_require__(36);
	
	function Menu_Mobile_Controller() {
		if (_typeof(Menu_Mobile_Controller.instance) === 'object') return Menu_Mobile_Controller.instance;
	
		Menu_Mobile_Controller.instance = this;
	
		var container_id = '#MENU_MOBILE',
		    container = '.menu_mobile',
		    part_name = 'menu_mobile',
		    loader = new _block.Block_Loader_Part({
			part_name: part_name,
			container: container
		}),
		    motion_controller = new _controller.Block_Motion_Controllers({
			container: container_id,
			content: container,
			open: 'down',
	
			can_open_by: 'width',
			can_open_to: 675,
	
			duration_open: 300,
			duration_close: 150
		});
	
		this.plugin_open = function () {
			motion_controller.plugin_open();
		};
	
		this.define = function () {
			APP.add_own_event(part_name + '_close', motion_controller.plugin_close);
			APP.add_own_event(part_name + '_open', motion_controller.plugin_open);
	
			motion_controller.define();
			(0, _define.define_event_button)({
				container: container_id
			});
		};
	
		this.get_content = function () {
			loader.define();
			loader.load_content();
	
			motion_controller.set_start_position();
		};
	}

/***/ },
/* 72 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	
	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };
	
	exports.Dialog_Controller = Dialog_Controller;
	
	var _controller = __webpack_require__(73);
	
	var _controller2 = __webpack_require__(75);
	
	function Dialog_Controller() {
		if (_typeof(Dialog_Controller.instance) === 'object') return Dialog_Controller.instance;
	
		Dialog_Controller.instance = this;
	
		var config = {
			part_name: 'dialog',
			html_id: '#DIALOG',
			container: '.dialog',
			header: '.dialog-header',
			content: '.dialog-content',
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
				loading.then(function () {
					designer.unset_loading();
				});
			});
		},
		    close = function close() {
			designer.close().then(loader.set_loading);
		},
		    close_with_cancel_event = function close_with_cancel_event() {
			designer.close_with_cancel_event(event).then(loader.set_loading);
		},
		    open = function open() {
			var loading = loader.get_content(this);
	
			designer.open().then(function () {});
		},
		    open_with_error = function open_with_error(event) {
			var title = event.detail.title,
			    content = event.detail.content,
			    code = event.detail.code;
	
			content = '<span class="is-bold"> Error content: </span>' + content + '<br>' + '<span class="is-bold"> Error code: </span>' + code;
	
			designer.open().then(function () {
				loader.set_error({
					title: title,
					content: content
				});
			});
		},
		    open_with_my_text = function open_with_my_text(event) {
			var title = event.detail.title,
			    content = event.detail.content;
	
			designer.open().then(function () {
				loader.set_text({
					title: title,
					content: content
				});
			});
		};
	
		this.define = function () {
			designer.define();
			loader.define();
	
			$(config.html_id).click(close_with_cancel_event);
			$(config.external_button).click(open);
			APP.add_own_event('dialog_close', close);
			APP.add_own_event('dialog_reload', reload);
			APP.add_own_event('open_dialog_error', open_with_error);
			APP.add_own_event('open_dialog_with_text', open_with_my_text);
		};
	}

/***/ },
/* 73 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Designer_Controller = Dialog_Designer_Controller;
	
	var _standard = __webpack_require__(21);
	
	var _view = __webpack_require__(74);
	
	function Dialog_Designer_Controller(config) {
		var _this = this;
	
		var view = new _view.Dialog_Designer_View(config),
		    cancel_event = function cancel_event(event) {
			event.stopPropagation();
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
	
		this.close_with_cancel_event = function (event) {
			cancel_event(event);
			return _this.close();
		};
	
		this.open = function () {
			return view.show();
		};
	
		this.define = function () {
			$(view.selector.window).click(cancel_event);
		};
	}

/***/ },
/* 74 */
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
/* 75 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Loader_Controller = Dialog_Loader_Controller;
	
	var _controller = __webpack_require__(28);
	
	var _define = __webpack_require__(41);
	
	var _define2 = __webpack_require__(36);
	
	var _controllers = __webpack_require__(76);
	
	var _define3 = __webpack_require__(68);
	
	var _controller2 = __webpack_require__(79);
	
	var _view = __webpack_require__(82);
	
	function Dialog_Loader_Controller(config) {
		var config_loader = {
			part_name: config.part_name,
			container: config.container
		},
		    view = new _view.Dialog_Loader_View(config),
		    form_controller = new _controller.Form_Controllers(config_loader, true),
		    little_form_controller = new _controllers.Little_Form_Controllers(config_loader),
		    notifications_controller = new _controller2.Notifications_Controller(config_loader);
	
		this.reload_content = function () {
			return view.send_request();
		};
	
		this.get_content = function (button) {
			return new Promise(function (resolve) {
				view.collect_data(button);
	
				view.send_request().then(resolve);
			});
		};
	
		this.set_loading = function () {
			view.set_text({
				title: '<div class="container-part-loading"> Loading... </div>',
				content: '<div class="dialog-message"> Loading... </div>'
			});
		};
	
		this.set_text = function (data) {
			data.content = '<div class="dialog-content-part">' + data.content + '</div>' + '<div class="dialog-content-part">' + '<button class="button event_button"' + 'type="button"' + 'data-name="button_close_dialog"' + 'data-event="part.close_dialog">' + 'Close</button>' + '</div>';
	
			view.set_text(data);
			this.define();
		};
	
		this.set_error = function (data) {
			data.content = '<div class="dialog-content-part">' + data.content + '</div>' + '<div class="dialog-content-part">' + '<button class="button event_button"' + 'type="button"' + 'data-name="redirect_website_error"' + 'data-event="redirect_website(url:/,uri:/)">' + 'Redirect to home</button>' + '<button class="button event_button"' + 'type="button"' + 'data-name="reaload_website_error"' + 'data-event="reload_website">' + 'Reload page</button>' + '<button class="button event_button"' + 'type="button"' + 'data-name="button_close_dialog"' + 'data-event="part.close_dialog">' + 'Close</button>' + '</div>';
	
			view.set_text(data);
			this.define();
		};
	
		this.define = function () {
			form_controller.define();
			(0, _define.define_post_button)(config_loader);
			(0, _define2.define_event_button)(config_loader);
			(0, _define3.define_directory_tree)(config_loader);
			little_form_controller.define();
			notifications_controller.define();
	
			$(config.internal_button, config.container).click(view.send_form);
		};
	}

/***/ },
/* 76 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Little_Form_Controllers = undefined;
	
	var _views = __webpack_require__(77);
	
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
/* 77 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	exports.Little_Form_Views = undefined;
	
	var _models = __webpack_require__(78);
	
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
/* 78 */
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
/* 79 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Notifications_Controller = Notifications_Controller;
	
	var _view = __webpack_require__(80);
	
	function Notifications_Controller(config) {
		if (!config || !config.container) {
			console.error('Part Loader error: Invalid configuration.');
			return {};
		}
	
		var container = config.container,
		    view = new _view.Notifications_View(),
		    model = view.model,
		    updata_list_notifications = function updata_list_notifications() {
			view.get_list(this).then(view.set_list);
		};
	
		this.define = function () {
			$(model.selector.list, container).each(updata_list_notifications);
	
			$(model.selector.show_more_button, container).click(updata_list_notifications);
		};
	}

/***/ },
/* 80 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Notifications_View = Notifications_View;
	
	var _model = __webpack_require__(81);
	
	function Notifications_View() {
		var model = void 0,
		    $list_notifications = void 0;
	
		this.model = new _model.Notifications_Model();
		model = this.model;
	
		this.set_list = function (response) {
			var html = model.receive_response(response);
	
			$list_notifications.children(model.selector.message).remove();
			$list_notifications.append(html);
		};
	
		this.get_list = function (button) {
			var $button = $(button),
			    $container = $button.parents(model.selector.container),
			    $list = $container.find(model.selector.list),
			    $last_notification = $list.children(model.selector.single).last(),
			    pk = $last_notification.data('pk');
	
			$list_notifications = $list;
	
			model.prepare_post_data(pk);
	
			return model.get_ten_notifications();
		};
	}

/***/ },
/* 81 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Notifications_Model = Notifications_Model;
	
	var _main = __webpack_require__(46);
	
	function Notifications_Model() {
		var request_manager = new _main.Request_Manager_Main(),
		    variable = {
			post_url: '/notification/',
			post_data: undefined,
			post_name: '__ground__'
		};
	
		this.selector = {
			container: '.notifications',
			list: '.notifications-list',
			message: '.dialog-message',
			single: '.notifications-single',
			show_more_button: '.notifications-show_more-button'
		};
	
		this.prepare_post_data = function (pk) {
			if (!pk) pk = '';
	
			variable.post_data = {
				_name_: 'ten_notifications',
				last_notification_pk: pk
			};
	
			variable.post_data[variable.post_name] = 'get';
		};
	
		this.receive_response = function (response) {
			if (response && response.html) return response.html;
		};
	
		this.get_ten_notifications = function () {
			return request_manager.send(variable.post_url, variable.post_data, variable.post_name);
		};
	}

/***/ },
/* 82 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Loader_View = Dialog_Loader_View;
	
	var _model = __webpack_require__(83);
	
	function Dialog_Loader_View(config) {
		var model = new _model.Dialog_Loader_Model(config);
	
		this.collect_data = function (button) {
			var $button = $(button);
	
			model.variable.post_data = {
				_type_: $button.data('type'),
				_name_: $button.data('name'),
				value: $button.data('value'),
				other_1: $button.data('other_1'),
				other_2: $button.data('other_2'),
				other_3: $button.data('other_3'),
	
				accept_name: $button.data('dialog-name'),
				accept_action: $button.data('dialog-action'),
				accept_value: $button.data('dialog-value'),
				accept_reload: $button.data('dialog-reload'),
				accept_redirect: $button.data('dialog-redirect'),
				accept_event: $button.data('dialog-event'),
				accept_url: $button.data('dialog-url'),
	
				accept_other_1: $button.data('dialog-other_1'),
				accept_other_2: $button.data('dialog-other_2'),
				accept_other_3: $button.data('dialog-other_3')
			};
		};
	
		this.send_request = function () {
			model.prepare_post_data();
	
			return model.send_request();
		};
	
		this.send_form = function () {
			$(config.form, config.container).submit();
		};
	
		this.set_text = function (data) {
			$(model.settings.header).html(data.title);
			$(model.settings.content).html(data.content);
		};
	}

/***/ },
/* 83 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
		value: true
	});
	exports.Dialog_Loader_Model = Dialog_Loader_Model;
	
	var _dialog = __webpack_require__(50);
	
	function Dialog_Loader_Model(config) {
	
		var part_dialog_loader = new _dialog.Block_Loader_Dialog(config);
	
		this.settings = {
			header: config.header,
			content: config.content
		};
	
		this.variable = {
			post_data: undefined,
			response: undefined
		};
	
		this.prepare_post_data = function () {
			var new_post_data = {},
			    post_data = this.variable.post_data;
	
			for (var data in post_data) {
				if (post_data.hasOwnProperty(data)) new_post_data[data] = post_data[data] || '';
			}this.variable.post_data = new_post_data;
		};
	
		this.send_request = function () {
			return part_dialog_loader.load_content(undefined, this.variable.post_data);
		};
	}

/***/ }
/******/ ]);
//# sourceMappingURL=bundle.js.map
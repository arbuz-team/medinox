/**
 * Created by mrskull on 24.11.16.
 */


window.EVENTS = {
  define: new Event('define'),
  redirect: new Event('redirect'),
  reload_website: new Event('reload_website'),

  plugins: {
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
    reload_cart: new Event('cart_reload'),
    reload_searcher: new Event('searcher_reload'),
    reload_ground: new Event('ground_reload'),
    reload_dialog: new Event('dialog_reload'),
  },
};
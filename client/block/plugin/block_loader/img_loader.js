
let $query = function(css_query)
{
  return document.querySelectorAll(css_query);
};

let attr = function(elem, name)
{
  return elem.getAttribute(name);
};


////////////////////////////////////////

export let define = function()
{
  let $images = $query('img'),
    default_src = '/static/img/icons/256/band_aid.png',
    image = new Image();

  function download_img($imgs, i)
  {
    if(!$imgs[i])
      return false;

    let downloadingImage = new Image(),
      data_src = attr($imgs[i], 'data-src'),
      data_src_default = attr($imgs[i], 'data-default-src');

    downloadingImage.onload = function()
    {
      $imgs[i].src = this.src;
      setTimeout(function()
      {
        $imgs[i].style = 'opacity: 1;';
        download_img($images, i + 1);
      }, 100);
    };

    downloadingImage.onerror = function()
    {
      $imgs[i].src = data_src_default || default_src;
      //$imgs[i].alt = 'Sorry, an error has occurred.';
      setTimeout(function()
      {
        $imgs[i].style = 'opacity: 1;';
        $imgs[i].setAttribute('class', 'error');
        download_img($images, i + 1);
      }, 100);
    };

    downloadingImage.src = data_src;
  }

  image.onload = function()
  {
    download_img($images, 0);
  };

  image.src = default_src;

};
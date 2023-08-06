const surveys = new Vue({
    el: '#surveys',
    delimiters: ["[[", "]]"],
    data: {
        surveys: [1, 2, 3, 4, 5],  
    },
});

$(document).ready(function() {

  $("#slider").slider({
    range: true,
    min: 0,
    max: 1000,
    step: 10,
    values: [0, 1000],
    slide: function(event, ui) {
      var delay = function() {
        //var handleIndex = $(ui.handle).data('index.uiSliderHandle');
        var handleIndex = $(ui.handle).index();
        var label = handleIndex == 1 ? '#min' : '#max';
        $(label).html(ui.value ).position({
          my: 'center top',
          at: 'center bottom',
          of: ui.handle,
          offset: "0, 10"
        });
      };

      // wait for the ui.handle to set its position
      setTimeout(delay, 5);
    }
  });

  $('#min').html($('#slider').slider('values', 0)).position({
    my: 'center top',
    at: 'center bottom',
    of: $('#slider span:eq(0)'),
    offset: "0, 10"
  });

  $('#max').html($('#slider').slider('values', 1)).position({
    my: 'center top',
    at: 'center bottom',
    of: $('#slider span:eq(1)'),
    offset: "0, 10"
  });

});



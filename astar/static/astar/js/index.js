$('.ui.radio.checkbox').checkbox();

$('#add_character').click(function() {
    character = $('#character').val();
    weight = $('#weight').val();
    color = $('#color').val();
    if (character && weight && color) {
        $('#tile_config').append(character + ':' + weight + ',' + color + '\n');
        $('#character').val('');
        $('#weight').val('');
        $('#color').val();
    }
});

$('#submit').click(function () {
    $('form').submit();
});

$('.algo').change(function () {
    $('#algo').val($(this).attr('data-value'));
});

$('.color.dropdown .item').each(function () {
    $(this).addClass('ui button');
    $(this).addClass($(this).attr('data-value'));
});

$('.board.dropdown .item').click(function () {
    $('#board_model').val($(this).attr('data-value'));
    $('#submit').click();
});

$('.game.board').ready(function () {
   $('.game.board').css('visibility', 'visible');
});

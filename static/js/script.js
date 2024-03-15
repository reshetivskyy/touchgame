$(function () {
    $(".tabs").tabs();
});

$(document).ready(function () {
    $('.tabs__btns li a').click(function () {
        var images = $(this).find('img');
        images.attr('src', images.data('active'));
        $('.tabs__btns li a').not(this).find('img').attr('src', function () {
            return $(this).data('normal');
        });
    });
});


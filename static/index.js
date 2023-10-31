$(document).ready(function () {
    $("#imageContainer").mouseenter(function () {
        $("#text").fadeIn();
    });
    $("#imageContainer").mouseleave(function () {
        $("#text").fadeOut();
    });
});
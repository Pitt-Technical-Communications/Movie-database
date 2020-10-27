$(document).ready(function () {
    $("#next-button").click(function () {
        location.href="./makeList.html"
    })
    $("#TV-container").on("click","button",function (e) {
        if($(this).hasClass("btn-focus-grey")){
            $(this).removeClass("btn-focus-grey")
        }else{
            $(this).addClass("btn-focus-grey")
        }
    })
})
$(document).ready(function(){
    var bannerHeight = $("#banner").outerHeight(true);
    $("#navbar").affix({
        offset: {
            top:  bannerHeight
        }
    });
    
    $("#navbar").on("affix.bs.affix", function(){
        $("#banner").css("margin-bottom","52px");
    });
    $("#navbar").on("affix-top.bs.affix", function(){
        $("#banner").css("margin-bottom","");
    });

    $("#navbar").on('click', 'a', function(event){
        event.preventDefault();
        if($(this).attr("href") != undefined){
            var element = $($.attr(this, 'href'));
            if(element.length > 0){
                $('html, body').animate({
                    scrollTop: $( $.attr(this, 'href') ).offset().top - 50
                }, 500);
            }
        }
    });

    $(".iframe-container").on("click", function(){
        $(this).children("iframe").addClass("active");
    });

    $(".iframe-container").on("mouseleave", function(){
        $(this).children("iframe").removeClass("active");
    });

    $('.icon-social').tooltip();
	
}); 
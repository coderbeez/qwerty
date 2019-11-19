$(document).ready(function () {

    //GLOBAL VARIABLES
    const star1 = $("[data-star=1]");
    const star2 = $("[data-star=2]");
    const star3 = $("[data-star=3]");
    const star4 = $("[data-star=4]");
    const star5 = $("[data-star=5]");
    const rate = $("[data-star=rate]");
    


    star1.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#4C4C4C");
        star3.css("color", "#4C4C4C");
        star4.css("color", "#4C4C4C");
        star5.css("color", "#4C4C4C");
        rate.val("1");
       
    })

    star2.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#00a9bd");
        star3.css("color", "#4C4C4C");
        star4.css("color", "#4C4C4C");
        star5.css("color", "#4C4C4C");
        rate.val("2");
    })

    star3.click(function () {

        star1.css("color", "#00a9bd");
        star2.css("color", "#00a9bd");
        star3.css("color", "#00a9bd");
        star4.css("color", "#4C4C4C");
        star5.css("color", "#4C4C4C");
        rate.val("3");

    })

    star4.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#00a9bd");
        star3.css("color", "#00a9bd");
        star4.css("color", "#00a9bd");
        star5.css("color", "#4C4C4C");
        rate.val("4");
    })

    star5.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#00a9bd");
        star3.css("color", "#00a9bd");
        star4.css("color", "#00a9bd");
        star5.css("color", "#00a9bd");
        rate.val("5");
    })







});
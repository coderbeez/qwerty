$(document).ready(function () {


    //GLOBAL VARIABLES
    const star1 = $("[data-star=1]");
    const star2 = $("[data-star=2]");
    const star3 = $("[data-star=3]");
    const star4 = $("[data-star=4]");
    const star5 = $("[data-star=5]");
    const rate = $("[data-star=rate]");
    const flag = $("[data-submit=flag]");
    const dark = $("[data-dark=switch]");
    const level1 = $("[data-level=1]");
    const level2 = $("[data-level=2]");
    const level3 = $("[data-level=3]");
    const level4 = $("[data-level=4]");
    const blevel1 = $("[data-blevel=1]");
    const blevel2 = $("[data-blevel=2]");
    const blevel3 = $("[data-blevel=3]");

    //ACCORDION
    level2.hide();
    level3.hide();
    level4.hide();
    //WHERE: https://stackoverflow.com/questions/42541274/jquery-on-page-load-event-not-working


    function slide(target) {
        if (target.is(":hidden")) {
            console.log("hidden")
            target.slideDown();
        } else {
            target.slideUp();
        }
    }
    //WHERE:https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery

    blevel1.click(function () {
        let value = $(this).attr('data-bvalue');
        let target = $('[data-2value="' + value + '"]')
        console.log(value);
        level2.slideUp();
        level3.slideUp();
        level4.slideUp();
        slide(target);
    });


    blevel2.click(function () {
        let value = $(this).attr('data-bvalue');
        let target = $('[data-3value="' + value + '"]')
        console.log(value);
        level3.slideUp();
        level4.slideUp();
        slide(target);
    });

    blevel3.click(function () {
        var value = $(this).attr('data-bvalue');
        let target = $('[data-4value="' + value + '"]')
        console.log(value);
        level4.slideUp();
        slide(target);
    });
    //WHERE: https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute
    //WHERE: https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery

   
    //DARK MODE STYLING CHANGES
    function makeDark() {
        $('body').addClass('dark');
        $('li').addClass('dark');
        $('li').css('border', '1px solid #717c84');
        $('.line').css('border-bottom', '1px solid #717c84');
        $('.btn:not(".button-style")').css('color', '#eda33e');
        $('.btn:not(".button-style")').addClass('dark-hover--stone');
        $('a:not(".dropdown-item")').css('color', '#eda33e');
        $('a:not(".dropdown-item")').addClass('dark-hover');
        $('.button-style').css('color', '#354550');
        $('.button-style').css('background-color', '#ECECEC');
        $('.button-style').addClass('dark-hover--orange');
    }
    //WHERE: https://learn.jquery.com/using-jquery-core/faq/how-do-i-check-uncheck-a-checkbox-input-or-radio-button/
    //WHERE: https://stackoverflow.com/questions/21051440/how-to-define-the-css-hover-state-in-a-jquery-selector
    //WHERE: https://stackoverflow.com/questions/4614120/not-class-selector-in-jquery


    //CHECK FOR DARK MODE
    function checkStorage() {
        if (localStorage.getItem("mode") == "dark") {
            dark.prop("checked", true);
            makeDark();
        }
    }
    //WHERE: https://stackoverflow.com/questions/50933011/read-value-of-localstorage-on-body-load-or-document-ready


    //RUN CHECK 4 MODE ON PAGE LOAD
    checkStorage();


    //RESTYLE IF MODE CHANGES
    dark.change(function () {
        if (this.checked) {
            makeDark();
            localStorage.setItem("mode", "dark")
        } else {
            $('body').removeClass('dark');
            $('li').removeClass('dark');
            $('li').css('border', '');
            $('.line').css('border-bottom', '');
            $('.btn:not(".button-style")').css('color', '');
            $('.btn:not(".button-style")').removeClass('dark-hover--stone');
            $('a:not(".dropdown-item")').css('color', '');
            $('a:not(".dropdown-item")').removeClass('dark-hover');
            $('.button-style').css('color', '');
            $('.button-style').css('background-color', '');
            $('.button-style').removeClass('dark-hover--orange');
            localStorage.clear();
        }
    })
    //WHERE:https://stackoverflow.com/questions/10710674/how-to-remove-and-clear-all-localstorage-data


    //RESTYLE FLAG ICON ON CLICK
    flag.click(function () {
        flag.css("color", "#ED5023");
    })


    //RESTYLE STARS ICONS ON CLICK
    star1.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#c9c9c9");
        star3.css("color", "#c9c9c9");
        star4.css("color", "#c9c9c9");
        star5.css("color", "#c9c9c9");
        rate.val("1");
    })

    star2.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#00a9bd");
        star3.css("color", "#c9c9c9");
        star4.css("color", "#c9c9c9");
        star5.css("color", "#c9c9c9");
        rate.val("2");
    })

    star3.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#00a9bd");
        star3.css("color", "#00a9bd");
        star4.css("color", "#c9c9c9");
        star5.css("color", "#c9c9c9");
        rate.val("3");
    })

    star4.click(function () {
        star1.css("color", "#00a9bd");
        star2.css("color", "#00a9bd");
        star3.css("color", "#00a9bd");
        star4.css("color", "#00a9bd");
        star5.css("color", "#c9c9c9");
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
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
    

    //DARK MODE STYLING CHANGES
    function makeDark() {
        $('body').addClass('dark');
        $('li').addClass('dark');
        $('li').css('border', '1px solid #717c84');
        $('a:not(".dropdown-item")').css('color', '#eda33e');
        $('.btn').css('color', '#eda33e');
        $('.borders-top').css('border-top', 'solid 1px #717c84');
        $('.button-style').css('color', '#354550');
        $('.button-style').css('background-color', '#ECECEC');
        $('a:not(".dropdown-item")').addClass('dark--hover');
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
            $('body').removeClass("dark");
            $('li').removeClass("dark");
            $('a').removeClass("dark--hover");
            $('li').css('border', '');
            $('li').css('border', '');
            $('a').css('color', '');
            $('.btn').css('color', '');
            $('.borders-top').css('color', '');
            $('.button-style').css('color', '');
            $('.button-style').css('background-color', '');
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
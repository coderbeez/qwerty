$(document).ready(function () {

    //GLOBAL VARIABLES - Dark Mode
    const dark = $("[data-dark=switch]");

    //GLOBAL VARIABLES - Accordion
    const level2 = $("[data-level=2]");
    const level3 = $("[data-level=3]");
    const level4 = $("[data-level=4]");
    const blevel1 = $("[data-blevel=1]");
    const blevel2 = $("[data-blevel=2]");
    const blevel3 = $("[data-blevel=3]");

    /**----------------------------------------
    * Dark Mode
    ----------------------------------------*/

    /**
     * Makes styling changes for dark mode.
     * Credit: https://learn.jquery.com/using-jquery-core/faq/how-do-i-check-uncheck-a-checkbox-input-or-radio-button/
     * Credit: https://stackoverflow.com/questions/21051440/how-to-define-the-css-hover-state-in-a-jquery-selector
     * Credit: https://stackoverflow.com/questions/4614120/not-class-selector-in-jquery
     */
    function makeDark() {
        $('body').addClass('dark');
        $('li').addClass('dark');
        $('ul.dark-ul>li').css('border', '1px solid #717c84');
        $('.line').css('border-bottom', '1px solid #717c84');
        $('.btn:not(".button-style")').css('color', '#eda33e');
        $('.btn:not(".button-style")').addClass('dark-hover--stone');
        $('a:not(".dropdown-item")').css('color', '#eda33e');
        $('a:not(".dropdown-item")').addClass('dark-hover');
        $('.button-style').css('color', '#354550');
        $('.button-style').css('background-color', '#ECECEC');
        $('.button-style').addClass('dark-hover--orange');
    }

    /**
     * Checks for Dark Mode on page load.
     * Credit: https://stackoverflow.com/questions/50933011/read-value-of-localstorage-on-body-load-or-document-ready
     */
    function checkStorage() {
        if (localStorage.getItem("mode") == "dark") {
            dark.prop("checked", true);
            makeDark();
        }
    }

    checkStorage();

    /**
     * Restyles if mode changes.
     * Credit: https://stackoverflow.com/questions/10710674/how-to-remove-and-clear-all-localstorage-data
     */
    dark.change(function () {
        if (this.checked) {
            makeDark();
            localStorage.setItem("mode", "dark");
        } else {
            $('body').removeClass('dark');
            $('li').removeClass('dark');
            $('ul.dark-ul>li').css('border', '');
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
    });

    /**----------------------------------------
    * Accordion
    ----------------------------------------*/

    /**
     * Check current state of an accordion target,
     * hides a visible target and reveals a hidden target.
     * Credit: https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery
     */
    function slide(target) {
        if (target.is(":hidden")) {
            target.slideDown();
        } else {
            target.slideUp();
        }
    }

    /**
     * For each level in the accordion
     * allows a button click to slide a target.
     * Data attribute values allow the association of a button
     * to a target when the template is rendered.
     * Credit: https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute
     * Credit: https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery
     */
    blevel1.click(function () {
        let value = $(this).attr('data-bvalue');
        let target = $('[data-2value="' + value + '"]');
        level2.slideUp();
        level3.slideUp();
        level4.slideUp();
        slide(target);
    });

    blevel2.click(function () {
        let value = $(this).attr('data-bvalue');
        let target = $('[data-3value="' + value + '"]');
        level3.slideUp();
        level4.slideUp();
        slide(target);
    });

    blevel3.click(function () {
        let value = $(this).attr('data-bvalue');
        let target = $('[data-4value="' + value + '"]');
        level4.slideUp();
        slide(target);
    });

    /**----------------------------------------
    * Star Rating
    ----------------------------------------*/

    /**
     * Restyles stars on click to better indicate star rating selected.
     */
    $("[data-star]").click(function () {
        $("[data-star]").css("color", "#c9c9c9");
        let rating = $(this).attr("data-star");
        let stars = [$("[data-star=1]"), $("[data-star=2]"), $("[data-star=3]"), $("[data-star=4]"), $("[data-star=5]")]
        $("[data-star=rate]").val(rating);
        stars.forEach(function (star) {
            if (stars.indexOf(star) < rating);
            star.css("color", "#00a9bd");
        })
    })

});
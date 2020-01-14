$(document).ready(function () {

    /**----------------------------------------
    * Dark Mode
    ----------------------------------------*/

    const dark = $("[data-dark=switch]");

    /**
     * Apply styling changes for dark mode.
     * Credits: 
     * https://learn.jquery.com/using-jquery-core/faq/how-do-i-check-uncheck-a-checkbox-input-or-radio-button/
     * https://stackoverflow.com/questions/21051440/how-to-define-the-css-hover-state-in-a-jquery-selector
     * https://stackoverflow.com/questions/4614120/not-class-selector-in-jquery
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
     * Check for Dark Mode on page load.
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
     * Restyle if mode changes.
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
     * Check current state of an accordion target.
     * Hides a visible target and reveals a hidden target.
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
     * For each level in the accordion allows a button click to slide a target.
     * Data attribute values allow the association of a button to a target when the template is rendered.
     * Credit: https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute
     * https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery
     */
    $("[data-blevel]").click(function () {
        console.log('test');
        let blevel = $(this).attr('data-blevel');
        let value = $(this).attr('data-bvalue');
        let target = $('[data-' + blevel + 'value="' + value + '"]');
        let levels = [$("[data-level=1]"), $("[data-level=2]"), $("[data-level=3]"), $("[data-level=4]")];
        levels.forEach(function (level) {
            let index = levels.indexOf(level);
            if (index >= parseInt(blevel)) {
                level.slideUp();
            }
        })
        slide(target);
    });

    /**----------------------------------------
    * Star Rating
    ----------------------------------------*/

    /**
     * Restyle stars on click to better indicate rating selected.
     */
    $("[data-star]").click(function () {
        $("[data-star]").css("color", "#c9c9c9");
        let rating = $(this).attr("data-star");
        let stars = [$("[data-star=1]"), $("[data-star=2]"), $("[data-star=3]"), $("[data-star=4]"), $("[data-star=5]")]
        $("[data-star=rate]").val(rating);
        stars.forEach(function (star) {
            if (stars.indexOf(star) < parseInt(rating)) {
                star.css("color", "#00a9bd");
            }
        });
    });

});
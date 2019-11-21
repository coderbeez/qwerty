$(document).ready(function () {



    //GLOBAL VARIABLES
    const star1 = $("[data-star=1]");
    const star2 = $("[data-star=2]");
    const star3 = $("[data-star=3]");
    const star4 = $("[data-star=4]");
    const star5 = $("[data-star=5]");
    const rate = $("[data-star=rate]");
    const dark = $("[data-dark=switch]");

    checkStorage();

//CHECK FOR DARK MODE
    function checkStorage(){
        if (localStorage.getItem("mode") == "dark") {
    $('body').addClass("dark");  
        } 
    }
    //WHERE: https://stackoverflow.com/questions/50933011/read-value-of-localstorage-on-body-load-or-document-ready

//SET DARK MODE
    dark.change(function () {
        if(this.checked) {
            $('body').addClass("dark");
            localStorage.setItem("mode", "dark")
        }
        else{
            $('body').removeClass("dark");
            localStorage.clear();
        }
        })

        //localStorage.getItem("mode") == "dark"

    // Store
//localStorage.setItem("lastname", "Smith");
// Retrieve
//document.getElementById("result").innerHTML = localStorage.getItem("lastname"); 
    

    flag.click(function () {
        flag.css("color", "#ED5023");
    })


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
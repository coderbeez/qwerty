$(document).ready(function () {

    //GLOBAL VARIABLES
    const star1 = $("[data-star=1]");
    const star2 = $("[data-star=2]");
    const star3 = $("[data-star=3]");
    const star4 = $("[data-star=4]");
    const star5 = $("[data-star=5]");
    const rate = $("[data-star=rate]");
    

    const star_sub1 = $("[data-star=sub1]");
    const star_sub2 = $("[data-star=sub2]");
    const star_sub3 = $("[data-star=sub3]");
    const star_sub4 = $("[data-star=sub4]");
    const star_sub5 = $("[data-star=sub5]");
    const flag = $("[data-flag=flag]");
    const form = $("[data-submit=form]");
    const submit1 = $("[data-submit=submit1]");
    
    


    //submit2.click(function () {
        //star_sub1.css("color", "#00a9bd");
        //star_sub2.css("color", "#c9c9c9");
        //star_sub3.css("color", "#c9c9c9");
        //star_sub4.css("color", "#c9c9c9");
        //star_sub5.css("color", "#c9c9c9");
        //setTimeout(function() {
           //form.submit();
      //},1000);      
    //})

    

    flag.click(function () {
        flag.css("color", "#ED5023");
        //setTimeout(function() {
            //form.submit();
      //},1000);   
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
//WHERE: https://forum.jquery.com/topic/settimeout-before-form-submit








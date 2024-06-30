function getBotResponse(input) {
    //rock paper scissors
    // if (input == "rock") {
    //     return "paper";
    // } else if (input == "paper") {
    //     return "scissors";
    // } else if (input == "scissors") {
    //     return "rock";
    // }

    // Simple responses
    // if (input == "hello") {
    //     return "Hello there!";
    // } else if (input == "goodbye") {
    //     return "Talk to you later!";
    // } 
    // else if (input=='Hiii'){
    //     return "Helo! There"; 
    // }
    // else {
    //     return "Try asking something else!";
    // }   
    url: 
/**
 * xResponse function
 *
 * xResponse method is made to return jQuery ajax response
 * 
 * @param  {string} url   [your url or file]
 * @param  {object} your ajax param
 * @return {mix}       [ajax response]
 */
 $.extend({
    xResponse: function(url, data) {
        // local var
        var theResponse = null;
        // jQuery ajax
        $.ajax({
            url: url,
            type: 'GET',
            data: data,
            dataType: "html",
            async: false,
            success: function(respText) {
                theResponse = respText;
            }
        });
        // Return the response text
        theResponse=theResponse.slice(1, -1);
         return theResponse;
    }
});

// set ajax response in var
var xData = $.xResponse('/chatbot?msg='+input, {issession: 1,selector: true});

// see response in console
return xData;
};
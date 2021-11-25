$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        makePredictions();
    });
});


function makePredictions() {
    var textArea = $("#exampleTextarea").val();


    var payload = {
        "textArea": textArea,
    }

    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
//  this is where the result of the prediction will be returned.  We will need a 
// pop up box or possibly a results page to support the outcome.  
            if (returnedData["prediction"] == 1) {
                $("#output").text("You Survived!");
            } else {
                $("#output").text("You Died!");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}

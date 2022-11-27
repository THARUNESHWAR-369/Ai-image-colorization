
// run loader
function runLoader(){
    toggleDisplay('loader', true);
    $("body").css('overflow', 'hidden');
    $("#model-popup").css("z-index", '-1');
}


// close loader
function closeLoader() {
    toggleDisplay('loader', false);
    $("body").css('overflow', 'auto');
    $("#model-popup").css("z-index", '1');
}

// toggle button
function toggleDisplay(tagId, show) {
    if (show) {
        $('#'+tagId).css('display', 'block');
    }
    else {
        $('#'+tagId).css('display', 'none');
    }
}


// display color image
var loadFile = (event) => {
    console.log("events: ",event.target.files)
    
    toggleDisplay('modal-display-image', true)
    toggleDisplay('colorit-btn', true);

    document.getElementById('model-resp-img').src = URL.createObjectURL(event.target.files[0]);
};

// burl background
function burlBg(show) {
    if (show) {
        $("#bg").addClass('add-blur');
        $("#container").addClass('add-blur');
        $("body").css('overflow', 'hidden');
    }
    else{
        $("#bg").removeClass('add-blur');
        $("#container").removeClass('add-blur');
        $("body").css('overflow', 'auto');
    }
}



// open model
$("#get-start").click(()=>{
    
    toggleDisplay('modal-display-image', false);
    toggleDisplay('modal-display-image-colored', false);
    setTimeout(function() {
        toggleDisplay('model-popup', true);
        burlBg(true);
    }, 100);
});

// close model
$("#close-model").click(()=>{      
    setTimeout(function() {
        toggleDisplay('colorit-btn', false);
        toggleDisplay('download-btn', false);
        toggleDisplay('model-popup', false);

        $("#color-img").val('');
        
        burlBg(false)
    }, 100);
});


// select black and white 
$("#upload-image-btn").click(()=>{
    //console.log("upload image btn clicked")
    document.getElementById("color-img").click()
});



// click colorize button 
$("#colorit-button").click(function(e){

    runLoader();

    let img = document.getElementById('color-img')
    let form_data = new FormData();

    form_data.append("color-img", img.files[0]);

    $.ajax({
        type: "post",
        url: "/",
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: form_data,
        success: function (data) {
            //console.log("DATA: ",data)
            if (data['status'] == true) {
                toggleDisplay('modal-display-image-colored', true);
                document.getElementById('model-resp-img-colored').src = "data:image/gif;base64,"+data['colored_img'];

                toggleDisplay('colorit-btn', false);
                toggleDisplay('download-btn', true)
                
                closeLoader();
    
                $("#download-img").html('<a href=data:image/gif;base64,'+data['colored_img']+' id="download-img-a-tag" target="_blank" download='+data['filename']+'>Download</a>')
            }
        },
        error: (e)=>{
            //console.log("ERROR: ",e);
            closeLoader();
        }
    });
});














// LOVE REACTION
function handleLoveClick(questionId) {
    // Send an AJAX request to increment the love count
    $.ajax({
        type: 'POST',
        url: '{% url "increment_love_count" %}',  // Replace with your backend URL
        data: {
            'question_id': questionId
        },
        success: function(response) {
            // Update the love count button text with the new value
            $('#loveBtn' + questionId).text(response.love_count);
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}


// DEPARTMENT CHOICE DROPDOWN
    $("#id_university").change(function () {
        const url = $("#QuestionForm").attr("data-departments-url");
        const universityId = $(this).val();
        $.ajax({
            url: url,
            data: {
                'university_id': universityId 
            },
            success: function (data) {  
                $("#id_department").html(data);
            }
        });
    });


// COURSE CHOICE DROPDOWN
    $("#id_university, #id_department, #id_year, #id_semester").change(function () {
        const url = $("#QuestionForm").attr("data-courses-url");
        const universityId = $("#id_university").val();
        const departmentId = $("#id_department").val();
        const year = $("#id_year").val();
        const semester = $("#id_semester").val();

        $.ajax({
            url: url,
            data: {
                'university_id': universityId,
                'department_id': departmentId,
                'year': year,
                'semester': semester
            },
            success: function (data) {
                $("#id_course").html(data);
            }
        });
    });

// TEACHER CHOICE DROPDOWN
$("#id_university, #id_department").change(function () {
    const url = $("#QuestionForm").attr("data-teachers-url");
    const universityId = $("#id_university").val();
    const departmentId = $("#id_department").val();

    $.ajax({
        url: url,
        data: {
            'university_id': universityId,
            'department_id': departmentId,
        },
        success: function (data) {
            $("#id_teacher").html(data);
        }
    });
});


// SHARE LINK
// Replace this with your function to retrieve the base URL of your application
function getBaseURL() {
    // Implement the logic to get the base URL of your application
    // This might involve Django's template tags or other methods to obtain the base URL
    return 'http://127.0.0.1:8000/'; // Replace with your actual base URL
}

function generateShareLink(resourceId) {
    var baseUrl = getBaseURL();
    var shareableLink = baseUrl + 'study/share/' + resourceId;

    var tempInput = document.createElement('input');
    tempInput.value = shareableLink;
    document.body.appendChild(tempInput);

    tempInput.select();
    tempInput.setSelectionRange(0, 99999);
    document.execCommand('copy');

    document.body.removeChild(tempInput);

    // Provide a visual cue or message
    var tooltip = document.createElement('div');
    tooltip.textContent = 'Link copied!';
    tooltip.style.position = 'fixed';
    tooltip.style.bottom = '500px';
    tooltip.style.right = '10px';
    tooltip.style.padding = '10px';
    tooltip.style.backgroundColor = '#65a147';
    tooltip.style.color = 'white';
    tooltip.style.borderRadius = '5px';
    tooltip.style.opacity = '0';
    tooltip.style.transition = 'opacity 0.5s';

    document.body.appendChild(tooltip);

    // Show the tooltip
    tooltip.style.opacity = '1';

    // Hide the tooltip after a delay
    setTimeout(function() {
        tooltip.style.opacity = '0';
    }, 3000);  // Adjust the delay (in milliseconds) as needed

    // Optionally, you can also keep the alert message
    alert('Copy the link?');
}





// ============================================================
    window.addEventListener("scroll", function () {
        var header = document.getElementById("main-header");

        // Check if the page has been scrolled down, then apply a class
        if (window.scrollY > 0) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    });

    document.querySelectorAll('.card-flip').forEach(function(card) {
        card.addEventListener('click', function() {
            card.classList.toggle('flipped');
        });
    });


// BACK BUTTON FOR ALL PAGES
    function goBack() {
        window.history.back();
    }
    
// SCROLL TO TOP BUTTON
    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

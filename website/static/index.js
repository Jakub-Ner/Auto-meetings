// this file is connected to base.html so I can override html file
function deleteNote(meetingId){ 
    fetch("/delete-note", { 
        method: "POST", 
        body: JSON.stringify({ meetingId: meetingId }), 
    }).then((_res) => { 
        window.location.href ="/";
    });
}
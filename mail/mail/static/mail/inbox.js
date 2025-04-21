document.addEventListener("DOMContentLoaded", function() {
    // Use buttons to toggle between views
    document
        .querySelector("#inbox")
        .addEventListener("click", () => load_mailbox("inbox"));

    document
        .querySelector("#sent")
        .addEventListener("click", () => load_mailbox("sent"));

    document.querySelector("#archived")
        .addEventListener("click", () => load_mailbox("archived"));

    document.querySelector("#compose").addEventListener("click", compose_email);
    document
        .querySelector("#compose-view")
        .addEventListener("submit", (event) => {
            const body = document.querySelector("#compose-body").value;
            fetch("/emails", {
                    method: "POST",
                    body: JSON.stringify({
                        recipients: document.querySelector("#compose-recipients").value,
                        subject: document.querySelector("#compose-subject").value,
                        body: document.querySelector("#compose-body").value,
                    }),
                })
                .then((response) => response.json())
                .then((result) => {
                    load_mailbox("inbox");

                });
        });

    // By default, load the inbox
    load_mailbox("inbox");
});

function compose_email() {
    // Show compose view and hide other views
    document.querySelector("#emails-view").style.display = "none";
    document.querySelector("#compose-view").style.display = "block";
    document.querySelector("#single-email-view").style.display = "none";
    document.querySelector("#archive").style.display = "none";
    document.querySelector("#unarchive").style.display = "none";
    document.querySelector("#reply").style.display = "none";

    // Clear out composition fields
    document.querySelector("#compose-recipients").value = "";
    document.querySelector("#compose-subject").value = "";
    document.querySelector("#compose-body").value = "";
}

function load_mailbox(mailbox) {
    if (mailbox === "inbox") {
        fetch("/emails/inbox")
            .then((response) => response.json())
            .then((emails) => {
                // Clear the emails view
                document.querySelector("#emails-view").innerHTML = "";

                for (let i = 0; i < emails.length; i++) {
                    // Create a new div
                    const newDiv = document.createElement("div");

                    // Give const to emails with emails[i]
                    const id = emails[i].id;
                    const sender = emails[i].sender;
                    const recipients = emails[i].recipients;
                    let subject = emails[i].subject;
                    const body = emails[i].body;
                    const timestamp = emails[i].timestamp;
                    const read = emails[i].read;
                    const button = document.createElement("button");

                    // Create a new div for each new email
                    newDiv.innerHTML = `<div class="sender">From: ${sender}</div>
                                    <div class="subject">Subject: ${subject}</div>
                                     <div class="timestamp">${timestamp}</div>`;

                    newDiv.classList.add("email-item");
                    // Gets the email view
                    const emailsView = document.getElementById("emails-view");
                    const singleEmailView = document.getElementById("single-email-view");

                    // Add the text node to the newly created div
                    emailsView.appendChild(newDiv);

                    // Hide / Show content (block = show, none = hide)
                    document.querySelector("#emails-view").style.display = "block";
                    document.querySelector("#single-email-view").style.display = "none";
                    document.querySelector("#archive").style.display = "none";
                    document.querySelector("#unarchive").style.display = "none";
                    document.querySelector("#reply").style.display = "none";

                    // Background colour if readed or unread
                    if (read == true) {
                        newDiv.style.backgroundColor = "white";
                    } else {
                        newDiv.style.backgroundColor = "lightblue";
                    }

                    // Make each mail clickable
                    newDiv.addEventListener("click", () => {
                        fetch(`/emails/${id}`, {
                            method: "PUT",
                            body: JSON.stringify({
                                read: true,
                            }),
                        }).then((response) => {
                            if (response.status === 204) {
                                return;
                            }
                            return response.json();
                        });

                        // Print email
                        singleEmailView.innerHTML = `<div class="sender">From: ${sender}</div>
                                                 <div class="sender">To: ${recipients}</div>
                                                 <div class="subject">Subject: ${subject}</div>
                                                 <div class="timestamp"${timestamp}</div>
                                                 <div class="body">${body}</div>`;

                        // Hide / Show content (block = show, none = hide)
                        document.querySelector("#single-email-view").style.display = "block";
                        document.querySelector("#emails-view").style.display = "none";
                        document.querySelector("#archive").style.display = "block";
                        document.querySelector("#unarchive").style.display = "none";
                        document.querySelector("#reply").style.display = "block";

                        // Archive an email
                        document.querySelector("#archive").addEventListener("click", () => {
                            fetch(`/emails/${id}`, {
                                method: "PUT",
                                body: JSON.stringify({
                                    archived: true,
                                }),
                            }).then((response) => {
                                load_mailbox("inbox");
                                if (response.status === 204) {
                                    return;
                                }
                                return response.json();
                            });
                        });



                        // Reply function
                        document.querySelector("#reply").addEventListener("click", (event) => {
                            document.querySelector("#compose-view").style.display = "block";
                            document.querySelector("#compose-recipients").value = sender;
                            if (!subject.startsWith("Re: ")) {
                                subject = "Re: " + subject;
                            }
                            document.querySelector("#compose-body").value = body;
                            document.querySelector("#compose-subject").value = subject;
                            newBody = "On " + timestamp + " " + sender + " " + "Wrote: " + body;
                            document.querySelector("#compose-body").value = newBody;

                        });

                    });
                }
            });

        // Show the mailbox and hide other views
        document.querySelector("#emails-view").style.display = "block";
        document.querySelector("#compose-view").style.display = "none";
        // Show the mailbox name
        document.querySelector("#emails-view").innerHTML =
            `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
    } else if (mailbox === "archived") {
        fetch("/emails/archive")
            .then((response) => response.json())
            .then((emails) => {
                document.querySelector("#emails-view").innerHTML = "";
                for (let i = 0; i < emails.length; i++) {
                    const archiveDiv = document.createElement("div");
                    const emailsView = document.getElementById("emails-view");

                    document.querySelector("#archive").style.display = "none";
                    document.querySelector("#unarchive").style.display = "none";
                    document.querySelector("#reply").style.display = "none";


                    // Get the archive status
                    const archive = emails[i].archived
                    const id = emails[i].id;
                    const sender = emails[i].sender;
                    const recipients = emails[i].recipients;
                    let subject = emails[i].subject;
                    const body = emails[i].body;
                    const timestamp = emails[i].timestamp;

                    if (emails[i].archived === true) {
                        // Create new div to display each archived email

                        document.querySelector("#single-email-view").style.display = "none";
                        archiveDiv.innerHTML = `<div class="sender">Sender: ${sender}</div>
                                                <div class="subject">Subject: ${subject}</div>
                                                <div class="timestamp"> Timestamp:${timestamp}</div> `;

                        archiveDiv.classList.add("email-item");
                        emailsView.appendChild(archiveDiv);
                    }
                    // (Inside for loop) Make each mail clickable
                    archiveDiv.addEventListener("click", () => {
                        fetch(`/emails/${id}`, {
                            method: "PUT",
                            body: JSON.stringify({
                                read: true,
                            }),
                        }).then((response) => {
                            if (response.status === 204) {
                                return;
                            }
                            return response.json();
                        });

                        // Print email
                        const singleEmailView = document.getElementById("single-email-view");
                        singleEmailView.innerHTML = `<div class="sender">From: ${sender}</div>
                 <div class="sender">To: ${recipients}</div>
                 <div class="subject">Subject: ${subject}</div>
                 <div class="timestamp" ${timestamp}</div>
                 <div class="body">${body}</div>`;

                        // Hide / Show content (block = show, none = hide)
                        document.querySelector("#single-email-view").style.display = "block";
                        document.querySelector("#emails-view").style.display = "none";
                        document.querySelector("#archive").style.display = "none";
                        document.querySelector("#unarchive").style.display = "block";
                        document.querySelector("#reply").style.display = "block";

                        // Unarchive
                        document.querySelector("#unarchive").addEventListener("click", () => {
                            fetch(`/emails/${id}`, {
                                method: "PUT",
                                body: JSON.stringify({
                                    archived: false,
                                }),
                            }).then((response) => {
                                load_mailbox("inbox");
                                if (response.status === 204) {
                                    return;
                                }
                                return response.json();
                            })
                        });


                        // Reply function
                        document.querySelector("#reply").addEventListener("submit", (event) => {
                            document.querySelector("#compose-view").style.display = "block";
                            document.querySelector("#compose-recipients").value = sender;
                            document.querySelector("#compose-body").value = body;
                            newBody = "On " + timestamp + " " + sender + " " + "Wrote: " + body;
                            document.querySelector("#compose-body").value = newBody;

                            if (!subject.startsWith("Re: ")) {
                                subject = "Re: " + subject;
                            }
                            document.querySelector("#compose-subject").value = subject;
                        });



                    })
                }
            })
    } else if (mailbox === "sent") {
        fetch("/emails/sent")
            .then((response) => response.json())
            .then((emails) => {
                // Clear the emails view
                document.querySelector("#emails-view").innerHTML = "";
                console.log("Fetching sent emails")

                document.querySelector("#archive").style.display = "none";
                document.querySelector("#unarchive").style.display = "none";
                document.querySelector("#reply").style.display = "none";
                
                for (let i = 0; i < emails.length; i++) {
                    // Create a new div
                    const newDiv = document.createElement("div");

                    // Give const to emails with emails[i]
                    const id = emails[i].id;
                    const sender = emails[i].sender;
                    const recipients = emails[i].recipients;
                    let subject = emails[i].subject;
                    const body = emails[i].body;
                    const timestamp = emails[i].timestamp;
                    const read = emails[i].read;
                    const button = document.createElement("button");
                    const user_email = document.querySelector("h2").textContent;

                    if (user_email === sender) {
                        // Create a new div for each new email
                        newDiv.innerHTML = `<div class="sender">Sender: ${sender}</div>
                                            <div class="subject">subject: ${subject}</div>
                                            <div class="timestamp">${timestamp}</div>`;
                        newDiv.classList.add("email-item");
                        // Gets the email view
                        const emailsView = document.getElementById("emails-view");
                        const singleEmailView = document.getElementById("single-email-view");

                        // Add the text node to the newly created div
                        emailsView.appendChild(newDiv);
                    }

                    // Hide / Show content (block = show, none = hide)
                    document.querySelector("#emails-view").style.display = "block";
                    document.querySelector("#single-email-view").style.display = "none";
                    document.querySelector("#archive").style.display = "none";
                    document.querySelector("#unarchive").style.display = "none";
                    document.querySelector("#reply").style.display = "none";
                }
            })

    }

    // Show the mailbox and hide other views
    document.querySelector("#emails-view").style.display = "block";
    document.querySelector("#compose-view").style.display = "none";

    // Show the mailbox name
    document.querySelector("#emails-view").innerHTML =
        `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

}

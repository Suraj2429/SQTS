const chatBox = document.getElementById("chat-box");
const typing = document.getElementById("typing");
const input = document.getElementById("user-input");

async function sendMessage(){

    const message = input.value.trim();

    if(message === "") return;

    addMessage(message, "user-message");

    input.value = "";

    typing.classList.remove("hidden");

    autoScroll();

    try{

        const response = await fetch(
            `/chat?query=${encodeURIComponent(message)}`
        );

        const data = await response.json();

        typing.classList.add("hidden");

        addMessage(
            formatResponse(data.response),
            "bot-message"
        );

    }catch(error){

        typing.classList.add("hidden");

        addMessage(
            "Something went wrong.",
            "bot-message"
        );
    }

    autoScroll();
}

function addMessage(message, className){

    const div = document.createElement("div");

    div.className = className;

    div.innerHTML = message;

    chatBox.appendChild(div);

    autoScroll();
}

function autoScroll(){

    chatBox.scrollTop = chatBox.scrollHeight;
}

function formatResponse(text){

    return text
        .replace(/\n/g, "<br>")
        .replace(/\*/g, "•");
}

input.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        sendMessage();
    }
});

function showLeadForm(){

    document
        .getElementById("lead-form-container")
        .classList
        .remove("hidden");
}

const leadForm = document.getElementById("lead-form");

leadForm.addEventListener("submit", async function(event){

    event.preventDefault();

    const name =
        document.getElementById("name").value;

    const email =
        document.getElementById("email").value;

    const interest =
        document.getElementById("interest").value;

    try{

        const response = await fetch(
            "/submit-lead",
            {
                method: "POST",
                headers: {
                    "Content-Type":
                    "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams({
                    name,
                    email,
                    interest
                })
            }
        );

        if(!response.ok){

            throw new Error("Submission Failed");
        }

        document
            .getElementById("lead-form-container")
            .classList
            .add("hidden");

        leadForm.reset();

        const popup =
            document.getElementById("success-popup");

        popup.classList.remove("hidden");

        setTimeout(() => {

            popup.classList.add("hidden");

        }, 3000);

    }catch(error){

        alert("Form submission failed.");
    }
});
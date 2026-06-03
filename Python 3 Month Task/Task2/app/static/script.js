window.onload = function(){

    const chatBox = document.getElementById("chat-box");
    const input = document.getElementById("user-input");
    const typing = document.getElementById("typing");

    window.sendMessage = async function(){

        const message = input.value.trim();

        if(message === ""){
            return;
        }

        addMessage(message, "user-message");

        input.value = "";

        typing.classList.remove("hidden");

        try{

            const response = await fetch(
                `/chat?query=${encodeURIComponent(message)}`
            );

            const data = await response.json();

            typing.classList.add("hidden");

            addMessage(
                data.response,
                "bot-message"
            );

        }catch(error){

            typing.classList.add("hidden");

            addMessage(
                "Something went wrong.",
                "bot-message"
            );
        }
    };

    window.sendPreset = function(message){

        input.value = message;

        sendMessage();
    };

    function addMessage(message, className){

        const div = document.createElement("div");

        div.className = className;

        div.innerHTML = message.replace(/\n/g,"<br>");

        chatBox.appendChild(div);

        chatBox.scrollTop = chatBox.scrollHeight;
    }

    input.addEventListener("keypress", function(event){

        if(event.key === "Enter"){
            sendMessage();
        }
    });
};
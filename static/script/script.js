function sendMessage() {
   var userInput = document.getElementById("user-input-field").value;
   if (userInput.trim() !== "") {
      appendUserMessage(userInput);
      getUserResponse(userInput);
      document.getElementById("user-input-field").value = "";
   }
}

function appendUserMessage(message) {
   var chatArea = document.getElementById("chat-area");
   var userMessageElement = document.createElement("div");
   userMessageElement.className = "user-message";
   userMessageElement.textContent = "You: " + message;
   chatArea.appendChild(userMessageElement);
   chatArea.scrollTop = chatArea.scrollHeight;
}

function appendBotMessage(message) {
   var chatArea = document.getElementById("chat-area");
   var botMessageElement = document.createElement("div");
   botMessageElement.className = "bot-message";
   botMessageElement.textContent = "Bot: " + message;
   chatArea.appendChild(botMessageElement);
   chatArea.scrollTop = chatArea.scrollHeight;
}

function getUserResponse(userInput) {
   $.ajax({
      type: "POST",
      url: "/get_bot_response",
      data: { user_input: userInput },
      success: function (response) {
         appendBotMessage(response);
      },
   });
}

const observer = new intersectionObserver((entries) => {
   entries.forEach((entry) => {
      if (entry.intersecting) {
         entry.target.classList.add("show");
      } else {
         entry.target.classList.remove("show");
      }
   });
});

const hiddenElements = document.querySelector(".hidden");
hiddenElements.forEach((el) => observer.observe(el));

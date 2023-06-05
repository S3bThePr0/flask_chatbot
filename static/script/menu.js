function check_chat_name(event) {
   event.preventDefault();
   var chatName = document.querySelector(".chat-name").value;
   if (chatName.length >= 5) {
      alert("Chat created successfully!");
      window.location.href = "/chat";
   } else {
      alert("Insert a name of at least 5 characters.");
   }
}

function clear() {
   location.reload();
}

const observer = new IntersectionObserver((entries) => {
   entries.forEach((entry) => {
      if (entry.isIntersecting) {
         entry.target.classList.add("show");
      } else {
         entry.target.classList.remove("show");
      }
   });
});

const hiddenElements = document.querySelectorAll(".hidden");
hiddenElements.forEach((el) => observer.observe(el));

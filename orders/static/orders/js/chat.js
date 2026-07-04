/**
 * chat.js
 * Handles the chat UI for the order detail page.
 */

const chatMessages = document.getElementById("chat-messages");
const chatInput = document.getElementById("chat-input");
const sendBtn = document.getElementById("send-btn");
const helpCard = document.getElementById("help-card");
const chatBox = document.getElementById("chat-box");

/**
 * Appends a message bubble to the chat window.
 * @param {string} text
 * @param {"customer" | "agent"} type
 */
function appendMessage(text, type) {
  if (!chatMessages) return;

  const div = document.createElement("div");
  div.classList.add(
    type === "customer" ? "customer-message" : "agent-message",
    "p-2",
    "px-3",
  );

  div.innerText = text;
  chatMessages.appendChild(div);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Reads the input, sends the message, and clears the field.
 */
function sendMessage() {
  if (!chatInput) return;

  const message = chatInput.value.trim();
  if (!message) return;

  appendMessage(message, "customer");
  chatInput.value = "";
  chatInput.focus();
}

/**
 * Shows the chat window and hides the help card.
 */
function showChat() {
  if (helpCard) {
    helpCard.style.display = "none";
  }

  if (chatBox) {
    chatBox.style.display = "flex";
    chatBox.classList.add("visible");
  }
}

// Event listeners
if (chatInput) {
  chatInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }
  });
}

if (sendBtn) {
  sendBtn.addEventListener("click", sendMessage);
}

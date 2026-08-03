document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // Upload Section
    // ==========================

    const uploadBox = document.getElementById("uploadBox");
    const browseBtn = document.getElementById("browseBtn");
    const fileInput = document.getElementById("fileInput");
    const selectedFile = document.getElementById("selectedFile");

    browseBtn.addEventListener("click", () => {
        fileInput.click();
    });

    fileInput.addEventListener("change", () => {

        if (fileInput.files.length > 0) {

            selectedFile.innerHTML =
                "📄 " + fileInput.files[0].name;

        }

    });

    uploadBox.addEventListener("dragover", (e) => {

        e.preventDefault();

        uploadBox.style.borderColor = "#2563eb";

        uploadBox.style.background = "#eff6ff";

    });

    uploadBox.addEventListener("dragleave", () => {

        uploadBox.style.borderColor = "#cbd5e1";

        uploadBox.style.background = "";

    });

    uploadBox.addEventListener("drop", (e) => {

        e.preventDefault();

        uploadBox.style.borderColor = "#cbd5e1";

        uploadBox.style.background = "";

        fileInput.files = e.dataTransfer.files;

        if (fileInput.files.length > 0) {

            selectedFile.innerHTML =
                "📄 " + fileInput.files[0].name;

        }

    });

    // ==========================
    // Chat Section
    // ==========================

    const input = document.querySelector(".chat-input input");
    const sendButton = document.querySelector(".chat-input button");
    const chatWindow = document.querySelector(".chat-window");
    const sources = document.querySelector(".sources");

    function addMessage(text, sender) {

        const message = document.createElement("div");

        message.classList.add("message");
        message.classList.add(sender);

        message.innerHTML = text;

        chatWindow.appendChild(message);

        chatWindow.scrollTop = chatWindow.scrollHeight;

    }

    function sendMessage() {

        const question = input.value.trim();

        if (question === "") {

            return;

        }

        addMessage(question, "user");

        input.value = "";

        // Fake AI loading
        setTimeout(() => {

            addMessage(
                "🤖 Backend integration will be added in the next step.",
                "ai"
            );

            sources.innerHTML = `
                <b>Retrieved Sources</b>
                <hr>
                <p>No backend connected yet.</p>
            `;

        }, 700);

    }

    sendButton.addEventListener("click", sendMessage);

    input.addEventListener("keypress", function (event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    });

});
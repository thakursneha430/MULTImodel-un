document.addEventListener("DOMContentLoaded", () => {

    // ==========================================
    // Upload Section
    // ==========================================

    const uploadBox = document.getElementById("uploadBox");
    const browseBtn = document.getElementById("browseBtn");
    const fileInput = document.getElementById("fileInput");
    const selectedFile = document.getElementById("selectedFile");

    browseBtn.addEventListener("click", () => {
        fileInput.click();
    });

    fileInput.addEventListener("change", async () => {

        if (fileInput.files.length === 0) return;

        const file = fileInput.files[0];

        selectedFile.innerHTML = "⏳ Uploading...";

        const formData = new FormData();
        formData.append("file", file);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/upload",
                {
                    method: "POST",
                    body: formData
                }
            );

            const data = await response.json();

            if (!response.ok) {
                selectedFile.innerHTML = "❌ Upload Failed";
                console.error(data);
                return;
            }

            selectedFile.innerHTML =
                `✅ ${data.filename}<br>${data.stored_chunks} chunks indexed`;

        }
        catch (error) {

            console.error(error);

            selectedFile.innerHTML =
                "❌ Backend not running";

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

        fileInput.dispatchEvent(new Event("change"));

    });

    // ==========================================
    // Chat Section
    // ==========================================

    const input = document.querySelector(".chat-input input");
    const sendButton = document.querySelector(".chat-input button");
    const chatWindow = document.querySelector(".chat-window");
    const sources = document.querySelector(".sources");

    let isSending = false;

    function addMessage(text, sender) {

        const message = document.createElement("div");

        message.className = `message ${sender}`;

        message.innerHTML = text;

        chatWindow.appendChild(message);

        chatWindow.scrollTop = chatWindow.scrollHeight;

    }

    async function sendMessage() {

        if (isSending) return;

        const question = input.value.trim();

        if (question === "") return;

        isSending = true;

        console.log("Send button clicked");

        addMessage(question, "user");

        input.value = "";

        addMessage("🤖 Thinking...", "ai");

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/ask",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        question: question
                    })
                }
            );

            const data = await response.json();

            chatWindow.lastChild.remove();

            if (!response.ok) {

                addMessage(
                    "❌ " + (data.detail || "Backend Error"),
                    "ai"
                );

                return;
            }

            addMessage(data.answer, "ai");

            sources.innerHTML =
                "<b>Retrieved Sources</b><hr>";

            if (data.sources && data.sources.length > 0) {

                data.sources.forEach((source, index) => {

                    sources.innerHTML += `
                        <div class="source-card">

                            <b>Source ${index + 1}</b>

                            <br><br>

                            <small>
                                ${source.text}
                            </small>

                            <br><br>

                            <b>Similarity:</b>
                            ${(1 - source.distance).toFixed(2)}

                        </div>

                        <br>
                    `;

                });

            }
            else {

                sources.innerHTML +=
                    "<p>No sources found.</p>";

            }

        }
        catch (error) {

            console.error(error);

            if (chatWindow.lastChild) {
                chatWindow.lastChild.remove();
            }

            addMessage(
                "❌ Unable to connect to backend.",
                "ai"
            );

        }
        finally {

            isSending = false;

        }

    }

    sendButton.addEventListener("click", sendMessage);

    input.addEventListener("keydown", (event) => {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();

        }

    });

});
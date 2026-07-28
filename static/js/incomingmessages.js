async function loadHistory() {

    console.log("Loading history...");
    const response = await fetch("/incomingmessages/messages");
    console.log(response);
    const messages = await response.json();
    console.log(messages);

    messages.forEach(message => {
        console.log("History message:", message);
        addMessage(message);

    });

}


// ===========================================================================================
console.log("JS Loaded");
function connectSSE() {
    console.log("Opening SSE...");
    const source = new EventSource("/stream/messages");
    source.onopen = () => {
        console.log("SSE Connected");
    };

    source.onmessage = (event) => {
        console.log("Received SSE:", event.data);
        const message = JSON.parse(event.data);
        console.log(message);
        addMessage(message);
    };

    source.onerror = (err) => {
        console.log("SSE Error", err);
    };
}
window.onload = () => {
    console.log("Window Loaded");
    loadHistory()
    connectSSE();
};


// =============================================================================================

// function connectSSE() {
//     console.log("Opening SSE...");
//     const source = new EventSource("/stream/messages");
//     source.onmessage = function(event){
//         const message = JSON.parse(event.data);
//         addMessage(message);
//     };
// }


function addMessage(message) {
    console.log("addMessage()", message);
    const list = document.getElementById("message-list");
    const row = document.createElement("div");

    // 👇 Convert Unix timestamp to readable time
    const date = new Date(message.timestamp * 1000);
    const formattedTime = date.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

    row.className = "message-row";
    row.dataset.platform = message.platform.toLowerCase();
    row.innerHTML = `
        <div class="avatar">
            ${message.name[0]}
        </div>

        <div class="content">
            <div>
                <strong>${message.name}</strong>
                <span class="badge">
                    ${message.platform}
                </span>
            </div>

            <div class="preview">
                ${message.text}
            </div>
        </div>

        <div class="time">
            ${new Date(message.timestamp * 1000).toLocaleTimeString()}
        </div>
    `;

    list.prepend(row);
}


const filterButtons = document.querySelectorAll(".filter-btn");
filterButtons.forEach(button => {
    button.addEventListener("click", () => {

        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove("active"));

        // Highlight clicked button
        button.classList.add("active");
        const selectedPlatform = button.dataset.filter;
        const rows = document.querySelectorAll(".message-row");
        rows.forEach(row => {

            if (
                selectedPlatform === "all" ||
                row.dataset.platform === selectedPlatform
            ) {
                row.style.display = "flex";
            } else {
                row.style.display = "none";
            }

        });

    });

});
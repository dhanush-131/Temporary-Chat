from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.routers import web_socket


app = FastAPI(title="Temporary Chat API")

app.include_router(web_socket.router)


@app.get("/")
async def health_check():
    return {"status": "ok"}


@app.get("/chat", response_class=HTMLResponse)
async def chat_page():
    return """
    <!doctype html>
    <html>
      <head>
        <title>Temporary Chat</title>
      </head>
      <body>
        <h1>Temporary Chat</h1>
        <form id="chat-form">
          <input id="message" autocomplete="off" placeholder="Type a message" />
          <button>Send</button>
        </form>
        <ul id="messages"></ul>

        <script>
          const protocol = window.location.protocol === "https:" ? "wss" : "ws";
          const socket = new WebSocket(`${protocol}://${window.location.host}/ws/chat`);
          const form = document.getElementById("chat-form");
          const input = document.getElementById("message");
          const messages = document.getElementById("messages");

          socket.onmessage = (event) => {
            const item = document.createElement("li");
            item.textContent = event.data;
            messages.appendChild(item);
          };

          form.addEventListener("submit", (event) => {
            event.preventDefault();
            if (!input.value.trim()) {
              return;
            }

            socket.send(input.value);
            input.value = "";
          });
        </script>
      </body>
    </html>
    """

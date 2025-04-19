const showResult = (id, message, type = "info") => {
    const element = document.getElementById(id);
    element.className = `mt-3 alert alert-${type}`;
    element.textContent = message;
    element.classList.remove("d-none");
  };
  
  // TEXT
  document.getElementById("textForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = document.getElementById("textInput").value;
  
    const res = await fetch("http://127.0.0.1:8000/predict_text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
  
    const data = await res.json();
    const type = data.result === "Scam" ? "danger" : "success";
    showResult("textResult", `Prediction: ${data.result}`, type);
  });
  
  // VOICE
  document.getElementById("voiceForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", document.getElementById("voiceFile").files[0]);
  
    const res = await fetch("http://127.0.0.1:8000/predict_voice", {
      method: "POST",
      body: formData,
    });
  
    const data = await res.json();
    const type = data.prediction === "Scam" ? "danger" : "success";
    showResult("voiceResult", `Transcription: ${data.transcription}\nPrediction: ${data.prediction}`, type);
  });
  
  // FAKE ACCOUNT
  document.getElementById("fakeForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("name", document.getElementById("accName").value);
    formData.append("followers", document.getElementById("followers").value);
    formData.append("following", document.getElementById("following").value);
    formData.append("file", document.getElementById("profilePic").files[0]);
  
    const res = await fetch("http://127.0.0.1:8000/predict_fake_account", {
      method: "POST",
      body: formData,
    });
  
    const data = await res.json();
    const type = data.is_fake ? "danger" : "success";
    const resultText = data.is_fake ? "Fake Account ❌" : "Genuine Account ✅";
    showResult("fakeResult", `Result: ${resultText}`, type);
  });
  
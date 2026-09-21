document.getElementById('downloadBtn').addEventListener('click', async () => {
  const statusDiv = document.getElementById('status');
  statusDiv.innerText = "Extracting details...";

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  if (!tab.url.includes("sharepoint.com")) {
    statusDiv.innerText = "Error: Open a SharePoint video page!";
    return;
  }

  // Get cookies for sharepoint.com
  chrome.cookies.getAll({ domain: "sharepoint.com" }, function(cookies) {
    let cookieNetscapeText = "# Netscape HTTP Cookie File\n";
    
    cookies.forEach(c => {
      const domain = c.domain.startsWith('.') ? c.domain : '.' + c.domain;
      const includeSubdomains = "TRUE";
      const path = c.path;
      const secure = c.secure ? "TRUE" : "FALSE";
      const expiration = c.expirationDate ? Math.round(c.expirationDate) : "0";
      const name = c.name;
      const value = c.value;

      cookieNetscapeText += `${domain}\t${includeSubdomains}\t${path}\t${secure}\t${expiration}\t${name}\t${value}\n`;
    });

    statusDiv.innerText = "Sending to yt-dlp...";

    fetch("http://127.0.0.1:5000/download", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        url: tab.url,
        cookies: cookieNetscapeText
      })
    })
    .then(res => res.json())
    .then(data => {
      if (data.status === "success") {
        statusDiv.innerText = "Download Started in CMD!";
      } else {
        statusDiv.innerText = "Failed: " + data.message;
      }
    })
    .catch(err => {
      statusDiv.innerText = "Error: Run app.py server first!";
    });
  });
});